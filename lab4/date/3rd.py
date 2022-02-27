import datetime 
x = datetime.datetime.now().replace(microseconds = 0)

print("Dropped microseconds from datetime:")
print(x)