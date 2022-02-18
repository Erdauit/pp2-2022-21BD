numbers = list(map(int, input().split()))
def has_33(numbers):
    for i in range (len(numbers)-1):
         if (numbers[i] == 3 and numbers[i+1]==3 ):
             return True
             
    else:
        return False

if has_33(numbers):
    print('OK')
else:
    print('NO')
