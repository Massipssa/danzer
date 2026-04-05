from pyspark.sql import SparkSession

from danzer.anonymizer.domain.rules.suppression import ColumnSuppressionRule
from danzer.anonymizer.infrastructure.connectors.filesystem import LocalFileSource
from danzer.anonymizer.infrastructure.engines.base import TabularExecutionEngine


class SparkTabularExecutionEngine(TabularExecutionEngine):
    def __init__(self, spark=None) -> None:
        self.spark = spark or SparkSession.builder.getOrCreate()

    def read(self, source: LocalFileSource):
        return self.spark.read.csv(source.path, header=True, inferSchema=True)

    def apply_rule(self, dataset, rule):
        if isinstance(rule, ColumnSuppressionRule):
            rule.validate()
            return dataset.drop(*rule.columns)
        raise ValueError(f"Unsupported rule: {type(rule).__name__}")

    def write(self, dataset, output_path: str) -> None:
        dataset.write.mode("overwrite").csv(output_path, header=True)
