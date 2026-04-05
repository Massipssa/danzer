from danzer.anonymizer.infrastructure.engines.base import TabularExecutionEngine
from danzer.anonymizer.infrastructure.engines.local_engine import LocalPandasExecutionEngine
from danzer.anonymizer.infrastructure.engines.spark_engine import SparkTabularExecutionEngine


def build_execution_engine(name: str) -> TabularExecutionEngine:
    if name == "local":
        return LocalPandasExecutionEngine()
    if name == "spark":
        return SparkTabularExecutionEngine()
    raise ValueError(f"Unsupported engine: {name}")
