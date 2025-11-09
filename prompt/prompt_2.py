from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Gemini model
model = GoogleGenerativeAI(model="gemini-2.5-flash")

st.header("🧠 Research Paper Summarization Tool")

# Paper selection
paper_input = st.selectbox(
    "Select research paper name:",
    [
        "Attention is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ]
)

# Summary type selection
system_input = st.selectbox(
    "Select the type of summary you want:",
    ["Technical summary", "Layman summary", "Key points", "Mathematical"]
)

# Length selection
length_input = st.selectbox(
    "Select the length of summary you want:",
    ["Short (1–2 paragraphs)", "Medium (3–4 paragraphs)", "Long (5–6 paragraphs)"]
)

# Define prompt template
template = PromptTemplate(
    template="Provide a {system_input} of the research paper titled '{paper_input}' in {length_input}.",
    input_variables=["system_input", "paper_input", "length_input"]
)

# Format the prompt with selected values
prompt = template.format(
    system_input=system_input,
    paper_input=paper_input,
    length_input=length_input
)

# Run model when button is clicked
if st.button("Get Answer"):
    with st.spinner("Generating summary..."):
        result = model.invoke(prompt)
        st.subheader("📄 Summary:")
        st.write(result)
