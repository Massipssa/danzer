from typing import Any, Dict, Optional

from pyspark.sql import DataFrame

from danzer.anonymizer.datasource.connector.data_connector import DataConnector
from danzer.anonymizer.engine.spark_engine import SparkExecutionEngine
from danzer.anonymizer.infrastructure.datasets.base import Dataset


class SparkDataframe(Dataset):
    def __init__(self,
                 spark_engine: SparkExecutionEngine,
                 spark_config: Optional[Dict[str, Any]],
                 data_connector: DataConnector) -> None:
        super().__init__(
            name="spark-dataset",
            data_connector=data_connector,
            execution_engine=spark_engine,
        )
        self.spark = spark_engine.get_or_create_spark_session(spark_config)

    def read_csv(self,
                 csv_file_path: str,
                 separator: str = None,
                 header=True,
                 infer_schema=True) -> DataFrame:
        return self.spark.read.csv(path=csv_file_path, header=header, inferSchema=infer_schema, sep=separator)

    def read_parquet(self):
        raise NotImplementedError

    def read_from_jdbc(self):
        raise NotImplementedError
