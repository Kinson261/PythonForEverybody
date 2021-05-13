"""
Exercise 7

    Rewrite the grade program from the previous chapter using
    a function called computegrade that takes a score as its parameter and
    returns a grade as a string.

Score       Grade
>= 0.9        A
>= 0.8        B
>= 0.7        C
>= 0.6        D
< 0.6         F

"""


def computegrade(score):
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

    return grade


try:
    score = float(input('Enter a score between 0.0 and 1.0: \t'))
    x = computegrade(score)
    print('Grade: ', x)

except:
    print('Error, bad score')
