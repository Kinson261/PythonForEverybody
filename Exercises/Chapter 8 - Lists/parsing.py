fname = 'mbox-short.txt'

fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2:])