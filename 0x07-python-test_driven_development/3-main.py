#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("john", "smith")
say_my_name("walter", "white")
try:
    say_my_name(12, "white")
except Exception as e:
    print(e)
