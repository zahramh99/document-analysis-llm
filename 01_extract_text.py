import pdfplumber

def extract_text_from_pdf(pdf_path, output_file):
    """Extracts text from PDF and saves to a .txt file."""
    with pdfplumber.open(pdf_path) as pdf:
        extracted_text = ""
        for page in pdf.pages:
            extracted_text += page.extract_text()
    
    with open(output_file, "w") as f:
        f.write(extracted_text)
    
    print(f"Text extracted to {output_file}")

# Example usage (called from main.py):
# extract_text_from_pdf("data/input.pdf", "data/extracted_text.txt")