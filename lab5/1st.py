import re 
a = str(input())
b = re.search("ab+", a)

if b:
    print("yeas")
else:
    print("no")