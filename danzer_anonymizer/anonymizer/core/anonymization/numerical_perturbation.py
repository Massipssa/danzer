import logging

import pandas as pd
import numpy as np

from typing import Dict

from pyspark.sql import DataFrame

from danzer_anonymizer.anonymizer.core.action import Action, ActionType
from danzer_anonymizer.anonymizer.core.engine.execution_engine import EngineType

logger = logging.getLogger(__name__)


class NumericalPerturbation(Action):
    """
    Numerical perturbation
    """

    def __init__(self,
                 df: pd.DataFrame | DataFrame,
                 params: Dict,
                 inplace: bool = False,
                 engine_type: EngineType = EngineType.IN_MEMORY,
                 standard_deviation: int = None,
                 ):

        self._df = df
        self._params = params
        self.inplace = inplace
        self.engine_type = engine_type
        self._standard_deviation = standard_deviation

        self._columns_to_anonymize = []

    def operate(self, params: Dict = None) -> pd.DataFrame | DataFrame:

        self.validate(params=self._params)
        if self.engine_type == EngineType.SPARK:
            logger.info("Suppress column with Spark-Engine")
            return self.perturb_spark_df()
        else:
            logger.info("Suppress column In-memory")
            return self.perturb_pandas_df()

    def perturb_pandas_df(self):
        std = self._standard_deviation
        # todo: check that all columns are valid
        for column in self._columns_to_anonymize:
            if std is None:
                std = self._df[column].std()

            with_noise = self._df[column].add(np.random.normal(0, std, self._df.shape[0]))
            df_copy = self._df.copy()
            df_copy[column] = with_noise
        # todo
        return df_copy

    def perturb_spark_df(self) -> DataFrame:
        pass

    def validate(self, params: Dict = None) -> None:
        if params.get("operation", None):
            self._params = params
            self._columns_to_anonymize = params["operation"]["columns_to_delete"]

    def action_name(self):
        return "perturbation"

    def action_type(self):
        return ActionType.Anonymize
