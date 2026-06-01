#!/usr/bin/env python3
"""Test task 2: CSV to JSON conversion."""

from task_02_csv import convert_csv_to_json

result = convert_csv_to_json("sample_data.csv")
print(f"Conversion successful: {result}")

if result:
    with open("data.json", "r", encoding="utf-8") as file:
        print(file.read())
