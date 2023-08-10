import logging
import pandas as pd

from typing import List, Optional

from data_anonymizer.core.anonymization.anonymization import Anonymization
from data_anonymizer.util.pd_dataframe_util import all_columns_name_are_valid

logger = logging.getLogger(__name__)


class ColumnSuppression(Anonymization):
    """
    Class that implement Suppression algorithm
    """
    def __init__(self,
                 algorithm_name: str,
                 df: pd.DataFrame,
                 columns_to_delete: List[str],
                 id: Optional[str] = None
                 ):
        super().__init__(algorithm_name, id)

        self._columns_to_delete = columns_to_delete
        self._df = df
        self.all_columns = list(map(str, self._df.columns.tolist()))
        self.anonymized_columns = []
        self.unanonymized_columns = self.all_columns.copy()

    def anonymize(self, inplace: bool = True) -> pd.DataFrame:
        if all_columns_name_are_valid(self._df, self._columns_to_delete):
            # todo: review
            if self._columns_to_delete in self.anonymized_columns:
                pass

            return self._df.drop(self._columns_to_delete, axis=1, inplace=True)
