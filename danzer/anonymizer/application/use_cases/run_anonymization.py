from danzer.anonymizer.application.dto.config import AnonymizationJobConfig
from danzer.anonymizer.application.validators.config_validator import validate_job_config
from danzer.anonymizer.domain.models.job import AnonymizationJob
from danzer.anonymizer.domain.rules.suppression import ColumnSuppressionRule
from danzer.anonymizer.infrastructure.connectors.filesystem import LocalFileSource
from danzer.anonymizer.infrastructure.engines.factory import build_execution_engine


class RunAnonymizationUseCase:
    """Application orchestration for one anonymization job."""

    def execute(self, config: AnonymizationJobConfig):
        validate_job_config(config)

        job = AnonymizationJob(
            source=LocalFileSource(config.source_path),
            rule=ColumnSuppressionRule(columns=config.rule_params.get("columns_to_delete", [])),
            engine_name=config.engine,
            output_path=config.output_path,
        )

        engine = build_execution_engine(job.engine_name)
        dataset = engine.read(job.source)
        result = engine.apply_rule(dataset, job.rule)
        if job.output_path:
            engine.write(result, job.output_path)
        return result
