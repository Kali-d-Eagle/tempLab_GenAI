# pip install sentence-transformers langchain-cohere cohere
import os
from sentence_transformers import SentenceTransformer
from langchain_cohere import ChatCohere

# Set Cohere API key
os.environ["COHERE_API_KEY"] = "YOUR_API_KEY"

# Load SentenceTransformer embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Cohere Chat Model
llm = ChatCohere(
    model="command-a-03-2025",
    temperature=0.3
)

# User input and text generation
prompt = input("Enter prompt: ")
embedding = embed_model.encode(prompt)
response = llm.invoke(prompt)

print("\nEmbedding Vector (first 10 values):")
print(embedding[:10])

print("\nLLM Response:")
print(response.content)
