from transformers import pipeline

# Using BERT model for question-answering
nlp = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')

def get_nlp_pipeline():
    return nlp

