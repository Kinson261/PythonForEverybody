"""
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

fname = input('Enter a file name: ')
#fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('File is missing: ', fname)
    print('Program will exit.')
    exit()

mails = dict()

# reading mails
for line in fhand:
    if line.startswith("From "):
        line.rstrip()
        words = list(line.split())
        for word in words:
            mail = words[1]
            if mail in mails:
                mails[mail] += 1
            else:
                mails[mail] = 1
print(mails)


# creating a list of tuples for ranging dict by values
lst = list()
for (email, count) in list(mails.items()):
    lst.append((count, email))
lst.sort(reverse=True)
print(lst[1])

