n = int(input())
a = []  
for i in range(n):
    a.append(int(input()))  

for i in a: 
    if (i) <= 10: 
        print ("Go to work!")
    if (i) > 10 and (i) <= 25:
        print ("You are weak") 
    if (i) > 25 and (i) <=45:
        print ("Okay, fine") 
    if (i) > 45:
        print ("Burn! Burn! Burn Young!")
        