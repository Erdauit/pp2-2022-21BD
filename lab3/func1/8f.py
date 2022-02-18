numbers = list(map(int, input().split()))
def has_007(numbers):
    for i in range (len(numbers)-1):
         if (numbers[i] == 0 and numbers[i+1]==0 and numbers[i+2]==7 ):
             return True
             
    else:
        return False

if has_007(numbers):
    print('OK')
else:
    print('NO')
