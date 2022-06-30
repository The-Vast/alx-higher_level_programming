#!/usr/bin/python3
"""How many instances"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instantiation of new Rectangle

        Args:
            width (int): how wide the new rectangle is
            height: how long the nedw rectangle is
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set with of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
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

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return string representation of the Rectangle

        Represents rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                shape.append('\n')

        return ("".join(shape))

    def __repr__(self):
        """return a string representation of the rectangle"""
        op = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return (op)

    def __del__(self):
        """message to be printed when an instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
