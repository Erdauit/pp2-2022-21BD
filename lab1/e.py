a, b = map(int, input().split()) #distance and cartridges

#идет распределение переменных на а и в (через пробел)
 
def isPrime(n):
    for i in range(2, (n//2)+1):    
        if n % i == 0:
            return False

    return True

#we need to find prime number and even cartridge

if a < 500:
    if isPrime(a) == True:
        if b % 2 == 0:
            print ("Good job!")   #correct
            exit(0)
        
        else:
            print ("Try next time!")
    else:
        print ("Try next time!")
else:
    print ("Try next time!")

