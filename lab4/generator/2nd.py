a = int(input())

def even(a):
    for i in range(a+1):
        if (i%2 == 0):
            yield i

for i in even(a):
    print(i, end=', ')