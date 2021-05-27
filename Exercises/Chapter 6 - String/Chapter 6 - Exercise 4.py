"""
Exercise 4: There is a string method called count that is similar to
the function in the previous exercise. Read the documentation of this
method at:
https://docs.python.org/library/stdtypes.html#string-methods

Write an invocation that counts the number of times the letter a occurs
in “banana”.
"""

word = 'banana'
for char in word:
    counter = word.count('a')
print('There are ', counter, ' "a" in the word ', word)
