import pandas as pd


class AnonymizationRule:
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError
