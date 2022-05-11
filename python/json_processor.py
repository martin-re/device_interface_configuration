import json

'''This module is helper for main.py.
The module contains some primitive functions for common json operations.'''


def deserialize(filename):
    with open(filename) as f:
        return json.load(f)


def pretty_print(data):
    print(json.dumps(data, sort_keys=False, indent=4))


def access_node(root, path):
    for node in path:
        root = root[node]
    return root
