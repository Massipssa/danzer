from danzer_anonymizer.anonymizer.core.action import Action
from danzer_anonymizer.anonymizer.core.engine.execution_engine import ExecutionEngine
from danzer_anonymizer.anonymizer.datasource.datasource import Datasource


class AnonymizerConfig:

    def __init__(self,
                 name: str,
                 action: Action,
                 data_source: Datasource,
                 execution_engine: ExecutionEngine):
        self.name = name
        self.action = action
        self.data_source = data_source
        self.execution_engine = execution_engine
