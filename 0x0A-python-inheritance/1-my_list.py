#!/usr/bin/python3
"""Define inherited list"""
class Mylist(list):
    """ Print sorted list for already built in list"""
    def print_sorted(self):
        print(sorted(self))
