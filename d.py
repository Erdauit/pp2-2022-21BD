a = int(input())
m = input ()
if (m == 'k'):
    cifri = int(input())
    a = round(a/1024, cifri)
if (m == 'b'):
    a = a * 1024
print (a)