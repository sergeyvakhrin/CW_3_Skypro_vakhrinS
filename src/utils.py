import json


def load_data(path):
    with open(path, "rt", encoding="UTF-8") as file:
        return json.load(file)

