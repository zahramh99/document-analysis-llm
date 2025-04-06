import nltk
from nltk.tokenize import sent_tokenize

def split_into_passages(text_file, max_words=200):
    """Splits text into passages of ~200 words."""
    nltk.download('punkt')  # Download once
    
    with open(text_file, "r") as f:
        text = f.read()
    
    sentences = sent_tokenize(text)
    passages = []
    current_passage = ""
    
    for sentence in sentences:
        if len(current_passage.split()) + len(sentence.split()) < max_words:
            current_passage += " " + sentence
        else:
            passages.append(current_passage.strip())
            current_passage = sentence
    
    if current_passage:
        passages.append(current_passage.strip())
    
    return passages

# Example usage:
# passages = split_into_passages("data/extracted_text.txt")