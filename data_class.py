import pandas as pd


# - **UNIFORMITY** Is the data in the same format (per column)?
# - **DUPLICATES** Are no duplicates in the data?
# - **MISSING VALUES** Are there any null / missing values?
# - **OUTLIERS** Any outliers in the data (per column)?


class DataClass:
    def __init__(self, path: str) -> None:
        self.df = pd.read_csv(path)

    def _find_hetero_data_types(self) -> str:
        for column_index in self.df:
            column = self.df[column_index]
            for value in column:
                print(type(value))
        pass

    def generate_report(self) -> str:

        return ""
