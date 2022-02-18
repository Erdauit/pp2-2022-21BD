numheads = 35
numlegs = 94
import math
def solve(numheads, numlegs):
    #4*rabbits + 2* chickens = 94 -> 2*rabbits + chickens = 47
    # rabbits + chickens =35
    rabbits = (numlegs/2)-numheads
    chickens = numheads - rabbits
    print(rabbits, " ", chickens)


solve (numheads, numlegs)
