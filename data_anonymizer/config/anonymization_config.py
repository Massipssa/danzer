from typing import Dict, Any

from data_anonymizer.core.anonymization.column_suppression import ColumnSuppression

ALGO_NAME = "algorithm_name"
COLUMNS = "columns"


def load_column_suppression(json_data: Dict[str, Any]) -> ColumnSuppression:
    column_suppression = ColumnSuppression(
        algorithm_name=json_data[ALGO_NAME],
        columns_to_delete=json_data[COLUMNS],
        df=None
    )
    return column_suppression
