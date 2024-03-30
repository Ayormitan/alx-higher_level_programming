#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL> using requests method
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    print(request.headers.get("X-Request-Id"))