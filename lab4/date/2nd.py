import datetime
today = datetime.datetime.now()

print("today's datetime is:")
print(today)
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
print("yesterday's datetime is:")
print(yesterday)
tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
print("tomorrow's datetime is:")
print(tomorrow)
