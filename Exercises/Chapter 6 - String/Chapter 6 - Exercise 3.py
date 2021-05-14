"""
    Exercise 3: Encapsulate this code in a function named count, and gen-
    eralize it so that it accepts the string and the letter as arguments.

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
        count = count + 1
    print(count)
"""

def count(inp, word):
    counter = 0
    for letter in word:
        if letter == inp:
            counter = counter + 1
    return counter


inp = input('Count: ')

if len(inp)>1:              #we can compare only one letter at a time
    print('Please enter only a letter in count')
    inp = input('Count: ')

else:
    word = input('Word: ')
    print("Program is going to count '", inp, "' in '", word,"'")

    x = count(inp, word)
    print('\nCounter =', x)