from transformers import pipeline

def answer_questions(questions, passages, model="deepset/roberta-base-squad2"):
    """Answers questions using document passages as context."""
    qa_pipeline = pipeline("question-answering", model=model)
    answers = []
    
    for question in questions:
        for passage in passages:
            answer = qa_pipeline(question=question, context=passage)
            answers.append({
                "question": question,
                "answer": answer['answer'],
                "score": answer['score']
            })
    
    return answers

# Example usage:
# answers = answer_questions(questions, passages)