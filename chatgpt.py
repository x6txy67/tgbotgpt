import os

import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(prompt):
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"Error interacting with ChatGPT: {e}")
        return "Sorry, I couldn't process that request."
