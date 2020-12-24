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
    if tag == '-':
        ul = "<ul>"
        for i in strzero:
            a = i.split(" ")
            a = a[1:]
            ul = ul + '\n' + '<li>' + ' '.join(a) + '</li>'
        ul = ul + "\n</ul>"
        return ul

    if tag == '*':
        ul = "<ol>"
        for i in strzero:
            a = i.split(" ")
            a = a[1:]
            ul = ul + '\n' + '<li>' + ' '.join(a) + '</li>'
        ul = ul + "\n</ol>"
        return ul

    array = strzero.split(' ')
    if tag == "#":
        mystr = " ".join(array[1:])
        return "<h{}>{}</h{}>".format(len(array[0]), mystr, len(array[0]))
    else:
        pass


if __name__ == "__main__":
    """markdown2html"""
    respr = ""
    writingaray = []
    myarr = []
    y = {}
    arrul = []
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)
    else:
        i = 0
        try:
            with open(sys.argv[1], "r") as file:
                f = str(file.read())
            try:
                os.remove(sys.argv[2])
            except BaseException:
                pass
            data = f.split('\n')
            while i < len(data):
                if '#' in data[i]:
                    respr = respr + representation(data[i], '#')
                    respr = respr + '\n'
                elif '-' in data[i]:
                    j = i
                    while j < len(data) and '-' in data[j]:
                        arrul.append(data[j])
                        j += 1
                    respr = respr + representation(arrul, '-')
                    arrul = []
                    if j != len(data) - 1:
                        respr += '\n'
                    i = j
                elif '*' in data[i]:
                    j = i
                    while j < len(data) and '*' in data[j]:
                        arrul.append(data[j])
                        j += 1
                    respr = respr + representation(arrul, '*')
                    arrul = []
                    if j != len(data) - 1:
                        respr += '\n'
                    i = j
                i += 1
            writer(respr, sys.argv[2])
        except FileNotFoundError:
            print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
            exit(1)
    exit(0)
