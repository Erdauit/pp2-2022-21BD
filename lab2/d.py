size = int(input())
if (size % 2 == 0):
    for i in range (size):
        for j in range (size):
            if i >= j:
                print ("#", end = "")
            else:
                print (".", end = "")
        print ("")
if (size % 2 == 1):
    for i in range (size):
        for j in range (size):
            if i + j >= size - 1:
                print ("#", end = "")
            else:
                print (".", end = "")
        print ("")
