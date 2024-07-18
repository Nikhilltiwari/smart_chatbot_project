from transformers import pipeline

# Using BERT model for question-answering
qa_pipeline = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')

def get_nlp_pipeline():
    return qa_pipeline

def process_nlp_query(query, context):
    result = qa_pipeline(question=query, context=context)
    return result['answer']



