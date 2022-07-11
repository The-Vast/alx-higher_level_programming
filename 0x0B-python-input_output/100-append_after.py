#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string.

    Args:
        filname (str): name of the file
        search_string (str): string to search for
        new_string (str): text to be inserted
    """
    replacement = ""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            replacement += line
            if search_string in line:
                replacement += new_string
    with open(filename, 'w') as w:
        w.write(replacement)
