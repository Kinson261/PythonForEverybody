"""
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

# fname = input('Enter a file name: ')
fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('File is missing: ', fname)
    print('Program will exit.')
    exit()

time = dict()

# reading mails
for line in fhand:
    if line.startswith("From "):
        line.rstrip()
        words = list(line.split())
        for word in words:
            time_comp = words[5]
            X = time_comp.split(':')
            hours = X[0]
            if hours in time:
                time[hours] += 1
                continue
            else:
                time[hours] = 1
                continue

print(time)
