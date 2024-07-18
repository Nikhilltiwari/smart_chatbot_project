import pandas as pd

def load_dataset(file):
    df = pd.read_csv(file)
    return df

def process_query(df, query):
    try:
        if 'average' in query:
            column = extract_column(query, 'average')
            if column:
                average_value = df[column].mean()
                return {f'average_{column}': average_value}
        elif 'maximum' in query or 'max' in query:
            column = extract_column(query, 'maximum')
            if column:
                max_value = df[column].max()
                return {f'maximum_{column}': max_value}
        elif 'minimum' in query or 'min' in query:
            column = extract_column(query, 'minimum')
            if column:
                min_value = df[column].min()
                return {f'minimum_{column}': min_value}
        else:
            return {'error': 'Unknown query'}
    except Exception as e:
        return {'error': str(e)}

def extract_column(query, operation):
    words = query.split()
    for i, word in enumerate(words):
        if word.lower() == operation:
            if i + 1 < len(words):
                return words[i + 1]
    return None


