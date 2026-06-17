import gensim.downloader as api
import random


model = api.load("glove-wiki-gigaword-100")

seed = "freedom"

words = [w for w, _ in model.most_similar(seed, topn=5)]


random.shuffle(words)


print(f"In a world of {seed}, people valued {', '.join(words)}.")
