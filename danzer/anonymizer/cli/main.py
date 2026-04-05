import logging

from danzer.anonymizer.api import AnonymizationService
from danzer.anonymizer.cli.args import parse_args
from danzer.anonymizer.infrastructure.readers import load_job_config_from_json

logger = logging.getLogger(__name__)


def main() -> None:
    args = parse_args()
    if args.action != "anonymize":
        raise ValueError("Only 'anonymize' is supported by the new CLI flow for now.")

    config = load_job_config_from_json(args.datasource)
    service = AnonymizationService()
    service.run(config)
    logger.info("Anonymization job completed.")
