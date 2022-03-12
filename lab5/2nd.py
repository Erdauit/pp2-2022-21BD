import re
a = input()
if re.search('ab{2,3}', a):
    print("Find")
else:
    print("not found")

