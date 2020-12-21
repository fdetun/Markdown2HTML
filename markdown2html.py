#!/usr/bin/python3
"""markdown2html"""
import sys
import os


def writer(code, file):
    """writer function"""
    f = open(file, "a+")
    f.write(code)


def representation(strzero, tag):
    """repr function"""
    ul = "<ul>"
    if type(strzero) == list:
        for i in strzero:
            a = i.split(" ")
            a = a[1:]
            ul = ul + '\n' + '<li>' + ' '.join(a) + '</li>'
        ul = ul + "\n</ul>"
        return ul

    array = strzero.split(' ')
    if tag == "#":
        mystr = " ".join(array[1:])
        return "<h{}>{}</h{}>".format(len(array[0]), mystr, len(array[0]))
    else:
        pass


if __name__ == "__main__":
    """markdown2html"""

    arrul = []
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)
    else:
        try:
            with open(sys.argv[1], "r") as file:
                f = str(file.read())
            try:
                os.remove(sys.argv[2])
            except BaseException:
                pass
            data = f.split('\n')
            for k, i in enumerate(data):
                if "#" in i:
                    codeline = representation(i, "#")
                    if k == len(data) - 1:
                        writer(codeline, sys.argv[2])
                    else:
                        writer(codeline + '\n', sys.argv[2])
                elif "-" in i:
                    arrul.append(i)
            if arrul != []:
                codeline = representation(arrul, "-")
                writer(codeline, sys.argv[2])
        except FileNotFoundError:
            print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
            exit(1)
    exit(0)
