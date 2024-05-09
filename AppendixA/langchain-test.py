from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = 'MY_API_KEY'

llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')

print(
    llm.invoke("What is the capital of Italy?")
)
