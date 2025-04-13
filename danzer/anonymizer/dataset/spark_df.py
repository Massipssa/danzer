from typing import Optional, Dict, Any

from danzer.anonymizer.core.engine.spark_engine import SparkExecutionEngine
from danzer.anonymizer.dataset.dataset import Dataset
from danzer.anonymizer.dataset.util import get_or_create_spark_session
from danzer.anonymizer.datasource.connector.data_connector import DataConnector
from pyspark.sql import DataFrame


class SparkDataframe(Dataset):

    def __init__(self,
                 spark_engine: SparkExecutionEngine,
                 spark_config: Optional[Dict[str, Any]],
                 data_connector: DataConnector
                 ) -> None:
        self.spark = spark_engine.get_or_create_spark_session(spark_config)
        self.data_connector = data_connector

    def read_csv(self,
                 csv_file_path: str,
                 separator: str = None,
                 header=True,
                 infer_schema=True
                 ) -> DataFrame:
        """
        Read csv file as DataFrame
        # todo: method takes csv_spark_df_config
        """
        return self.spark.read.csv(path=csv_file_path, header=header, inferSchema=infer_schema, sep=separator)

    def read_parquet(self):
        pass

    def read_from_jdbc(self):
        pass
