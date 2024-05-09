import openai
openai.api_key = 'MY_API_KEY'
prompt = 'What is the capital of Italy?'
 
messages = [{"role": "user", "content": prompt}]
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
)

print(response.choices[0].message.content.strip())
