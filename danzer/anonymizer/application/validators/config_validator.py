from danzer.anonymizer.application.dto.config import AnonymizationJobConfig


SUPPORTED_RULES = {"column_suppression"}
SUPPORTED_ENGINES = {"spark", "local"}


def validate_job_config(config: AnonymizationJobConfig) -> None:
    if not config.source_path:
        raise ValueError("source_path must not be empty.")
    if config.rule_name not in SUPPORTED_RULES:
        raise ValueError(f"Unsupported rule_name: {config.rule_name}.")
    if config.engine not in SUPPORTED_ENGINES:
        raise ValueError(f"Unsupported engine: {config.engine}.")
