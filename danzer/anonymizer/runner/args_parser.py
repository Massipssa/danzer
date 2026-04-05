import argparse
from argparse import Namespace

VALID_ACTIONS = ["anonymize", "deanonymize"]


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser(
        description="Run anonymization or de-anonymization on a given data source definition."
    )

    parser.add_argument(
        "-d",
        "--datasource",
        required=True,
        help="Path to JSON or YAML file containing the data source definition."
    )

    parser.add_argument(
        "-a",
        "--action",
        choices=VALID_ACTIONS,
        help="Action to perform: 'anonymize' or 'deanonymize'.",
        required=True
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        help="Enable verbose logging output.",
        action="store_false",
        required=False
    )
    return parser.parse_args()


def get_action_type(action_name: str) -> str:
    action_name = action_name.lower().strip()
    if action_name in VALID_ACTIONS:
        return action_name
    raise ValueError(f"Invalid action '{action_name}'. Valid options are: {', '.join(VALID_ACTIONS)}")
