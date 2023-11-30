#!/usr/bin/python3
from sys import argv
def prints_args():
    argument_no = len(argv) - 1

    print(f"{argument_no} argument", end='')
    if argument_no == 0:
        print(".")
    elif argument_no == 1:
        print(":")
    else:
        print("s:")
    for i, arg in enumerate(argv[1:], start=1):
        print(f"{i}: {arg}")
if __name__ == "__main__":
    prints_args()
