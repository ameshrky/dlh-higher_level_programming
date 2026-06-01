#!/usr/bin/python3
"""Return dictionary description of an object."""


def class_to_json(obj):
    """Return the dictionary description with simple data structures."""
    return obj.__dict__
