"""
Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
"""

def chop(mylist1):
    del mylist1[0]
    del mylist1[len(mylist1) - 1]
    return mylist1

def middle(mylist1):
    mylist2 = mylist1[1:len(mylist1)-1]         #does not include last element
    return mylist2



age= [13, 25, 49, 65, 32, 15, 65, 23, 24, 24, 6, 14]

A = chop(age)
print(age)

B = middle(age)
print(age)

print(A is B)                                   #As a verification: should return False
                                                #although the two lists have the same value
                                                #they do not return the same object

