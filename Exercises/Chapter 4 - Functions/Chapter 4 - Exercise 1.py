import random

"""
Exercise 1

    Run the program on your system and see what numbers
    you get. Run the program more than once and see what numbers you
    get.

"""

print('\nThe function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0)')
print('Each time you call random, you get the next number in a long series.\n')
for i in range(10):
    x = random.random()
    print(x)

print('\n\n________________________________________')
print(
    '\nThe function randint takes the parameters low and high, and returns an integer between low and high (including both).\n')

for i in range(5):
    x = random.randint(5, 10)
    print(x)

print('\n\n________________________________________')
print('To choose an element from a sequence at random, you can use choice:')

t = [1, 2, 3]
for i in range(5):
    x = random.choice(t)
    print(x)