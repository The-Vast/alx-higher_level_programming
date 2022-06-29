#!/bin/usr/python3

"""Real definition of a rectangle"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width, height):
        """instantiation of new Rectangle

        Args:
            width (int): how wide the new rectangle is
            height: how long the nedw rectangle is
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """get width of rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """set with of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """set height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
