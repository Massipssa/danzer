from danzer.anonymizer.application.dto.config import AnonymizationJobConfig
from danzer.anonymizer.util.json_util import load_config_from_json


def load_job_config_from_json(file_path: str) -> AnonymizationJobConfig:
    raw = load_config_from_json(file_path)
    operation = raw.get("operation", {})
    data_source = raw.get("data_source", {})
    execution_engine = raw.get("execution_engine", {})

    return AnonymizationJobConfig(
        source_path=data_source.get("path") or data_source.get("base_directory") or "",
        rule_name=operation.get("algorithm_name", "column_suppression"),
        rule_params={
            "columns_to_delete": operation.get("columns") or operation.get("columns_to_delete") or []
        },
        engine=execution_engine.get("name", "spark").lower(),
    )
