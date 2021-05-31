"""
Exercise 3: Write a program to read through a email log, build a his-
togram using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""



#fname=input("Enter file name: ")
fname = 'mbox-short.txt'                                #filename
fhand = open(fname)                                     #file handler

address = dict()                                        #dict

for line in fhand:                                      #reading line
    if line.startswith('From'):
        word_list = line.rstrip().split()
        for word in range(len(line)):                   #reading word
            list_address = word_list[1]                 #address (str)
            address[list_address] = address.get(list_address, 0) + 1            #checking if key is in dictionary
                                                                                #if not, assigning 0 to it, otherwise incrementing it
    else:
        continue                                        #skip

print(address)                                          #output

