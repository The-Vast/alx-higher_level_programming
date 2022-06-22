#!/usr/bin/python3
"""class Square that defines a square by:.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    You are not allowed to import any module.
"""


class Square:
    """This is the Square."""

    def __init__(self, size):
        """Initialize the square
        Args:                                                                                                                                                size (int): The size of a square.                                                                                                      
        """
        self.__size = size
