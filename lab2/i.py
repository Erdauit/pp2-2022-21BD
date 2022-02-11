a = int(input())
shelf = []
taken = []
for i in range(a):
    b = input().split()
    if (b[0] == "1"):
        shelf.append(b[1])
    elif (b[0] == "2"):
        taken.append(shelf[0])
        shelf.pop(0)
for i in taken:
    print (i, end = " ")
