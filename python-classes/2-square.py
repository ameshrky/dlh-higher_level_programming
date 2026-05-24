#!/usr/bin/python3
"""This module shows an example for how to create a class."""


class Square:
    """This class describes the blueprint of a square."""

    def __init__(self, size=0):
        """Initialize a square with a size. size here is a private field."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
