!pip install langchain_community
!pip install langchain_cohere
import os
from langchain_community.document_loaders import TextLoader
from langchain_cohere import ChatCohere


os.environ["COHERE_API_KEY"] = "cohere_1EG5EOMS8Xwpa7ebiXXK252ThO14BnmYfxcDsQvT1rUxV5"

from google.colab import files

uploaded = files.upload()

# upload ur chess.txt file

loader = TextLoader("chess.txt")
docs = loader.load()
text = docs[0].page_content


llm = ChatCohere(model="command-a-03-2025")


while True:
    q = input("Ask: ")
    if q == "exit":
        break
    prompt = f"Document:\n{text}\n\nQuestion: {q}"
    response = llm.invoke(prompt)
    print("\nAnswer:")
    print(response.content)
