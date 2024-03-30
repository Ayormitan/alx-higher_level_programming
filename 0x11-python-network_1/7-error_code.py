#!/usr/bin/python3
""" Sends a url and display response """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
