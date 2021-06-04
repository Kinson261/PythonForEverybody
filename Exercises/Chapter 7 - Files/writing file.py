fname = open('output.txt', 'w')

line1 = 'This is an output\n'
line2 = 'This is another output\n'
fname.write(line1)
fname.write(line2)

fname.close()