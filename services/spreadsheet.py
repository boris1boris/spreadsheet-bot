
import pandas as pd

class SpreadsheetManager:
    def __init__(self):
        self.data = []

    def add_row(self, row):
        self.data.append(row)

    def to_dataframe(self):
        if not self.data:
            return pd.DataFrame()
        max_len = max(len(row) for row in self.data)
        return pd.DataFrame(self.data, columns=[f"Col{i+1}" for i in range(max_len)])

    def to_string(self):
        df = self.to_dataframe()
        return df.to_markdown(index=False)
