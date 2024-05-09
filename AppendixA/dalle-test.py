import openai
import requests

openai.api_key = 'MY_API_KEY'
prompt = 'Create a painting of a beautiful sunset over a calm lake.'

n=1
response = openai.images.generate(
  prompt=prompt,
  n=n, #A
  size='1024x1024'
)

i = 0
for image_data in response.data:
    print(image_data.url)
    img = requests.get(image_data.url).content
    with open(f"image-{i}.png", 'wb') as handler:
        handler.write(img)
    i += 1

