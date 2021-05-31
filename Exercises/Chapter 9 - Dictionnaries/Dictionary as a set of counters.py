"""
Create a program, capable of counting how many times each letter
is repeated thorough a text document
"""
import string

fname = input('Enter file name: ')
#fname = 'words.txt'

try:
    fhand = open(fname)
except:
    print('File is missing: ', fname, '\nProgram will exit')
    exit()

letter = {}                     #counts words
mots = {}                       #counts words

for line in fhand:
    line.rstrip()                                   #del whitespace
    line.translate(line.maketrans('','', string.punctuation))
    word_list = line.lower().split()                        #separating each word
    for word in word_list:                          #picking word from the list
        mots[word]= mots.get(word, 0) + 1
        for char in word:
            letter[char] = letter.get(char, 0) + 1   #checking if the char exists
                                                     #if it doesn't, assign the value 0 to it
                                                     #otherwise increment it

print(mots)
print('\n', letter)


