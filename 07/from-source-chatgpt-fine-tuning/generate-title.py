import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

model_id = "ft:gpt-3.5-turbo-0613:personal::7svxBPgm"

completion = openai.ChatCompletion.create(
    model=model_id,
    messages=[
        {
            "role": "system",
            "content": "You are a data analyst showing data to a technical audience.",
        },
        {
            "role": "user", 
            "content": "A chart on how to select the best sport to fund"},
    ],
)

print(completion.choices[0].message)

