from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

result = chat.invoke("make a song in hindi on cricketer", temperature=0.7, max_output_tokens=50)

print(result.content)