#!/usr/bin/python3
"""This module is to read a file."""


def write_file(filename="", text=""):
    """Write a UTF8 text to file and returns number of characters."""
    with open(filename, mode='w', encoding="utf-8") as myFile:
        return myFile.write(text)
