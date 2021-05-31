"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
"""
import random

fname = 'words.txt'                                     #file name
fhand = open(fname)                                     #file handler

words = {}                                              #empty dictionary


def create_dictionary():
    for line in fhand:
        line.rstrip()                                   #del whitespace at the end of line
        list_words = line.split()                       #list of words on line
        for word in range(len(list_words)):
            key = list_words.pop()                      #picking word starting from the end of the list
            words[key] = random.random()                #assigning random value to key
    return words


create_dictionary()                                     #execute function

inp = input('Enter a word to search: ')

if inp in words:                                        #search word in dictionary
    print("'", inp, "'", ' is in the dictionary.')
else:
    print("'", inp, "'", 'is not in th dictionary')
