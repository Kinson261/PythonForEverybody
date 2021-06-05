"""
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Enter file:mbox.txt
39594

Enter file:mbox-short.txt
39756
"""

import re

import numpy as np

fname = input("Enter file name: ")
# fname = 'mbox.txt'
try:
    fhand = open(fname)
except:
    print("File is missing: ", fname)
    print("Programm will now exit.")
    exit()

Y = list()



def searching():
    for line in fhand:
        line = line.rstrip()
        X = re.findall('New\sRevision:\s([0-9.]+)', line)                   #finding pattern and extracting number
        if len(X) > 0:
            Y.append(X)                                                     #adding it to a list
        else:
            continue

    return Y


def computing(listoflist):
    myArray = np.hstack(listoflist)                                         #concatenation of the list of lists
    myArray = list(map(int, myArray))                                       #converting string to int in array
    # print(myArray)
    mean = sum(myArray) / len(myArray)                                      #computing mean
    print("The average of number is: ", int(mean))                          #output


searching()
computing(Y)

