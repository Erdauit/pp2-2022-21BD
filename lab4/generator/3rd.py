a = int(input())

def div(a):
    for i in range(a+1):
        if (i%3 == 0) and (i%4 == 0):
            yield i

for i in div(a):
    print(i)