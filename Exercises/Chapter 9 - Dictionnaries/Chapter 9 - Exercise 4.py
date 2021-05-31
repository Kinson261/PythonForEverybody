"""
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the
dictionary has been created, look through the dictionary using a
maximum loop (see Chapter 5: Maximum and minimum loops) to find who
has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
#fname=input("Enter file name: ")
fname = 'mbox-short.txt'                                        #file name
fhand = open(fname)                                             #file handler

dico = dict()                                                   #dict

for line in fhand:                                              #reading line
    if line.startswith('From'):
        word_list = line.rstrip().split()
        for word in range(len(line)):                           #reading word
            address = word_list[1]                              #address (str)
            dico[address] = dico.get(address, 0) + 1            #checking if key is in dictionary
                                                                #if not, assigning 0 to it, otherwise incrementing it
    else:
        continue                                                #skip


print('\n', dico)

mails = list(dico.keys())                                       #list of keys
times = list(dico.values())                                     #list of values
MAX = mails[times.index(max(times))]                            #returns key with max value
print('\nHas the most messages: ', MAX)                         #output





