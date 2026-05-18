#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
        
    roman_int_map = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    roman_int = 0
    i = len(roman_string) - 1
    while i >= 0:
        if roman_string[i] == 'X':
            if i > 0 and roman_string[i-1] == 'I':
                roman_int += roman_int_map.get('IX')
                i -= 2
                continue
        if roman_string[i] == 'L':
            if i > 0 and roman_string[i-1] == 'X':
                roman_int += roman_int_map.get('XL')
                i -= 2
                continue
        if roman_string[i] == 'C':
            if i > 0 and roman_string[i-1] == 'X':
                roman_int += roman_int_map.get('XC')
                i -= 2
                continue
        if roman_string[i] == 'D':
            if i > 0 and roman_string[i-1] == 'C':
                roman_int += roman_int_map.get('CD')
                i -= 2
                continue
        if roman_string[i] == 'M':
            if i > 0 and roman_string[i-1] == 'C':
                roman_int += roman_int_map.get('CM')
                i -= 2
                continue
        roman_int += roman_int_map.get(roman_string[i])
        i -= 1
    return roman_int
