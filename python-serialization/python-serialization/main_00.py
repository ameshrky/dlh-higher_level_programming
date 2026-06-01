#!/usr/bin/env python3
"""Test task 0: basic serialization."""

from task_00_basic_serialization import (
    load_and_deserialize,
    serialize_and_save_to_file,
)

data = {
    "name": "Alice",
    "age": 30,
    "city": "Paris",
    "skills": ["Python", "JSON", "Serialization"],
}

serialize_and_save_to_file(data, "data.json")
loaded_data = load_and_deserialize("data.json")

print(loaded_data)
