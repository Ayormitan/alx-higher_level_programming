#!/usr/bin/python3
def text_indentation(text):
    """
    Function will print a textn with two line after encountering some char
    args:
        test: character to test
    """
    char_to_check = ['.', '?', ':']
    for char in text:
        print(char, end="")
        if char in char_to_check:
            print("\n" * 2, end="")
    print()
    if not isinstance(text, string):
        raise TypeError("textmust be a string")
