from src import (
    extract_text_from_pdf,
    summarize_document,
    split_into_passages,
    generate_questions,
    answer_questions
)

def main():
    # Step 1: Extract text
    extract_text_from_pdf("data/input.pdf", "data/extracted_text.txt")
    
    # Step 2: Summarize
    summary = summarize_document("data/extracted_text.txt")
    print("Summary:", summary)
    
    # Step 3: Split passages
    passages = split_into_passages("data/extracted_text.txt")
    
    # Step 4: Generate questions
    questions = generate_questions(passages[:3])  # Use first 3 passages for demo
    
    # Step 5: Answer questions
    answers = answer_questions(questions, passages)
    
    # Print results
    for qa in answers:
        print(f"Q: {qa['question']}\nA: {qa['answer']}\n")

if __name__ == "__main__":
    main()