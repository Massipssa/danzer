from danzer.anonymizer.core.anonymization.column_suppression import ColumnSuppression
from danzer.anonymizer.core.engine.execution_engine import EngineType
from danzer.anonymizer.core.engine.spark_engine import SparkExecutionEngine
from danzer.anonymizer.datasource.connector.file_system_connector import FileSystemConnector
from danzer.anonymizer.runner.args_parser import parse_args
from danzer.anonymizer.util.json_util import read_json_file

import json
import logging

logger = logging.getLogger(__name__)


class Runner:

    def __init__(self, execution_engine):
        self.execution_engine = execution_engine


def run() -> None:
    args = parse_args()

    with open(args.datasource, "r", encoding="utf-8") as f:
        config = json.load(f)

    fs_data_connector = FileSystemConnector(**config)
    execution_engine = SparkExecutionEngine(data_connector=fs_data_connector)

    df = execution_engine.read_csv(
        csv_file_path=f"{fs_data_connector.base_directory}/{fs_data_connector.file_regex}",
        separator=","
    )

    config_path = "../../../examples/config/json/fs_column_suppression.json"
    json_data = read_json_file(config_path)

    column_suppression = ColumnSuppression(
        params=json_data,
        df=df,
        engine_type=EngineType.SPARK
    )

    result_df = column_suppression.operate()
    result_df.printSchema()
