"""
Exercise 6

    Rewrite your pay computation with time-and-a-half for overtime
    and create a function called computepay which takes two parameters
    (hours and rate).

    Enter Hours: 45
    Enter Rate: 10
    Pay: 475.0

"""

print('\n\n________________________________________')
print('Exercise 6')


def computepay(hours, rate):
    if hours > 40:
        pay = (rate * 40) + ((rate * 1.5) * (hours - 40))
    else:
        pay = rate * hours
    return pay


try:
    hours = float(input('Enter hours: \t'))
    rate = float(input('Enter rate: \t'))

    total = computepay(hours, rate)
    print('Pay: ', total)

except:
    print('Error, enter a numeric value.')
