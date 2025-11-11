from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")
chat_history = [SystemMessage(content='you are a helpful assistant.')]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result =model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("AI: ", result)

print(chat_history)