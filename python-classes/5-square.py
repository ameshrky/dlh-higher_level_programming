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

    @property
    def size(self):
        """retriever the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """This function returns the area of a square."""

        return self.__size ** 2

    def my_print(self):
        """This method print ### as many times as the size of the square"""

        for i in range(self.__size):
            print("#" * self.__size)
