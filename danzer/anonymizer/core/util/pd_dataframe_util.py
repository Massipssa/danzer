import logging
import pandas as pd

from typing import List

from danzer.anonymizer.exceptions.exceptions import DataAnonymizerError


logger = logging.getLogger(__name__)


def all_columns_name_are_valid(df: pd.DataFrame, columns_to_check: List[str]) -> bool:
    """
    Check if all columns are present in pd Dataframe
    """
    invalid_columns = set(columns_to_check) - set(df.columns)
    if len(invalid_columns) > 0:
        raise DataAnonymizerError(f"Columns '{invalid_columns}' are not present in the DataFrame.")
    return True
