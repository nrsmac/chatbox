import os

from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(input_text):
    # Set OpenAI API and get key from dotenv
    llm = OpenAI(temperature=0.9, openai_api_key=os.getenv("OPENAI_API_KEY"))
    return llm(input_text)
