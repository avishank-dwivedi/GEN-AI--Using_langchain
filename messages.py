from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, who are you?"),
    # AIMessage(content="I am an AI created by Google."),
    # HumanMessage(content="Can you help me?"),
]
result = model.invoke(messages)
messages.append(AIMessage(content=result))
print(messages)