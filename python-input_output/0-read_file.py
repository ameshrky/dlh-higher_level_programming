#!/usr/bin/python3
"""This module is to read a file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as myFile:
        x = myFile.read()
        print(x)
