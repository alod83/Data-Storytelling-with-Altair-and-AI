import os
import openai
import time

openai.api_key = os.getenv('OPENAI_API_KEY')

# Create a new fine-tuning dataset
dataset = openai.File.create(file=open('general-public.jsonl', 'rb'), purpose='fine-tune')
print('Uploaded file id', dataset.id)

while True:
    print('Waiting while file is processed...')
    file_handle = openai.File.retrieve(id=dataset.id)
    if len(file_handle) and file_handle.status == 'processed':
        print('File processed')
        break
    time.sleep(3)

# Create a new fine-tuning job
job = openai.FineTuningJob.create(training_file=dataset.id, model="gpt-3.5-turbo")

while True:
    print('Waiting while fine-tuning is completed...')
    job_handle = openai.FineTuningJob.retrieve(id=job.id)
    if job_handle.status == 'succeeded':
        print('Fine-tuning complete')
        print('Fine-tuned model info', job_handle)
        print('Model id', job_handle.fine_tuned_model)
        break
    time.sleep(3)