"""
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the email came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

import random

#fname = input('Enter file name: ')
fname = 'mbox-short.txt'                                    #file name

domain = dict()                                             #dict

try:
    fhand = open(fname)                                     #fhandler
except:
    print('File is missing: ', fname)
    print('Program will now exit')
    exit()

for line in fhand:                                          #read line
    if line.startswith('From'):
        line = line.rstrip().split()
        email = line[1]                                     #full email address
        email_ext = email.split(sep='@')                    #splitting domain from email address ==> results in a list
        domain_list = email_ext[1:]
        domain_list = '.'.join(domain_list)                 #joining remaining elements of the list into a string
        domain[domain_list]= random.randint(0,10)           #generating random value for dictionary
    else:
        continue                                            #skip

print(domain)                                               #output
