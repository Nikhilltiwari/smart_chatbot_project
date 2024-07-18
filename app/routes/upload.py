from flask import Blueprint, request, render_template, redirect, url_for, jsonify
import pandas as pd
from app.utils.data_processing import load_dataset

upload_bp = Blueprint('upload', __name__)
df = pd.DataFrame()  # Global dataframe to store the dataset

@upload_bp.route('/', methods=['GET', 'POST'])
def upload_file():
    global df
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        try:
            df = load_dataset(file)
            return redirect(url_for('upload.upload_file'))
        except Exception as e:
            return jsonify({'error': str(e)})
    return render_template('index.html', columns=df.columns.tolist())
