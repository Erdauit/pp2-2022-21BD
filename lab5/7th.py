import re as erdaut 
a = input()
b = erdaut.sub("[_]"," ", a)
c= erdaut.split("\s", b)
for i in range(1,len(c)):
    print(c[0]+""+c[i].capitalize(), end='')
