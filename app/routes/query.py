from flask import Blueprint, request, jsonify
from transformers import pipeline
import pandas as pd

query_bp = Blueprint('query', __name__)
nlp = pipeline('question-answering')
df = pd.DataFrame()  # Global dataframe to store the dataset

@query_bp.route('/', methods=['POST'])
def handle_query():
    global df
    if df.empty:
        return jsonify({'error': 'No data available. Please upload a dataset first.'})
    
    data = request.json
    query = data.get('query')
    context = df.to_string()
    result = nlp(question=query, context=context)
    return jsonify({'answer': result['answer']})


