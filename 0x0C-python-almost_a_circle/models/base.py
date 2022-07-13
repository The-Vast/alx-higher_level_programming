#!/usr/bin/python3
"""Base class"""


class Base:
    """defines base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiation of base object

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
