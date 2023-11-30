#!/usr/bin/python3
import sys
def add_func(args):
    try:
        result = sum(map(int, args))
        print(result)
    except ValueError:
        print("Error")
if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        add_func(args)
    else:
        print("0")
