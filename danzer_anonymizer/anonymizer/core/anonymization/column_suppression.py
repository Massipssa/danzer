import logging
from typing import Dict

import pandas as pd
from pyspark.sql import DataFrame

from danzer_anonymizer.anonymizer.core.action import Action, ActionType
from danzer_anonymizer.anonymizer.core.anonymization.anonymization import ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP
from danzer_anonymizer.anonymizer.core.engine.execution_engine import EngineType
from danzer_anonymizer.anonymizer.core.util.pd_dataframe_util import all_columns_name_are_valid

logger = logging.getLogger(__name__)


class ColumnSuppression(Action):
    """
    Class that implement Suppression algorithm
    """

    def __init__(self,
                 df: pd.DataFrame | DataFrame,
                 params: Dict,
                 inplace: bool = False,
                 engine_type: EngineType = EngineType.IN_MEMORY
                 ):

        self._params = params
        self._df = df
        self.inplace = inplace
        self.engine_type = engine_type

        # todo: they serve for tracking
        self._anonymized_columns = []
        self._unanonymized_columns = []
        self._methods_applied = {}

        self._columns_to_delete = []

    def operate(self, inplace: bool = True) -> pd.DataFrame | DataFrame:

        self.validate(params=self._params)
        if self.engine_type == EngineType.SPARK:
            logger.info("Suppress column with Spark-Engine")
            return self.supress_column_from_spark_df()
        else:
            logger.info("Suppress column In-memory")
            return self.supress_columns_from_pandas_df()

    def supress_columns_from_pandas_df(self):
        """
        Suppress a list of columns from pandas Dataframe
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

    def supress_column_from_spark_df(self) -> DataFrame:
        """
        Drop a list of columns from Spark Dataframe
        """
        return self._df.drop(*self._columns_to_delete)

    def validate(self, params: Dict = None) -> None:
        if params.get("operation", None):
            self._params = params
            self._columns_to_delete = params["operation"]["columns_to_delete"]

    def action_name(self) -> str:
        return "column-suppression"

    def action_type(self) -> ActionType:
        return ActionType.Anonymize
