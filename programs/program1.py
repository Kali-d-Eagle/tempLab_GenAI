import gensim.downloader as api
from scipy.spatial.distance import cosine

# Load pre-trained Word2Vec model (google news 300 dimensions)
model = api.load("word2vec-google-news-300")

# Find most similar words to "king"
print("Words most similar to 'king':")
print(model.most_similar("king", topn=5))

# Perform word vector arithmetic: king - man + woman = queen
print("\nWord analogy result: king - man + woman:")
print(model.most_similar(
    positive=["king", "woman"],
    negative=["man"],
    topn=1
))

# Calculate cosine similarity between "king" and "queen"
sim = 1 - cosine(model["king"], model["queen"])
print("\nSimilarity between 'king' and 'queen':", round(sim, 4))
