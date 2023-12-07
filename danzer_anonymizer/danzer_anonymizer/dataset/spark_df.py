from danzer_anonymizer.danzer_anonymizer.dataset.dataset import Dataset
from danzer_anonymizer.danzer_anonymizer.dataset.util import get_or_create_spark_session
from danzer_anonymizer.danzer_anonymizer.datasource.connector.data_connector import DataConnector
from pyspark.sql import DataFrame


class SparkDataframe(Dataset):

    def __init__(self,
                 data_connector: DataConnector,
                 spark_config=None
                 ) -> None:
        self.data_connector = data_connector
        if spark_config is None:
            spark_config = {}

        spark = get_or_create_spark_session(spark_config)
        self.spark = spark

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
   