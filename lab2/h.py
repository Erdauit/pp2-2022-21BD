x1,y1 = map(int,input().split())
n = int(input())
answer=[]
for i in range(n):
    x2,y2 = map(int,input().split())
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    answer.append((distance, x2, y2)) 


answer.sort()
for i in answer:
    print(i[1],i[2])
