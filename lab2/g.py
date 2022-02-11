t = {}
n = int(input()) #demons
for i in range(n):
    name,technic = map(str, input().split())
    t.setdefault(technic,0)
    t[technic] += 1
    
m = int(input()) #hunters
for i in range(m):
    name,technic2,e = input().split()
    e = int(e)
    if technic2 in t:
        t[technic2] -= e
answer = 0
for i in t.values():
    if i > 0:
        answer+=i

print("Demons left: " + str(answer) )