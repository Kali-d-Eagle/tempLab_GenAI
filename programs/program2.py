
!pip install gensim

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.downloader import load
def reduce_dimensions (embeddings):
  pca = PCA(n_components=2)
  reduced_embeddings = pca.fit_transform(embeddings)
  return reduced_embeddings
def visualize_embedding(words, reduced_embeddings) :

  plt.figure(figsize=(10, 6))

  for i, word in enumerate(words):

    x, y = reduced_embeddings[i]

    plt.scatter(x, y, color= 'blue', marker='o')
    plt.text(x + 0.02, y+ 0.02, word, fontsize=12)

  plt.title("2D Visualization of word Embeddings")

  plt.xlabel("PCA Component 1")

  plt.ylabel("PCA Component 2")

  plt.grid()

  plt.show()

def get_similar_words(word, model):
  print(f"Top 5 words similar to '(word):")
  similar_words = model.most_similar(word, topn=10)

  for similar_word, similarity in similar_words:

    print (f"{similar_word} ({similarity: 4f})")
print("Loading pre-trained Glove model (50 dimensions)...")
model = load("glove-wiki-gigaword-50")
words=['football','basketball','soccer','tennis','cricket','hockey','baseball','golf','volleyball','rugby']
embeddings = [model[word] for word in words]
reduced_embeddings = reduce_dimensions (embeddings)
visualize_embedding(words, reduced_embeddings)
get_similar_words("programming", model)
