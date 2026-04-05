from danzer.anonymizer.application.dto.config import AnonymizationJobConfig
from danzer.anonymizer.application.use_cases.run_anonymization import RunAnonymizationUseCase


class AnonymizationService:
    """Thin facade used by CLI or external callers."""

    def __init__(self, use_case: RunAnonymizationUseCase | None = None) -> None:
        self._use_case = use_case or RunAnonymizationUseCase()

    def run(self, config: AnonymizationJobConfig):
        return self._use_case.execute(config)
