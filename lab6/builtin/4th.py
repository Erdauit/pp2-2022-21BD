import math, time
a = int(input())
mill = int(input())

time.sleep(mill/1000)

print("Square root of",a,"after",mill,"miliseconds is" ,math.sqrt(a))
