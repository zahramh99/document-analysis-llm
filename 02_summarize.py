from transformers import pipeline

def summarize_document(text_file, model="t5-small"):
    """Generates a summary of the document."""
    with open(text_file, "r") as f:
        text = f.read()
    
    summarizer = pipeline("summarization", model=model)
    summary = summarizer(text[:1000], max_length=150, min_length=30)
    return summary[0]['summary_text']

# Example usage:
# summary = summarize_document("data/extracted_text.txt")