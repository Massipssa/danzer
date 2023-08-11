import argparse

from data_anonymizer.config.column_suppression_config import load_column_suppression
from data_anonymizer.core.anonymization.numerical.numerical_perturbation import NumericalPerturbation
from data_anonymizer.datasource.connector.file_system_connector import FileSystemConnector


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
    # 1- create connector
    data_connector = FileSystemConnector(
        name="test",
        datasource_name="testdatasource",
        file_regex=".*csv",
        base_directory="../../examples/data"
    )

    # read the dataset based on the requirement
    import pandas as pd
    df = pd.read_csv(f"{data_connector.base_directory}/flies.csv")
    print(df.columns)

    # init the algo
    column_suppression = load_column_suppression("../../examples/anonymization/column-suppression/fs_column_suppression.json")
    column_suppression._df = df

    suppression_df = column_suppression.anonymize()
    print(suppression_df.columns)

    numerical_perturbation = NumericalPerturbation(
        algorithm_name="Suppression",
        columns_to_anonymize=["dockcount"],
        df=df,
        std=10
    )

    numerical_perturbation_df = numerical_perturbation.anonymize()
    print(numerical_perturbation_df.columns)
    print(numerical_perturbation_df["dockcount"])

if __name__ == '__main__':
    run()
