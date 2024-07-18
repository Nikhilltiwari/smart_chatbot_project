from transformers import pipeline

nlp = pipeline('question-answering')

def get_nlp_pipeline():
    return nlp
