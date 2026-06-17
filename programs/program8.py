import os
from langchain_community.document_loaders import TextLoader
from langchain_cohere import ChatCohere

# Set Cohere API key
os.environ["COHERE_API_KEY"] = "YOUR_API_KEY"

# Load text content using LangChain's TextLoader
loader = TextLoader("teaching.txt")
docs = loader.load()
text = docs[0].page_content

# Initialize ChatCohere model
llm = ChatCohere(model="command-a-03-2025")

# Interactive conversational QA loop
while True:
    q = input("Ask: ")
    if q == "exit":
        break
    prompt = f"Document:\n{text}\n\nQuestion: {q}"
    response = llm.invoke(prompt)
    print("\nAnswer:")
    print(response.content)
