#!/usr/bin/python3

"""Write to a file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (): file name
        text (str): text to be written
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
