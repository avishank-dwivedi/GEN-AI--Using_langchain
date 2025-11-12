from langchain_google_genai import GoogleGenerativeAI

import streamlit as st
from dotenv import load_dotenv
import os
# API key environment mein set honi chahiye
load_dotenv()
# initialize the Google Generative AI model (it will use the API key from environment variables)
model = GoogleGenerativeAI(model="gemini-2.5-flash")

st.header("Research tool")

user_input = st.text_input("Enter your research  query here : ")

if st.button("Get Answer"):
    result = model.invoke(user_input)        
    st.write(result)