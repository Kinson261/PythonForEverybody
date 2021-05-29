"""
Exercise 6: Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.

    Enter a number: 6
    Enter a number: 2
    Enter a number: 9
    Enter a number: 3
    Enter a number: 5
    Enter a number: done
    Maximum: 9.0
    Minimum: 2.0
"""

numbers = []                                        #create a list
while True:
    user_input = input('Enter a number: ')          #input
    try:
        num_user = float(user_input)                #convert input into float
        numbers.append(num_user)                    #add input to list
    except:                                         #catch
        if user_input.lower() == 'done':            #'DONE'=='Done'=='dONE'=='done'
            break                                   #stop cycle
        else:
            print('Please, enter a number')         #guard
            continue

maximum = max(numbers)                              #max from list
minimum = min(numbers)                              #min from list
print('Maximum:\t', maximum)
print('Minimum:\t', minimum)




