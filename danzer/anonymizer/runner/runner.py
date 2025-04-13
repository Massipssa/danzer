from danzer.anonymizer.core.anonymization.column_suppression import ColumnSuppression
from danzer.anonymizer.core.engine.execution_engine import ExecutionEngine, EngineType
from danzer.anonymizer.core.engine.spark_engine import SparkExecutionEngine
from danzer.anonymizer.datasource.connector.file_system_connector import FileSystemConnector
from danzer.build.lib.danzer_anonymizer.util.json_util import read_json_file

import logging

logger = logging.getLogger(__name__)


class Runner:

    def __init__(self, execution_engine: ExecutionEngine):
        self.execution_engine = execution_engine


def run():
    config_path = "../../../examples/config/fs_column_suppression.json"
    data_path = "../../../examples/data/"

    # 1- create connector
    fs_data_connector = FileSystemConnector(
        name="test",
        datasource_name="testdatasource",
        file_regex=".*csv",
        base_directory=data_path
    )

    execution_engine = SparkExecutionEngine(data_connector=fs_data_connector)

    df = execution_engine.read_csv(
        csv_file_path=f"{fs_data_connector.base_directory}/flies.csv",
        separator=","
    )
    df.printSchema()

    # init the algo
    json_data = read_json_file(config_path)

    column_suppression = ColumnSuppression(
        params=json_data,
        df=df,
        engine_type=EngineType.SPARK
    )

    df = column_suppression.operate()
    df.printSchema()

    # suppression_df = column_suppression.operate()
    # logger.info(suppression_df.columns)

    """
    # read the dataset based on the requirement
    import pandas as pd
    df = pd.read_csv(f"{data_connector.base_directory}/flies.csv")
    logger.info(df.columns)

    
    """
