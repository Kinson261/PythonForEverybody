"""
Exercise 2: Write a program that categorizes each email message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""

#fname = input('Enter file name')
fname = 'mbox-short.txt'                                    #filename
fhand = open(fname)                                         #file handler

days = {}                                                   #dict

for line in fhand:                                          #reading line
    if line.startswith('From '):
        list_word = line.rstrip().split()
        for word in range(len(list_word)):                  #reading word
            key = list_word[2]                              #days(str)
            days[key] = days.get(key, 0) + 1                #checking if key is in dictionary
                                                            #if not, assigning 0 to it, otherwise incrementing it
    else:
        continue                                            #skip

print(days)                                                 #output
