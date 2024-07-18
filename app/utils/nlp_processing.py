from transformers import pipeline

nlp = pipeline('question-answering')

def process_nlp_query(query, context):
    result = nlp(question=query, context=context)
    return result['answer']
