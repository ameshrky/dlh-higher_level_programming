#!/usr/bin/env python3
"""Test task 3: XML serialization and deserialization."""

from task_03_xml import deserialize_from_xml, serialize_to_xml

data = {
    "name": "Maria",
    "age": 28,
    "city": "Lisbon",
    "occupation": "Software Engineer",
}

serialize_to_xml(data, "data.xml")
loaded_data = deserialize_from_xml("data.xml")

print(loaded_data)
