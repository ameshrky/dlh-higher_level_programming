#!/usr/bin/python3
"""Returns the JSON representation of an object as a string."""


import json


def to_json_string(my_obj):
    """Convert an object to a JSON string."""
    return json.dumps(my_obj)
