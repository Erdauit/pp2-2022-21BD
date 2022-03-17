a = input()
upper = 0
lower = 0
for i in a:
    if ord(i) >= 65 and ord(i) <= 90:
        upper+=1
    elif ord(i) >= 97 and ord(i) <= 122:
        lower+=1
print ("Number of uppercase is "+str(upper))
print ("Number of lowercase is "+str(lower))