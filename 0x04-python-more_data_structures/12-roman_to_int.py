#!/usr/bin/python3
"""
Return value of char
"""


def roman_value(char):
    match char:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
        case '_':
            return -1


"""
convert roman to int
"""


def roman_to_int(roman_string):
    if (not roman_string) or \
            type(roman_string) != str:
        return None
    number = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            if roman_value(roman_string[i]) \
                    >= roman_value(roman_string[i + 1]):
                number += roman_value(roman_string[i])
            else:
                number -= roman_value(roman_string[i])
        else:
            number += roman_value(roman_string[i])
    return number
