from itertools import permutations 
 
def permutation(str): 
    a = permutations(str) 
    for x in a: 
        for y in x: 
            print(y, end = "") 
        print (" ")


str = input()
permutation(str)