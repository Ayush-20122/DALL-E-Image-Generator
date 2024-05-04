from openai import OpenAI
import os

key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=key)

response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)
