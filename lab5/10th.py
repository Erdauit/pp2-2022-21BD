import re as erdaut
def camel_split(string):
    c = erdaut.findall("[A-Z][^A-Z]*", string)
    answers = " ".join(c)
    return answers

a = input()
b = erdaut.sub("\s", "_", camel_split(a).lower())

print(b)