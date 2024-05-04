import os
from openai import OpenAI
from flask import Flask, render_template, jsonify

key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=key)

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', )


@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("Prompt: ", prompt)
  response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=1,
  )
  images = [{'url': image.url} for image in response.data]
  print(response)
  return jsonify({'data': images})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
