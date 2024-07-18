from flask import Blueprint, request, jsonify
import pandas as pd

upload_bp = Blueprint('upload', __name__)
df = pd.DataFrame()  # Global dataframe to store the dataset

@upload_bp.route('/', methods=['POST'])
def upload_file():
    global df
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    try:
        df = pd.read_csv(file)
        return jsonify({'message': 'File uploaded successfully', 'columns': df.columns.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})
