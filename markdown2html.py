#!/usr/bin/python3
"""markdown2html"""
import sys


if len(sys.argv) != 3:
    print('Usage: ./markdown2html.py README.md README.html' ,file=sys.stderr)
    exit(1)
else:
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError:
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
exit(0)
