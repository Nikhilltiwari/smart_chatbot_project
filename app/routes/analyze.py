from flask import Blueprint, request, jsonify
import pandas as pd
from app.utils.data_processing import process_query

analyze_bp = Blueprint('analyze', __name__)
df = pd.DataFrame()  # Global dataframe to store the dataset

@analyze_bp.route('/', methods=['POST'])
def analyze_data():
    global df
    if df.empty:
        return jsonify({'error': 'No data available. Please upload a dataset first.'})
    
    data = request.json
    query = data.get('query')

    try:
        result = process_query(df, query)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

