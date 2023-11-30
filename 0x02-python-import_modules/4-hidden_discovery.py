#!/usr/bin/python3
if __name__ == "__main__":
    from importlib import import_module

    dlib = import_module('hidden_4')
    for i in list(m for m in dir(dlib) if m[:2] != "__"):
        print(i)
