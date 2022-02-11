num = []
x = 1
while(x!=0):
    x = int(input())
    if x!=0:
        num.append(x)
        
answer = []

for i in range(len(num)//2):
    answer.append(num[0] + num[-1])
    num.pop(0)
    num.pop(-1)
    if len(num) == 1:
        answer.append(num[0])
for i in answer:
    print(i, end=" ")