#!/usr/bin/python3

"""Defines a square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of side of the square.
        """
        self.__size = size

    @property
    def size(self):
        "Properties for the length of a size of a square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square.

        Returns:
            the area of the square.
        """
        return self.__size ** 2
