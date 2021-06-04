"""
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

# Library
import string

import matplotlib.pyplot as plt

# fname = input('Enter file name: ')
fname = 'mbox.txt'
fhand = open(fname)

# global variable
alphabet = list()


# processing text
def printing():
    counter = dict()
    for line in fhand:
        line = line.rstrip()  # removing whitespace
        line = line.translate(line.maketrans('', '', string.punctuation))  # removing punctuations
        line = line.translate(line.maketrans('', '', string.digits))  # removing digits
        words = list(line.lower().split())  # each word in lower case
        for word in words:
            for char in word:
                if char in counter:
                    counter[char] += 1  # incrementing if exists
                else:
                    counter[char] = 1  # adding if not
    print(counter)
    for (char, val) in list(counter.items()):
        alphabet.append((val, char))
    alphabet.sort(reverse=True)
    print('\n\n', alphabet)

    return alphabet


# Visualizing result with a frequency plot

def histos(MyList):
    letter = []  # list of letters
    frequency = []  # list of value

    for i in range(len(MyList)):
        frequency.append(MyList[i][0])
        letter.append(MyList[i][1])

    plt.bar(letter, frequency)
    plt.show()


printing()
histos(alphabet)

#todo make a percentage plot
