from transformers import pipeline

# Using BERT model for question-answering
nlp = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')

def process_nlp_query(query, context):
    result = nlp(question=query, context=context)
    return result['answer']
