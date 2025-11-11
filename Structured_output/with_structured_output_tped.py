from langchain_google_genai import GoogleGenAI
from dontenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = GoogleGenAI(model_name="gemini-pro", temperature=0)

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke('''Provide a brief summary and sentiment of the following review: "The product quality is excellent, and I am very satisfied with my purchase."''')

print(type(result))
