#!/usr/bin/env python3
"""Test task 1: pickling custom classes."""

from task_01_pickle import CustomObject

obj = CustomObject("John", 25, True)
obj.serialize("object.pkl")

loaded_obj = CustomObject.deserialize("object.pkl")

if loaded_obj is not None:
    loaded_obj.display()
else:
    print("Deserialization failed.")
