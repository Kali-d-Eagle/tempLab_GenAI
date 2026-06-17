from transformers import pipeline


summarizer = pipeline("summarization", model="t5-small")

text = """
The Industrial Revolution changed society from farming-based to industrial.
Factories, machines, and mass production increased manufacturing and transportation.
"""


summary = summarizer(text, max_length=30, min_length=10, do_sample=False)


print(summary[0]['summary_text'])
