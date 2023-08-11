import pandas as pd
import numpy as np

from typing import Optional, List

from data_anonymizer.core.anonymization.anonymization import Anonymization


class NumericalPerturbation(Anonymization):
    """
    Numerical perturbation
    """

    def __init__(self,
                 algorithm_name: str,
                 df: pd.DataFrame,
                 columns_to_anonymize: List[str],
                 standard_deviation: int = None,
                 id: Optional[str] = None
                 ):
        super().__init__(algorithm_name, id)

        self._columns_to_anonymize = columns_to_anonymize
        self._df = df
        self._standard_deviation = standard_deviation

    def anonymize(self) -> pd.DataFrame:
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
