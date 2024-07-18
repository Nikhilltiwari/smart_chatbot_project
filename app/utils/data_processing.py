import pandas as pd

def load_dataset(file):
    # Check file extension to determine how to load the dataset
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please upload a .csv or .xls/.xlsx file.")
    return df

def process_query(df, query):
    try:
        query_lower = query.lower()
        if "average" in query_lower:
            column = extract_column(query_lower, 'average')
            if column in df.columns:
                average_value = df[column].mean()
                return {f'average_{column}': average_value}
        elif "maximum" in query_lower or "max" in query_lower:
            column = extract_column(query_lower, 'maximum')
            if column in df.columns:
                max_value = df[column].max()
                return {f'maximum_{column}': max_value}
        elif "minimum" in query_lower or "min" in query_lower:
            column = extract_column(query_lower, 'minimum')
            if column in df.columns:
                min_value = df[column].min()
                return {f'minimum_{column}': min_value}
        elif "highest salary" in query_lower:
            highest_salary_idx = df['Annual Salary'].idxmax()
            employee_name = df.loc[highest_salary_idx, 'Name']
            return {f'employee_with_highest_salary': employee_name}
        else:
            return {'error': 'Unknown query'}
    except Exception as e:
        return {'error': str(e)}

def extract_column(query, operation):
    words = query.split()
    if operation in words:
        idx = words.index(operation) + 1
        if idx < len(words):
            return words[idx]
    return None


