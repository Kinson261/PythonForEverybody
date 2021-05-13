"""
Exercise 3

 Write a program to prompt the user for hours and rate per
 hour to compute gross pay.
 Enter Hours: 35
 Enter Rate: 2.75
 Pay: 96.25
"""

print('\n\n________________________________________')
print('Exercise 3')
hours = int(input('Enter hours: \t'))
rate = float(input('Enter rate: \t'))

pay = hours * rate;
print('Pay: \t', pay, ' $')

input()