a = int(input())
x = 0
answer = []
def checkpass(a):
    x = 0
    y = 0
    z = 0
    for i in a:
        if (ord(i) >= 48 and ord(i) <= 57):
            x+=1
        elif (ord(i) >= 65 and ord(i) <= 90):
            y+=1
        elif (ord(i) >= 97 and ord(i) <= 122):
            z+=1
    if (x > 0 and y > 0 and z > 0):
        return True

while x != a:
    b = str(input())
    answer.append(b)
    x = x + 1
answer1 = []
for i in answer:
    if checkpass(i) == True:
        answer1.append(i)
answer1 = sorted(set(answer1))
print (len(answer1))
for i in answer1:
    print (i)
