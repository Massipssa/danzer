import logging
import pandas as pd

from typing import List, Optional

from danzer_anonymizer.danzer_anonymizer.core.anonymization.anonymization import Anonymization, ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP
from danzer_anonymizer.danzer_anonymizer.util.pd_dataframe_util import all_columns_name_are_valid

logger = logging.getLogger(__name__)


class ColumnSuppression(Anonymization):
    """
    Class that implement Suppression algorithm
    """

    def __init__(self,
                 algorithm_name: str,
                 df: pd.DataFrame,
                 columns_to_delete: List[str],
                 inplace: bool = False,
                 id: Optional[str] = None
                 ):
        super().__init__(algorithm_name, id)

        self._columns_to_delete = columns_to_delete
        self._df = df
        self.inplace = inplace

        # todo: they serve for tracking
        self._anonymized_columns = []
        self._unanonymized_columns = []
        self._methods_applied = {}

    @property
    def columns_to_delete(self) -> List[str]:
        return self._columns_to_delete

    def anonymize(self, inplace: bool = True) -> pd.DataFrame:
        columns_to_delete = self._columns_to_delete
        if all_columns_name_are_valid(self._df, columns_to_delete):
            if self.inplace:
                unanonymized_columns = list(filter(lambda item: item not in self._df.columns,
                                                   columns_to_delete))
                self._df.drop(columns_to_delete, axis=1, inplace=True)

                # todo: move to separate method or class
                self._anonymized_columns.append(columns_to_delete)
                self._unanonymized_columns.append(unanonymized_columns)
                for colum in columns_to_delete:
                    self._methods_applied[colum] = ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP[
                        ColumnSuppression.__name__]
            else:
                df2 = self._df.copy()
                return df2.drop(columns_to_delete, axis=1, inplace=False)
