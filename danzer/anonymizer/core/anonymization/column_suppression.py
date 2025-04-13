import logging
from typing import Dict, Union, List

import pandas as pd
from pyspark.sql import DataFrame

from danzer.anonymizer.core.action import Action, ActionType
from danzer.anonymizer.core.anonymization.anonymization import ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP
from danzer.anonymizer.core.engine.execution_engine import EngineType
from danzer.anonymizer.core.util.pd_dataframe_util import all_columns_name_are_valid

logger = logging.getLogger(__name__)


class ColumnSuppression(Action):
    """
    Suppresses (drops) specified columns from a pandas or Spark DataFrame.
    """

    def __init__(self,
                 df: Union[pd.DataFrame, DataFrame],
                 params: Dict,
                 inplace: bool = False,
                 engine_type: EngineType = EngineType.IN_MEMORY
                 ):

        self._params = params
        self._df = df
        self.inplace = inplace
        self.engine_type = engine_type

        # todo: they serve for tracking
        self._anonymized_columns: List[str] = []
        self._unanonymized_columns: List[str] = []
        self._methods_applied: Dict[str] = {}

        self._columns_to_delete: List[str] = []

    def operate(self, inplace: bool = True) -> Union[pd.DataFrame, DataFrame]:
        """
        Applies column suppression on the DataFrame.
        """
        self.validate(params=self._params)
        if self.engine_type == EngineType.SPARK:
            logger.info("Suppress column with Spark-Engine")
            return self._suppress_columns_spark()
        else:
            logger.info("Suppress column In-memory")
            return self._suppress_columns_pandas()

    def _suppress_columns_pandas(self) -> Union[pd.DataFrame, None]:
        """
        Suppress specified columns from a pandas DataFrame.
        Returns a new DataFrame if not inplace.
        """
        if all_columns_name_are_valid(self._df, self._columns_to_delete):
            if self.inplace:
                unanonymized_columns = list(filter(lambda item: item not in self._df.columns,
                                                   self._columns_to_delete))
                self._df.drop(self._columns_to_delete, axis=1, inplace=True)

                # todo: move to separate method or class
                self._anonymized_columns.append(self._columns_to_delete)
                self._unanonymized_columns.append(unanonymized_columns)
                for colum in self._columns_to_delete:
                    self._methods_applied[colum] = ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP[
                        ColumnSuppression.__name__]
            else:
                logger.info("Delete column in fly")
                df2 = self._df.copy()
                return df2.drop(self._columns_to_delete, axis=1, inplace=False)

    def _suppress_columns_spark(self) -> DataFrame:
        """
        Drop a list of columns from Spark Dataframe
        """
        return self._df.drop(*self._columns_to_delete)

    def validate(self, params: Dict = None) -> None:
        """
        Validates the input parameters.
        """
        if params.get("operation", None):
            self._params = params
            self._columns_to_delete = params["operation"]["columns_to_delete"]

    def action_name(self) -> str:
        return "column-suppression"

    def action_type(self) -> ActionType:
        return ActionType.Anonymize
