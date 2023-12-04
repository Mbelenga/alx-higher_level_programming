#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    max_integer = my_list[0]
    for char in my_list:
        if char > max_integer:
            max_integer = char
    return max_interger
