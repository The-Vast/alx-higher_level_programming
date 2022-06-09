#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    max_score = 0
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
    return max_score
