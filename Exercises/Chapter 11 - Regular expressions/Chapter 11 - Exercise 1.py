"""
Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^Xmbox.
txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
"""

import re

fname = input('Enter file name: ')
# fname = 'mbox.txt'
try:
    fhand = open(fname)
except:
    print('File is missing: ', fname)
    print('Programm will now exit.')
    exit()


def searching():
    counter = int()
    expr = input('Enter a regular expression: ')
    for line in fhand:
        line = line.rstrip()
        if re.findall(expr, line):
            counter += 1
        else:
            continue
    print(fname, ' had ', counter, ' lines that matched ', expr)


searching()
