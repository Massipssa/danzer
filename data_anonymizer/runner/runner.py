import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action",
                        choices=["anonymization", "p-anonymizatoin"],
                        help="Action to perform: anonymization or pseudo-anonymizatoin",
                        required=True
                        )
    parser.add_argument("-d", "--datasource", help="Json to datasource definition")
    parser.add_argument("-v", "--verbosity", help="Verbosity", action="store_false")


def get_action_type(action_name: str):
    if action_name in ("anonymization", "p-anonymizatoin"):
        return action_name
    raise ValueError("Invalid argument is provided for action to perform")


def run():
    pass


if __name__ == '__main__':
    run()
