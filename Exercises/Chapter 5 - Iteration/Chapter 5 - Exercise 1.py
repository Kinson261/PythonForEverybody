""""
    Exercise 1:
    Write a program which repeatedly reads numbers until the
    user enters “done”. Once “done” is entered, print out the total, count,
    and average of the numbers. If the user enters anything other than a
    number, detect their mistake using try and except and print an error
    message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
"""

count = 0               #initialization
total = 0

while True:             #infinite loop
    line = input("Enter a number: \t ")
    try:
        total = total + float(line)         #convert string to float
    except:
        if line == 'done':                  #keyword to stop input
            break
        else:
            print('Invalid input')          #only numbers are permitted
            continue

    count = count + 1                       #counts only valid input

    average = total / count

print('\n\n Sum= ', total,
      '\t\t count= ', count,
      '\t\t Average number= ', average)
