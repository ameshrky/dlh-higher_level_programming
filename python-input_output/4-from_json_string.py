#!/usr/bin/python3
"""Returns the JSON representation of an object as a string."""


import json


def from_json_string(my_str):
    """Convert an object to a JSON string."""
    return json.loads(my_str)
