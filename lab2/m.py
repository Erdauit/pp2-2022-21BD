num = []
while(True):
    x = input().split()
    if x[0]== '0':
        break
    num.append((x[2], x[1], x[0]))
        
num = sorted(num)
b = []
for i in num:
    b.append((i[2], i[1], i[0]))
for i in b:
    print (*i)