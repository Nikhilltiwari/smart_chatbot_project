import pandas as pd

def load_dataset(file):
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please upload a .csv or .xls/.xlsx file.")
    return df



