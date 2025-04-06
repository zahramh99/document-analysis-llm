# Document Analysis with LLMs

This project analyzes PDF documents using Large Language Models to extract text, generate summaries, create questions, and provide answers. For the official code and details, please refer to this repository.

## Requirements
* Python 3.8 or higher
* Install dependencies: `pip install -r requirements.txt`

## Setup
1. Clone the repo: `git clone https://github.com/yourusername/document-analysis-llm.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your PDF: `cp your_doc.pdf data/input.pdf`

## Usage
To run the full pipeline, execute: `python src/main.py`. To use individual modules, you can do the following: 
```python
from src.summarize import summarize_document
summary = summarize_document("data/extracted_text.txt")

## 📂 Project Structure
`data/` - PDFs and generated files  
  ├── `input.pdf` *(add your PDF here)*  
  └── `extracted_text.txt` *(auto-generated)*  

`src/` - Processing scripts  
  ├── `01_extract_text.py`  
  ├── `02_summarize.py`  
  ...  
  └── `main.py` *(master controller)*  

Root files:  
• `requirements.txt`  
• `README.md`

[... previous sections ...]

## 📝 Notes
• First run downloads NLP models (~500MB)  
• Processing time scales with document size  
• Customize models in individual script files  

## 📜 License 
[MIT License](LICENSE)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)