from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chat = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

result = chat.invoke("make a song in hindi on cricketer hardik pandya", temperature=0.7, max_output_tokens=50)

print(result.content)