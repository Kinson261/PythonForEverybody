"""
Exercise 1

    Rewrite your pay computation to give the employee 1.5
    times the hourly rate for hours worked above 40 hours.
    Enter Hours: 45
    Enter Rate: 10
    Pay: 475.0
"""
print('\n\n________________________________________')
print('Exercise 1')

hours = float(input('Enter hours: \t'))
rate = float(input('Enter rate: \t'))

if hours > 40:
    pay = (rate * 40) + ((rate * 1.5) * (hours-40))
else:
    pay = rate * hours

print('Pay: ', pay)