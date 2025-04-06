from transformers import pipeline

def generate_questions(passages, model="valhalla/t5-base-qg-hl"):
    """Generates questions from text passages."""
    qg_pipeline = pipeline("text2text-generation", model=model)
    questions = []
    
    for passage in passages:
        input_text = f"generate questions: {passage}"
        results = qg_pipeline(input_text)
        passage_questions = results[0]['generated_text'].split('<sep>')
        questions.extend([q.strip() for q in passage_questions if q.strip()])
    
    return questions

# Example usage:
# questions = generate_questions(passages)