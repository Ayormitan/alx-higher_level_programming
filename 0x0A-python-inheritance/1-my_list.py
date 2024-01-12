#!/usr/bin/python3
class Mylist(list):
    def print_sorted(self):
        sort_list = sorted(self)
        print(sort_list)
