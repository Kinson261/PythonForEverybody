"""
We are given a string and we need to remove all duplicates from it? What will be the output if the order of character matters? Examples:

    Input : geeksforgeeks
    Output : efgkors

"""

user_input = "geeksforgeeks"
output = []

# adding all letters without duplicate in output
for letter in user_input:
    if letter not in output:
        output.append(letter)
    else:
        continue

# sorting letters in alphabetical order
output = sorted(output, key=lambda letter: letter.lower())

print(output)
# uncomment next line if your output should be a string
# print("".join(output))
