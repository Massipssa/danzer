import argparse


VALID_ACTIONS = ["anonymize", "deanonymize"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run anonymization or de-anonymization on a given data source definition."
    )
    parser.add_argument("-d", "--datasource", required=True, help="Path to a job configuration JSON file.")
    parser.add_argument("-a", "--action", choices=VALID_ACTIONS, required=True)
    parser.add_argument("-v", "--verbosity", action="store_true", help="Enable verbose logging.")
    return parser.parse_args()
