import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import numpy as np


corpus = [
    "patient diagnosed with diabetes",
    "treatment includes antibiotics",
    "vaccine prevents infections",
    "doctor recommends therapy"
]


data = [s.lower().split() for s in corpus]


model = Word2Vec(data, vector_size=50, min_count=1)


words = list(model.wv.index_to_key)
vectors = np.array([model.wv[w] for w in words])


tsne = TSNE(n_components=2, perplexity=3, random_state=42)
points = tsne.fit_transform(vectors)


plt.figure(figsize=(10, 8))
for i, word in enumerate(words):
    plt.scatter(points[i, 0], points[i, 1])
    plt.text(points[i, 0], points[i, 1], f"  {word}", fontsize=12)

plt.title("Medical Word Embeddings (t-SNE projection)")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True)
plt.show()


print("Words most similar to 'treatment':")
print(model.wv.most_similar("treatment", topn=3))
