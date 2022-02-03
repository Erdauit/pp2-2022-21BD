a = int(input())
i = 0
erdaut = []
while (i < a):
    erdaut.append(input())
    i += 1

for l in erdaut:
    if (l.find("@gmail.com") > 0):
        word = l.replace("@gmail.com", "")
        print(word)
