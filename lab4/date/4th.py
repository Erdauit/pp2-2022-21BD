import datetime as erdaut
x = erdaut.datetime.now()
then = erdaut.datetime.now() + erdaut.timedelta(days=1)

delta = then - x
print(delta.total_seconds())

# print((then - x).total_seconds())
