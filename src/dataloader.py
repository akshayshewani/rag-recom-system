import pandas as pd

class DataLoader:
    def __init__(self, file_path: str, processed_file:str):
        self.file_path = file_path
        self.processed_file = processed_file

    def load_data(self) -> pd.DataFrame:
        """Load data from a CSV file and return as a pandas DataFrame."""
        try:
            data = pd.read_excel(self.file_path)
            
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
