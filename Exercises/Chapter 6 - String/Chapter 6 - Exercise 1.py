"""
    Exercise 1:
    Write a while loop that starts at the last character in the
    string and works its way backwards to the first character in the string,
    printing each letter on a separate line, except backwards.

"""


word = input('Enter a word: ')
index = len(word)-1                 #index starts from 0 whereas len() start from 1
while index >= 0:
    letter = word[index]
    index = index - 1
    print(letter)
