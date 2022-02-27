a = int(input())

def square(a):
    for i in range(a):
        if (i*i) <= a:
            yield i * i

for i in square(a):
    print (i)



