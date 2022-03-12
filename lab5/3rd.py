import re
a = input()
b = re.findall("\w+_\w+", a)
print(b)
