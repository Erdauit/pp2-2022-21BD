import psycopg2
from config import database

config = psycopg2.connect(**database)
current = config.cursor()

show = '''
SELECT * FROM phonebook1;
'''

current.execute(show)
result = current.fetchall()

for i in result:
    print(*i)
current.close()