#!/usr/bin/python3
# 4-print_square.py


"""Print square"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): length of the square

    raises;
        TypeError("size must be an integer")
        ValueError("size must be >= 0")

    """

    if not (isinstance(size, int) or (isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
