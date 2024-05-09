import openai
import requests

openai.api_key = ''
prompt = 'Create a painting of a beautiful sunset over a calm lake.'

response = openai.Image.create(
  prompt=prompt,
  n=1, #A
  size='1024x1024'
)
image_url = response['data'][0]['url']

img_data = requests.get(image_url).content
with open('image.png', 'wb') as handler:
    handler.write(img_data)


