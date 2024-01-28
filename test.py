from io import BytesIO

import requests
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image

load_dotenv()

client = OpenAI()

prompt = input("Prompt: ")

if prompt == "":
    print("No prompt provided. Exiting...")
    exit(1)

print("Generating image...")

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="hd",
    n=1,
)

image_url = response.data[0].url

print("Image URL: " + image_url)
print()

# Download the image content
image_response = requests.get(image_url)
image_content = Image.open(BytesIO(image_response.content))

# Save the image as a PNG file
output_image_path = "generated_image.png"
image_content.save(output_image_path, format="PNG")

print(f"Image has been saved to {output_image_path}")
