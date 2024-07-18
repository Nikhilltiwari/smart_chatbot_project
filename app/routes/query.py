from flask import Blueprint, request, jsonify
from transformers import pipeline

query_bp = Blueprint('query', __name__)
nlp = pipeline('question-answering')

@query_bp.route('/', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query')
    result = nlp(question=query, context='Your context here')
    return jsonify({'answer': result['answer']})
