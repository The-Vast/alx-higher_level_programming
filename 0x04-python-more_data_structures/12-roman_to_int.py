#!/usr/bin/python3
def roman_to_int(roman_string):
    """that converts a Roman numeral to an integer."""
    if isinstance(roman_string, str) and roman_string != None:
        main = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = main[roman_string[0]]
        if len(roman_string) == 1:
            return integer
        for i in range(1, len(roman_string)):
            if main[roman_string[i]] > main[roman_string[i-1]]:
                integer = main[roman_string[i]] - integer
            else:
                integer += main[roman_string[i]]
        return integer
    return 0
