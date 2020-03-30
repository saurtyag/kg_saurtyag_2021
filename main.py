import sys


def checkstring(a: str, b: str) -> bool:
    if len(a) == len(b):
        return False
    len1 = len(set(b))
    len2 = len(set(a))
    len3 = len(set(zip(a, b)))
    boolval = (len1 == len2 == len3)
    return boolval


argumentList = sys.argv
string1 = sys.argv[1]
string2 = sys.argv[2]
print(string1)
print(string2)
flag = checkstring(string1, string2)
if flag:
    print("True")
else:
    print("False")
