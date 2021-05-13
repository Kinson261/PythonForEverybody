"""
Exercise 2

    Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
    Enter Hours: 20
    Enter Rate: nine
    Error, please enter numeric input

    Enter Hours: forty
    Error, please enter numeric input
"""

print('\n\n________________________________________')
print('Exercise 2')

inp_hours = input('Enter hours: \t')
inp_rate = input('Enter rate: \t')

try:
    hours = float(inp_hours)
    rate = float(inp_rate)

    if hours > 40:
        pay = (rate * 40) + ((rate * 1.5) * (hours - 40))
    else:
        pay = rate * hours

    print('Pay: ', pay)

except:
    print('\nERROR, please enter numeric input')
