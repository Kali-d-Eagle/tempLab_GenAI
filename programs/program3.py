import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import numpy as np

# Medical training corpus
corpus = [
    "patient diagnosed with diabetes",
    "treatment includes antibiotics",
    "vaccine prevents infections",
    "doctor recommends therapy"
]

# Tokenize and lowercase sentences
data = [s.lower().split() for s in corpus]

# Train a Word2Vec model locally
model = Word2Vec(data, vector_size=50, min_count=1)

# Extract vocabulary and vectors
words = list(model.wv.index_to_key)
vectors = np.array([model.wv[w] for w in words])

# Perform t-SNE dimensionality reduction
tsne = TSNE(n_components=2, perplexity=3, random_state=42)
points = tsne.fit_transform(vectors)

# Plot the 2D representations
plt.figure(figsize=(10, 8))
for i, word in enumerate(words):
    plt.scatter(points[i, 0], points[i, 1])
    plt.text(points[i, 0], points[i, 1], f"  {word}", fontsize=12)

plt.title("Medical Word Embeddings (t-SNE projection)")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True)
plt.show()

# Find most similar words to "treatment"
print("Words most similar to 'treatment':")
print(model.wv.most_similar("treatment", topn=3))
