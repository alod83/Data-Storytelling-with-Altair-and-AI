import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

model_id = "ft:gpt-3.5-turbo-0613:personal::7t1Xuct5"

completion = openai.ChatCompletion.create(
    model=model_id,
    messages=[
        {
            'role': 'system',
            'content': 'You are a data analyst showing data to a general public.',
        },
        {
            'role': 'user', 
            'content': 'Top sports: rowing (62%) and cycling (58%)'
        },
    ],
)

print(completion.choices[0].message)

