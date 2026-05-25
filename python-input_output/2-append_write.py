#!/usr/bin/python3
"""This module is to read a file."""


def append_write(filename="", text=""):
    """Append a UTF8 text to file and returns number of characters."""
    with open(filename, mode='a', encoding="utf-8") as myFile:
        return myFile.write(text)
