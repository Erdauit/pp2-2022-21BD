def toLowerCase(c):
    lower = ""
    for i in c : 
        if (i >= 'A' and i <= 'Z'):
            lower += chr(ord(i) + 32)
        else :
            lower += i

    print (lower)


c = input()
toLowerCase(c)