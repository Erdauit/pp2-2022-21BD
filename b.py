def uuuu(a):
    ascii = []
    total = 0
    for character in a:
        ascii.append(ord(character))
    total = sum(ascii)
    return total

r = input()
if (uuuu(r) > 300): 
    print ("It is tasty!")
else :
    print ("Oh, no!")