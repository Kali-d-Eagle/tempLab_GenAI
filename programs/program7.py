from transformers import pipeline

# Initialize summarization pipeline using t5-small model
summarizer = pipeline("summarization", model="t5-small")

text = """
The Industrial Revolution changed society from farming-based to industrial.
Factories, machines, and mass production increased manufacturing and transportation.
"""

# Summarize text with length constraints
summary = summarizer(text, max_length=30, min_length=10, do_sample=False)

# Print the resulting summary text
print(summary[0]['summary_text'])
