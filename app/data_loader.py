import json
import pandas as pd

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Invalid JSON format: Expected a list of dictionaries")
        return data
    except Exception as e:
        raise ValueError(f"Error loading JSON file: {str(e)}")