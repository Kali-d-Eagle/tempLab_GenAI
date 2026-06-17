
! pip install gensim
from gensim. downloader import load
print("Loading pre-trained Glove model (50 dimensions)...")
model = load("glove-wiki-gigaword-50")
def ewr():
  result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)

  print ("Inking - man + woman = ?", result[0][0])

  print ("similarity:", result[0][1])

  result = model.most_similar(positive=['paris', 'italy'], negative=['france'], topn=1)

  print("Inparis - france + italy = ?", result [0][0])

  print("similarity:", result[0][1])

  result = model.most_similar(positive=['programming'], topn=5)

  print("\nTop 5 words similar to 'programming':")

  for word, similarity in result:
    print(word, similarity)

if __name__ == "__main__":
  ewr()

