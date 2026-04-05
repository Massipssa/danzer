import pandas as pd

from danzer.anonymizer.domain.rules.suppression import ColumnSuppressionRule
from danzer.anonymizer.infrastructure.connectors.filesystem import LocalFileSource
from danzer.anonymizer.infrastructure.engines.base import TabularExecutionEngine


class LocalPandasExecutionEngine(TabularExecutionEngine):
    def read(self, source: LocalFileSource):
        return pd.read_csv(source.path)

    def apply_rule(self, dataset, rule):
        if isinstance(rule, ColumnSuppressionRule):
            rule.validate()
            return dataset.drop(columns=rule.columns)
        raise ValueError(f"Unsupported rule: {type(rule).__name__}")

    def write(self, dataset, output_path: str) -> None:
        dataset.to_csv(output_path, index=False)
