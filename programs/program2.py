import gensim.downloader as api
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load pre-trained Word2Vec model
model = api.load("word2vec-google-news-300")

# Define target words and extract their vectors
words = ['computer', 'internet', 'software', 'hardware', 'server']
vectors = [model[w] for w in words]

# Perform PCA to reduce dimensionality to 2D
pca = PCA(n_components=2)
points = pca.fit_transform(vectors)

# Print most similar words to "computer"
print("Words most similar to 'computer':")
print(model.most_similar("computer", topn=5))

# Plot the 2D representations of word embeddings
plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    plt.scatter(points[i, 0], points[i, 1])
    plt.text(points[i, 0], points[i, 1], f"  {word}", fontsize=12)

plt.title("Word Embeddings (2D PCA projection)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True)
plt.show()
