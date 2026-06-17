import gensim.downloader as api
from scipy.spatial.distance import cosine


model = api.load("word2vec-google-news-300")


print("Words most similar to 'king':")
print(model.most_similar("king", topn=5))


print("\nWord analogy result: king - man + woman:")
print(model.most_similar(
    positive=["king", "woman"],
    negative=["man"],
    topn=1
))


sim = 1 - cosine(model["king"], model["queen"])
print("\nSimilarity between 'king' and 'queen':", round(sim, 4))
