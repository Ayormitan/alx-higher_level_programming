#!/usr/bin/python3
""" 1-main.py"""
from models.rectangle import Rectangle

if __name__ == "__manin__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
