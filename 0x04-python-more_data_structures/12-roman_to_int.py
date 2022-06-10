#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        main = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = main[roman_string[-1]]
        if len(roman_string) == 1:
            return integer
        for i in range(len(roman_string) - 1, 0, -1):
            if main[roman_string[i]] > main[roman_string[i-1]]:
                integer -= main[roman_string[i-1]]
            else:
                integer += main[roman_string[i-1]]
        return integer
    return (0)
