#!/usr/bin/python3
def no_c(my_string):
    mynew_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            mynew_string += char
    return (mynew_string);
