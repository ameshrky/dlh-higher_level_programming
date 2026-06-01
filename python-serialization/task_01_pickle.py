#!/usr/bin/env python3
"""Pickling and unpickling a custom class."""

import pickle


class CustomObject:
    """Represent a custom object that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object to filename."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None
        return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from filename."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError, EOFError):
            return None
