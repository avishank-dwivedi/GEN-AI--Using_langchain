from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load environment variables
load_dotenv()

try:
    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    # Initialize embeddings with the smaller model
    embedding = OpenAIEmbeddings(
        model='text-embedding-3-small',  # Using smaller model which is more commonly available
        openai_api_key=api_key
    )

    # Sample documents
    documents = [
        "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
        "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
        "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
        "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
        "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
    ]

    query = 'tell me about bumrah'

    # Generate embeddings
    print("Generating embeddings...")
    doc_embeddings = embedding.embed_documents(documents)
    query_embedding = embedding.embed_query(query)

    # Calculate similarity
    scores = cosine_similarity([query_embedding], doc_embeddings)[0]
    index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

    # Print results
    print("\nQuery:", query)
    print("\nMost similar document:", documents[index])
    print("Similarity score:", score)

except Exception as e:
    print(f"\nError: {str(e)}")
    print("\nTroubleshooting Tips:")
    print("1. Check if your OpenAI API key is valid (not a prototype/test key)")
    print("2. Make sure you have billing set up on your OpenAI account")
    print("3. Verify you have internet connection")
    print("4. Make sure scikit-learn is installed for cosine_similarity")



