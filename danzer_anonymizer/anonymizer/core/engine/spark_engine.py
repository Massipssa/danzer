import pyspark
from typing import Optional
from pyspark.sql import SparkSession, DataFrame
# todo
#from pyspark.sql.connect.session import SparkSession as SparkConnectSession

from danzer_anonymizer.anonymizer.core.engine.execution_engine import ExecutionEngine
from danzer_anonymizer.anonymizer.datasource.connector.data_connector import DataConnector
from danzer_anonymizer.anonymizer.datasource.connector.file_system_connector import FileSystemConnector


class SparkExecutionEngine(ExecutionEngine):

    def __init__(self,
                 name: str | None = None,
                 spark_config: Optional[dict] = None,
                 spark: Optional[SparkSession] = None,
                 data_connector: DataConnector = None) -> None:
        super().__init__(name)

        spark_config = spark_config or {}
        self.spark: pyspark.SparkSession
        if spark:
            self.spark = spark
        else:
            self.spark = SparkExecutionEngine.get_or_create_spark_session(
                spark_config=spark_config,
            )
        self.data_connector = data_connector

    @staticmethod
    def get_or_create_spark_session(
            spark_config  #: Optional[SparkConfig] = None,
    ) -> SparkSession:
        """Obtains Spark session if it already exists; otherwise creates Spark session and returns it to caller.

        Args:
            spark_config: Dictionary containing Spark configuration (string-valued keys mapped to string-valued properties).

        Returns:
            SparkSession
        """
        spark_config = spark_config or {}

        spark_session: SparkSession
        """
        try:
            spark_session = pyspark.SparkConnectSession.builder.getOrCreate()
        except (ModuleNotFoundError, ValueError):
            spark_session = SparkSession.builder.getOrCreate()
        """
        spark_session = SparkSession.builder.getOrCreate()
        return spark_session

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
        if isinstance(self.data_connector, FileSystemConnector):
            return self.spark\
                .read.csv(path=csv_file_path, header=header, inferSchema=infer_schema, sep=separator)

    def read_parquet(self):
        pass

    def read_from_jdbc(self):
        pass
