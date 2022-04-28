from collections import Counter
from typing import Dict, Any, List

import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype


# - **UNIFORMITY** Is the data in the same format (per column)?
# - **DUPLICATES** Are no duplicates in the data?
# - **MISSING VALUES** Are there any null / missing values?
# - **OUTLIERS** Any outliers in the data (per column)?


def _determine_best_type(value: Any):
    # Workaround, couldn't find an appropriate method from pandas
    try:
        float(value)
        return "numeric"
    except ValueError:
        pass
    return "string"


class DataClass:
    def __init__(self, path: str) -> None:
        self.df: pd.DataFrame = pd.read_csv(path)

    def check_uniformity(self) -> Dict[str, Any]:
        bad_types_by_column = {}
        for column_index in self.df:
            column = self.df[column_index]
            counter = Counter([_determine_best_type(value=value) for value in column])
            if len(counter) > 1:
                most_common_type, _ = counter.most_common()[0]
                non_confirming_indexes = [
                    i
                    for i, value in enumerate(column)
                    if _determine_best_type(value=value) != most_common_type
                ]
                bad_types_by_column[str(column.name)] = non_confirming_indexes
        return bad_types_by_column

    def check_duplicates(self) -> List[int]:
        df = self.df[self.df.duplicated(keep=False)]
        duplicate_rows = df.groupby(list(df)).apply(lambda x: tuple(x.index))
        if not duplicate_rows.empty:
            return duplicate_rows.tolist()
        return []

    def check_missing_values(self) -> List[int]:
        null_data = self.df[self.df.isnull().any(axis=1)]
        return null_data.index.tolist()

    def detect_outliers(self) -> Dict[str, Any]:
        # For simplicity outliers are defined as 3 standard deviations from the mean
        outliers_by_column = {}
        for column_index in self.df:
            column = self.df[column_index]
            if is_numeric_dtype(column):
                outliers = column[((column - column.mean()).abs() > 3 * column.std())]
                outliers_by_column[str(column.name)] = outliers.index.tolist()
        return outliers_by_column

    def generate_report(self) -> Dict[str, Any]:
        report = {
            "UNIFORMITY": self.check_uniformity(),
            "DUPLICATE_ROWS": self.check_duplicates(),
            "MISSING_VALUE_ROWS": self.check_missing_values(),
            "OUTLIERS": self.detect_outliers(),
        }
        return report
