from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_len=120):
    if len(text) < 50:
        return text  # Skip summarization for very short text
    return summarizer(text, max_length=max_len, min_length=30, do_sample=False)[0]['summary_text']
