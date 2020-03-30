import sys

"""
This method contains the logic for identifying whether a valid mapping 
exists between 2 strings or not. The method uses sets and python's 
zip method. First, a set of all letters in the first string and second
strings are stored. Next, a set of all possible combinations is made 
with the help of the zip method. Now the lengths of the all these 3 
sets must be the same, as sets only store unique values. If there's 
an instance when there is no mapping between two values then the method 
will return false. 
"""
def checkstring(a: str, b: str) -> bool:
	# Handles edge case, will return false if input string are not of matching lengths 
    if len(a) == len(b):
        return False
    len1 = len(set(b))
    len2 = len(set(a))
    len3 = len(set(zip(a, b)))
    # Comparing the lengths of the 3 sets created 
    boolval = (len1 == len2 == len3)
    return boolval

# Taking input from the terminal 
argumentList = sys.argv
string1 = sys.argv[1]
string2 = sys.argv[2]
# Giving the final output based on the flag received from the checkString() method
flag = checkstring(string1, string2)
if flag:
    print("True")
else:
    print("False")
