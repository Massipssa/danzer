import json


def read_json_file(file_path: str):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)
