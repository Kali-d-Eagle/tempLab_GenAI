from transformers import pipeline


sentiment = pipeline('sentiment-analysis')

# add more sentences...(+ve | -ve)
texts = [
    "This phone is amazing!",
    "Worst product ever."
]


results = sentiment(texts)


for text, result in zip(texts, results):
    print(text)
    print(result)
