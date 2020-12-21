#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)
elif len(sys.argv) == 3:
    try:
        f = open(sys.argv[2], "r")
    except FileNotFoundError:
        print("Missing <filename>")
        exit(1)
exit(0)