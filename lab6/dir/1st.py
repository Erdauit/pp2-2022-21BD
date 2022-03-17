import os
from traceback import print_tb

a = os.getcwd()

directory = []
file = []

for i in os.listdir(a):
    if os.path.isdir(i):
        directory.append(i)
    if os.path.isfile(i):
        file.append(i)

print(directory)
print(file)
print(os.listdir())