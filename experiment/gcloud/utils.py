import json


def pretty_json(val, indent=True):
    return json.dumps(val, indent=(2 if indent else 0))


def print_json(val):
    print(pretty_json(val))
