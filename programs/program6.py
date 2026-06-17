from transformers import pipeline

# Initialize Hugging Face sentiment-analysis pipeline
sentiment = pipeline('sentiment-analysis')

texts = [
    "This phone is amazing!",
    "Worst product ever."
]

# Run sentiment inference on list of texts
results = sentiment(texts)

# Print the text and its corresponding sentiment result
for text, result in zip(texts, results):
    print(text)
    print(result)
