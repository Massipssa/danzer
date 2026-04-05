import logging
from typing import Dict, List

import pandas as pd
from abc import ABC

from danzer.anonymizer.core.anonymization.suppression.column_suppression import PandasRule
from danzer.anonymizer.core.rule import ActionType
from danzer.anonymizer.core.util.pd_dataframe_util import all_columns_name_are_valid

logger = logging.getLogger(__name__)


class PandasSuppressRule(PandasRule, ABC):

    def __init__(self, columns: list, params: Dict = None, inplace: bool = False):
        super().__init__(columns, params)
        self.inplace = inplace

        self._anonymized_columns: List[str] = []
        self._unanonymized_columns: List[str] = []
        self._methods_applied: Dict[str, str] = {}

    def validate(self, params: Dict = None) -> None:
        if params is not None:
            self.params = params

    def apply(self, df: pd.DataFrame) -> pd.DataFrame | None:
        """Suppress specified columns from a pandas DataFrame."""
        columns_to_delete = self.columns or self.params.get("operation", {}).get("columns_to_delete", [])
        if not columns_to_delete:
            return df if not self.inplace else None

        try:
            all_columns_name_are_valid(df, columns_to_delete)
        except Exception:
            logger.warning("Columns requested for suppression are not present in the DataFrame.")
            return df

        if self.inplace:
            df.drop(columns_to_delete, axis=1, inplace=True)
            self._anonymized_columns.extend(columns_to_delete)
            return None

        df2 = df.copy()
        result = df2.drop(columns_to_delete, axis=1, inplace=False)
        self._anonymized_columns.extend(columns_to_delete)
        return result

    def action_name(self) -> str:
        return "column-suppression"

    def action_type(self) -> ActionType:
        return ActionType.Anonymize

    def name(self) -> str:
        return "suppress"
