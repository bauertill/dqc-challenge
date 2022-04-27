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
            types_in_column = set(type(value) for value in column)
            if len(types_in_column) > 1:
                uniformity_report[
                    str(column.name)
                ] = "contains different types " + " ,".join(str(types_in_column))
        return uniformity_report

    def check_duplicates(self):
        df = self.df[self.df.duplicated(keep=False)]
        duplicate_rows = df.groupby(list(df)).apply(lambda x: tuple(x.index))
        if not duplicate_rows.empty:
            return duplicate_rows.tolist()
        return []

    def generate_report(self) -> Dict[str, Any]:
        report = {
            "UNIFORMITY": self.check_uniformity(),
            "DUPLICATE_ROWS": self.check_duplicates(),
        }
        return report
