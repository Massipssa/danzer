import logging
from abc import abstractmethod
from typing import Dict, Union, List

import pandas as pd
from pyspark.sql import DataFrame

from danzer.anonymizer.core.anonymization.anonymization import ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP

from danzer.anonymizer.core.rule import Rule
from danzer.anonymizer.core.util.pd_dataframe_util import all_columns_name_are_valid


class SparkRule(Rule):
    @abstractmethod
    def apply(self, df: "pyspark.sql.DataFrame") -> "pyspark.sql.DataFrame":
        pass


class PandasRule(Rule):
    @abstractmethod
    def apply(self, df: "pandas.DataFrame") -> "pandas.DataFrame":
        pass

# class ColumnSuppression(Action):
#     """
#     Suppresses (drops) specified columns from a pandas or Spark DataFrame.
#     """
#
#     def __init__(self,
#                  df: Union[pd.DataFrame, DataFrame],
#                  params: Dict,
#                  inplace: bool = False,
#                  engine_type: EngineType = EngineType.IN_MEMORY
#                  ):
#
#         self._params = params
#         self._df = df
#         self.inplace = inplace
#         self.engine_type = engine_type


# def operate(self, inplace: bool = True) -> Union[pd.DataFrame, DataFrame]:
#     """
#     Applies column suppression on the DataFrame.
#     """
#     self.validate(params=self._params)
#     if self.engine_type == EngineType.SPARK:
#         logger.info("Suppress column with Spark-Engine")
#         return self._suppress_columns_spark()
#     else:
#         logger.info("Suppress column In-memory")
#         return self._suppress_columns_pandas()

# def validate(self, params: Dict = None) -> None:
#     """
#     Validates the input parameters.
#     """
#     if params.get("operation", None):
#         self._params = params
#         self._columns_to_delete = params["operation"]["columns_to_delete"]
#
# def action_name(self) -> str:
#     return "column-suppression"
#
# def action_type(self) -> ActionType:
#     return ActionType.Anonymize
