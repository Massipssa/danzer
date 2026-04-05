from typing import Dict

from pyspark.sql import DataFrame
import pandas as pd

from danzer.anonymizer.core.action import Action
from danzer.anonymizer.core.engine.execution_engine import EngineType
from danzer.anonymizer.core.rule import ActionType
from danzer.anonymizer.core.util.pd_dataframe_util import all_columns_name_are_valid


class ColumnSuppression(Action):
    """Backward-compatible column suppression entry point used by older tests and runner code."""

    def __init__(self,
                 df: pd.DataFrame | DataFrame,
                 params: Dict,
                 inplace: bool = False,
                 engine_type: EngineType = EngineType.LOCAL):
        self._df = df
        self._params = params or {}
        self.inplace = inplace
        self.engine_type = engine_type
        self._columns_to_delete: list[str] = []

    def validate(self, params: Dict = None) -> None:
        config = params or self._params
        operation = config.get("operation", {})
        self._columns_to_delete = operation.get("columns_to_delete", [])
        self._params = config

    def _suppress_columns_pandas(self) -> pd.DataFrame | None:
        if not self._columns_to_delete:
            return self._df if not self.inplace else None

        try:
            all_columns_name_are_valid(self._df, self._columns_to_delete)
        except Exception:
            return self._df

        if self.inplace:
            self._df.drop(self._columns_to_delete, axis=1, inplace=True)
            return None

        return self._df.drop(self._columns_to_delete, axis=1, inplace=False)

    def _suppress_columns_spark(self) -> DataFrame:
        if not self._columns_to_delete:
            return self._df
        return self._df.drop(*self._columns_to_delete)

    def operate(self):
        self.validate(self._params)
        if self.engine_type == EngineType.SPARK:
            return self._suppress_columns_spark()
        return self._suppress_columns_pandas()

    def apply(self, params: Dict = None):
        if params is not None:
            self.validate(params)
        return self.operate()

    def action_name(self) -> str:
        return "column-suppression"

    def action_type(self) -> ActionType:
        return ActionType.Anonymize
