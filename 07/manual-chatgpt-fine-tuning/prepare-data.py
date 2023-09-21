import pandas as pd
import json

df = pd.read_csv('general-public.csv')

json_list = []

for index, row in df.iterrows():
    json_object = {
        "messages": [
            {
                "role": "system",
                "content": "You are a data analyst showing data to a general public."
            },
            {
                "role": "user",
                "content": row['prompt']
            },
            {
                "role": "assistant",
                "content": row['completion']
            }
        ]
    }
    json_list.append(json_object)

with open('general-public.jsonl', 'w') as outfile:
    for json_object in json_list:
        json.dump(json_object, outfile)
        outfile.write('\n')

