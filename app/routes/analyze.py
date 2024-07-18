from flask import Blueprint, request, jsonify
import pandas as pd
from app.utils.data_processing import process_query
from app.utils.context_management import ContextManager

analyze_bp = Blueprint('analyze', __name__)
df = pd.DataFrame()  # Global dataframe to store the dataset
context_manager = ContextManager()

@analyze_bp.route('/', methods=['POST'])
def analyze_data():
    global df
    if df.empty:
        return jsonify({'error': 'No data available. Please upload a dataset first.'})
    
    data = request.json
    query = data.get('query')
    session_id = data.get('session_id')

    try:
        result = process_query(df, query)
        context_response = context_manager.process(query, session_id)
        return jsonify({'result': result, 'context_response': context_response})
    except Exception as e:
        return jsonify({'error': str(e)})



