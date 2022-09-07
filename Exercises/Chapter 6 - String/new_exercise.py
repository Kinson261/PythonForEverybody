#question 
'''i am learning to contribute to open source

We are given a string and we need to remove all duplicates from it? What will be the output if the order of character matters? Examples:

    Input : geeksforgeeks 
    Output : efgkors'''

def removeDuplicate(str):
    s=set(str)
    s="".join(s)
    print("Without Order:",s)
    t=""
    for i in str:
        if(i in t):
            pass
        else:
            t=t+i
        print("With Order:",t)
     
str="geeksforgeeks"
removeDuplicate(str)
