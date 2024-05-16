import json


def read_json_data(path: str) -> dict:
    with open(path, '+r') as file:
        return json.load(file)

read_json_data("C:/Users/alber/OneDrive/Documents/GitHub/HoopsML/scripts/data/saved_data.json")