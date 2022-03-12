import re
a = input()
b = re.sub("[\s,.]", ":", a)

print(b)
