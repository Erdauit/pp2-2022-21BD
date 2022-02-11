vvod= input().split()

if len(vvod) == 1: #на случай если в 5 тесте инпут через строку...
    w = int(input())
    vvod.append(w)
    
n = int(vvod[0])
x = int(vvod[1])
arr = []
for i in range(n):
    b = x + 2 * i
    arr.append(b)

xor = arr[0]

for i in range(1,len(arr)):
    x = x ^ arr[i]

print (x)

