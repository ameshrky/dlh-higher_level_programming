#!/usr/bin/python3
"""Student class with reload from JSON."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, optionally filtered by attrs."""
        if isinstance(attrs, list):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of Student from json dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
