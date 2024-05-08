import openai
openai.api_key = 'MY API KEY'
prompt = 'What is the capital of Italy?'
 
messages = [{"role": "user", "content": prompt}]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
)
output = response.choices[0].message["content"]
print(output)