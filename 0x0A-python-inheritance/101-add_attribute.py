#!/usr/bin/python3

"""Access the possibility of adding a new attribute
    to an object
"""


def add_attribute(objt, attr, value):
    """Add a new attribute to an object if possible.
    Args:
        objt (any): The object to add an attribute to.
        attr (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(objt, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objt, attr, value)
