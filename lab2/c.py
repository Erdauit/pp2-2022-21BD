size = int(input())
for i in range(size):
    for j in range(size):
        if i == 0:
            print(j,end=" ")
        elif j == 0:
            print(i,end=" ")
        elif i == j:
            print(i*j,end=" ")
        else:
            print(0,end=" ")
    print()