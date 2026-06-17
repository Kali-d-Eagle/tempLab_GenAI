from transformers import pipeline


sentiment = pipeline('sentiment-analysis')

texts = [
    "This phone is amazing!",
    "Worst product ever."
]


results = sentiment(texts)


for text, result in zip(texts, results):
    print(text)
    print(result)
