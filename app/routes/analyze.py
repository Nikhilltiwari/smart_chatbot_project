from flask import Blueprint, request, jsonify
import pandas as pd
from app.utils.data_processing import load_dataset
from app.utils.context_management import ContextManager
from app.models.nlp_model import get_nlp_pipeline, process_nlp_query

analyze_bp = Blueprint('analyze', __name__)
df = pd.DataFrame()  # Global dataframe to store the dataset
context_manager = ContextManager()
nlp = get_nlp_pipeline()

@analyze_bp.route('/', methods=['POST'])
def analyze_data():
    global df
    if df.empty:
        return jsonify({'error': 'No data available. Please upload a dataset first.'})
    
    data = request.json
    query = data.get('query')
    session_id = data.get('session_id')

    try:
        context = df.to_string()  # Convert the dataframe to a string context for NLP processing
        context_response = process_nlp_query(query, context)
        return jsonify({'context_response': context_response})
    except Exception as e:
        return jsonify({'error': str(e)})






