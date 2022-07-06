#!/usr/bin/python3

"""Exact same object"""


def is_same_class(obj, a_class):
    """
    Verifies if the object is exactly an instance of the specified class

    Args:
        obj (any): object to be checked
        a_class (type): class to be matched as the object type

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
