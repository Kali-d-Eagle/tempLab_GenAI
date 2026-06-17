import gensim.downloader as api
import random

# Load pre-trained GloVe embedding model
model = api.load("glove-wiki-gigaword-100")

seed = "freedom"
# Get the top 5 most similar words to the seed
words = [w for w, _ in model.most_similar(seed, topn=5)]

# Shuffle the results for random phrase composition
random.shuffle(words)

# Print generated text using semantic association
print(f"In a world of {seed}, people valued {', '.join(words)}.")
