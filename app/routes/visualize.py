from flask import Blueprint, request, jsonify
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

visualize_bp = Blueprint('visualize', __name__)
df = pd.DataFrame()  # Placeholder for the uploaded dataset

@visualize_bp.route('/', methods=['POST'])
def visualize_data():
    global df
    data = request.json
    query = data.get('query')
    if 'sales trend' in query:
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x='Date', y='Sales')
        plt.title('Sales Trend')
        plt.savefig('static/images/sales_trend.png')
        return jsonify({'message': 'Visualization created', 'path': 'static/images/sales_trend.png'})
