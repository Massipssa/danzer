import logging
from typing import Optional

import pandas as pd

from danzer.anonymizer.core.engine.execution_engine import ExecutionEngine
from danzer.anonymizer.dataset.dataset import Dataset
from danzer.anonymizer.datasource.connector.data_connector import DataConnector
from danzer.anonymizer.datasource.connector.file_system_connector import FileSystemConnector

logger = logging.getLogger(__name__)


class PandasDataframe(Dataset):
    def __init__(self,
                 name: str,
                 data_connector: DataConnector,
                 execution_engine: ExecutionEngine
                 ):
        super().__init__(name, data_connector, execution_engine)

    def read_csv(self) -> Optional[pd.DataFrame]:
        if isinstance(self.data_connector, FileSystemConnector):
            logger.info("Read pandas dataframe from file system")
            return pd.read_csv(self.data_connector.base_directory)
