import pandas as pd
from datetime import datetime

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        df = pd.read_csv(self.file_path)
        df['gregorian_date'] = pd.to_datetime(df['gregorian_date'])
        df['hijri_date'] = pd.to_datetime(df['hijri_date'])
        return df