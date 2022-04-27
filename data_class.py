from typing import Dict, Any

import pandas as pd


# - **UNIFORMITY** Is the data in the same format (per column)?
# - **DUPLICATES** Are no duplicates in the data?
# - **MISSING VALUES** Are there any null / missing values?
# - **OUTLIERS** Any outliers in the data (per column)?


class DataClass:
    def __init__(self, path: str) -> None:
        self.df: pd.DataFrame = pd.read_csv(path)

    def check_uniformity(self) -> Dict[str, Any]:
        uniformity_report = {}
        for column_index in self.df:
            column = self.df[column_index]
            for value in column:
                print(type(value))
        return uniformity_report

    def generate_report(self) -> Dict[str, Any]:
        report = {"UNIFORMITY": self.check_uniformity()}
        return report
