from data_anonymizer.core.anonymization.column_suppression import ColumnSuppression
from data_anonymizer.util.json_util import read_json_file

ALGO_NAME = "algorithm_name"
COLUMNS = "columns"


def load_column_suppression(config_path: str) -> ColumnSuppression:
    json_data = read_json_file(config_path)
    column_suppression = ColumnSuppression(
        algorithm_name=json_data[ALGO_NAME],
        columns_to_delete=json_data[COLUMNS],
        df=None
    )
    return column_suppression
