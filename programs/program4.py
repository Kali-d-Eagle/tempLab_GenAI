
import os
from sentence_transformers import SentenceTransformer
from langchain_cohere import ChatCohere


os.environ["COHERE_API_KEY"] = "cohere_1EG5EOMS8Xwpa7ebiXXK252ThO14BnmYfxcDsQvT1rUxV5"


embed_model = SentenceTransformer("all-MiniLM-L6-v2")


llm = ChatCohere(
    model="command-a-03-2025",
    temperature=0.3
)

while True:

    prompt = input("Enter prompt: ")
    if prompt == "exit":
        break
    embedding = embed_model.encode(prompt)
    response = llm.invoke(prompt)

    print("\nEmbedding Vector (first 10 values):")
    print(embedding[:10])

    print("\nLLM Response:")
    print(response.content)
