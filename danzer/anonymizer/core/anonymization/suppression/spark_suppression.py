from abc import ABC
from typing import Dict

from pyspark.sql import DataFrame

from danzer.anonymizer.core.anonymization.suppression.column_suppression import SparkRule
from danzer.anonymizer.core.rule import ActionType


class SparkSuppressRule(SparkRule, ABC):

    def validate(self, params: Dict = None) -> None:
        if params is not None:
            self.params = params

    def apply(self, df: DataFrame) -> DataFrame:
        """Drop a list of columns from a Spark DataFrame."""
        return df.drop(*self.columns)

    def action_name(self) -> str:
        return "column-suppression"

    def action_type(self) -> ActionType:
        return ActionType.Anonymize

    def name(self) -> str:
        return "suppress"
