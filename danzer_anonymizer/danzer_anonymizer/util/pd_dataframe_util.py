import logging
import pandas as pd

from typing import List

from danzer_anonymizer.danzer_anonymizer.exceptions.exceptions import DataAnonymizerExpectationsError

logger = logging.getLogger(__name__)


def all_columns_name_are_valid(df: pd.DataFrame, columns_to_check: List[str]) -> bool:
    invalid_columns = set(columns_to_check) - set(df.columns)
    if len(invalid_columns) > 0:
        raise DataAnonymizerExpectationsError(f"Columns '{invalid_columns}' are not present in the DataFrame.")
    return True
