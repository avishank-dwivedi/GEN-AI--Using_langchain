from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# API key environment mein set honi chahiye
load_dotenv()

# YEH STANDARD LLM MODEL HAI

llm = GoogleGenerativeAI(model="gemini-2.5-flash")

# .invoke() seedha string return karta hai
result = llm.invoke("what is the capital of india?")

print(result)