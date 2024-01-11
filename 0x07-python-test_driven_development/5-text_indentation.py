#!/usr/bin/python3
def text_indentation(text):
    """
    Function will print a textn with two line after encountering some char
    args:
        test: character to test
    """
    if not isinstance(text, str):
        raise TypeError("textmust be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
