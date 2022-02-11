n = int(input()) 
arr = list(map(int, input().split())) #в арр кидаются числа(без ограничений)
arr.sort(reverse=True)
print (arr[0]*arr[1])
