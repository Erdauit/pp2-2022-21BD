from collections import defaultdict
def zero_value():
    return 0

students, money_to_get = defaultdict(zero_value), 0
for i in range(int(input())):
    name, money = input().split() 
    students[name] += int(money) 
    if students[name] > money_to_get: 
        money_to_get = students[name]

sorted_students = sorted(students)

for i in sorted_students:
    if students[i] == money_to_get:
        print(i, 'is lucky!')
    else:
        out = money_to_get - students[i]
        print(i, 'has to receive', out, 'tenge')