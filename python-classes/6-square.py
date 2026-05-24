#!/usr/bin/python3
"""This module shows an example for how to create a class."""


class Square:
    """This class describes the blueprint of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a size. size here is a private field."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

    @property
    def position(self):
        """retriever the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square."""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = (value[0], value[1])

    def area(self):
        """This function returns the area of a square."""

        return self.__size ** 2

    def my_print(self):
        """This method print ### as many times as the size of the square"""

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
