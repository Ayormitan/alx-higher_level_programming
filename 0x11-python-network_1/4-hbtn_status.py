#!/usr/bin/python3
""" Fecthes url using requst module"""
import requests
if __name__ == "__main__":
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
