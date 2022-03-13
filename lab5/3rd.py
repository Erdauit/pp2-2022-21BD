import re
a = input()
b = re.findall("[^A-Z]\w+_\w+", a)
print(b)
