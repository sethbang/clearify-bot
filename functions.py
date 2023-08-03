import openai
import os
from dotenv import load_dotenv
import re

load_dotenv()

# Load the OpenAI API key from the .env file
openai.organization = os.getenv('OPENAI_ORG')
openai.api_key = os.getenv('OPENAI_API_KEY')


def get_modifier(level):
    # Search for the first group of characters surrounded by @ symbols in the level string
    match = re.search(r'@([^@]+)@', level)
    if match:
        # Return the group of characters that were surrounded by @ symbols
        return match.group(1).strip()
    else:
        # If there was no match, return the default modifier
        return 'layman'


def clearify(parent_comment, level="layman", oai_model="gpt-3.5-turbo"):

    # Generate a clarification from the model
    completion = openai.ChatCompletion.create(
        model=oai_model,
        messages=[
            {"role": "system", "content": f"You are an assistant who helps clarify a comment so that I can understand it as a {level}. Make sure you take into account that you are explaining this to a {level}."},
            {"role": "user", "content": f"Remember that I am a person without professional or specialized knowledge in the comments subject matter, and specifically I am a {level}. Now, can you please clarify this comment: {parent_comment}"}
        ]
    )
    return completion
