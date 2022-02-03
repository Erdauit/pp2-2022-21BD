s = input()
t = input()
array1 = []
br = 0
for i in s:
    array1.append(i)
    
for l in array1:
    if (l == t):
        br += 1

if (br == 1):
    ernar = s.index(t)
    print (ernar)
if (br > 1):
    ernar = s.index(t)
    erdautgood = s.rindex(t)
    print (ernar, erdautgood)




    
