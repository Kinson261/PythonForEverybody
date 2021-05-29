"""
Shakespeare used over 20,000 words in his works. But how would you
determine that? How would you produce the list of all the words that
Shakespeare used? Would you download all his work, read it and track
all unique words by hand?

Let’s use Python to achieve that instead. List all unique words, sorted
in alphabetical order, that are stored in a file romeo.txt containing a
subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
Create a list of unique words, which will contain the final result. Write
a program to open the file romeo.txt and read it line by line. For each
line, split the line into a list of words using the split function. For
each word, check to see if the word is already in the list of unique
words. If the word is not in the list of unique words, add it to the list.
When the program completes, sort and print the list of unique words
in alphabetical order.

    Enter file: romeo.txt
    ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
    'and', 'breaks', 'east', 'envious', 'fair', 'grief',
    'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
    'sun', 'the', 'through', 'what', 'window',
    'with', 'yonder']
"""

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print('File does not exist: ', fname)
    print('Program will exit')
    exit()

words_list = []                         #create an empty list
for line in fhand:                      #reading each line
    line.rstrip()                       #del whitespace at the end of the line
    words = line.split()                #list of each word inside the line
    for item in words:
        if item in words_list:          #checking if word is already in the list
            continue                    #skip
        else:
            words_list.append(item)     #add new word to the list

words_list.sort()                       #sort the list od unique words
print(words_list)                       #output