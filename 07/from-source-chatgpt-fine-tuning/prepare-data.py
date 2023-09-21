# import required libraries
# load the medium-articles.csv file as a dataframe
# convert the dataframe to the following JSON format:
# For each row in the dataframe produce the following JSON object:
# [{"messages": general technical audience."}, 
#  {"role": "user", "content": <prompt column of the dataframe>}, 
#  {"role": "assistant", "content": <completion column of the dataframe>}]}]
# save the JSON object to a file called 'medium-articles.jsonl'

import pandas as pd
import json

df = pd.read_csv('medium-articles.csv')

json_list = []

for index, row in df.iterrows():
    json_object = {
        "messages": [
            {
                "role": "system",
                "content": "You are a data analyst showing data to a technical audience."
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

with open('technical-audience.jsonl', 'w') as outfile:
    for json_object in json_list:
        json.dump(json_object, outfile)
        outfile.write('\n')

# Path: chatgpt-fine-tuning/prepare-data.py
