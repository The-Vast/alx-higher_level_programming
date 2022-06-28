#!/usr/bin/python3
# 3-say_my_name.py


"""Say my name"""



def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>

    args:
        first_name and last_name must be strings
        otherwise, raise a TypeError

    raise:
        TypeError("first_name must be a string")
        TypeError("last_name must be a string")
    
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must")
    if not isinstance(last_name, str)
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
