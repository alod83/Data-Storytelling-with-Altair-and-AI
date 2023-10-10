# pip install langchain
# pip install langchain[html]
# pip install langchain[llm]
# pip install unstructured
# pip install pydantic==1.10.11
# pip install chromadb
# pip install tiktoken

# pdf2image
# pdfminer
# pdfminer.six
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# download the following HTML page:
# https://www.fda.gov/food/seafood-guidance-documents-regulatory-information/aquacultured-seafood

#from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import PDFMinerLoader

# Download the document from https://digitalmaine.com/cgi/viewcontent.cgi?article=1007&context=dmr_docs
# and export only pp. 28-32 as a PDF and save it as GovernorTaskForce.pdf
loader = PDFMinerLoader("GovernorTaskForce.pdf")

data = loader.load()


# load data
#loader = UnstructuredHTMLLoader('aquaculture.html')
#data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap  = 20,
    length_function = len,
    is_separator_regex = False,
)

splitted_data = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings()

store = Chroma.from_documents(
    splitted_data, 
    embeddings, 
    ids = [f"{item.metadata['source']}-{index}" for index, item in enumerate(splitted_data)],
    collection_name='aquaculture',
persist_directory='db',
)
store.persist()

template = """You are a bot that generates commentaries of 200 characters for graphs based on the context and question provided.
If you don't know the answer, simply state that you don't know.

{context}

question: {question}"""

prompt = PromptTemplate(
    template=template, input_variables=['context', 'question']
)

llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=store.as_retriever(),
    chain_type_kwargs={"prompt": prompt, },
    return_source_documents=True,
)

print(
    #qa('Describe aquaculture in the U.S.')
    qa('In the U.S. there was a reduction in sales of cultivated salmon in the 1990s, only to recover in subsequent years. Explain why this phenomenon happened.')
)