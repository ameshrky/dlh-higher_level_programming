#!/usr/bin/python3
"""This module is to read a file"""


def read_file(filename=""):
    """Reads a UTF8 text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as myFile:
        x = myFile.read()
        print(x, end="")
