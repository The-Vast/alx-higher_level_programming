#!/usr/python3

"""Square #1"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size):
        """instantiation of Square

        Args:
            size (int): size of the square side
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
