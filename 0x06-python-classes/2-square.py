#!/usr/bin/python3

"""class Square that defines a square by:
    Private instance attribute: size.
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception.
"""


class Square:
    """Body of the square"""
    def __init__(self, size=0):
        """Initialize square.

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
