"""
Exercise 3

    Write a program to prompt for a score between 0.0 and
    1.0. If the score is out of range, print an error message. If the score is
    between 0.0 and 1.0, print a grade using the following table:

Score   Grade
>= 0.9    A
>= 0.8    B
>= 0.7    C
>= 0.6    D
< 0.6     F

    Run the program repeatedly as shown above to test the various different values for
    input.

"""

print('\n\n________________________________________')
print('Exercise 3')

inp = input('Enter a score from 0.0 to 1.: \t')

try:
    score = float(inp)

    if score <= 1.0 and score >= 0.9:
        grade = 'A'
    elif score <= 0.9 and score >= 0.8:
        grade = 'B'
    elif score <= 0.8 and score >= 0.7:
        grade = 'C'
    elif score <= 0.7 and score >= 0.6:
        grade = 'D'
    elif score <= 0.6 and score >= 0:
        grade = 'F'

    print('Grade: \t', grade)

except:
    print('Error, enter as numeric value between 0.0 and 1.0')
