"""
    Exercise 2:
    Write another program that prompts for a list of numbers
    as above and at the end prints out both the maximum and minimum of
    the numbers instead of the average.

"""


def great_func(my_list):
    biggest = None
    for value in my_list:
        if biggest is None or biggest < value:
            biggest = value
    return biggest


def small_func(my_list):
    smallest = None
    for value in my_list:
        if smallest is None or smallest > value:
            smallest = value
    return smallest


values = []
while True:
    inp = input('Enter a number: ')

    try:
        value = float(inp)
        values.append(value)

    except:
        if inp == 'done':
            break
        else:
            print('Invalid input')
            continue

maximum = great_func(values)
print('\nBiggest number: ', maximum)
minimum = small_func(values)
print('Smallest number: ', minimum)
