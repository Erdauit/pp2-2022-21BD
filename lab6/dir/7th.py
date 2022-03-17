# import shutil
# shutil.copyfile('erdauit.txt', 'test2.txt')

second = open('test2.txt', 'w')
first = open('erdauit.txt', 'r')
for i in first:
    second.write(i)