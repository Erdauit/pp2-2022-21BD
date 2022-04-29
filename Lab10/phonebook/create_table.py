import psycopg2
from config import database

config = psycopg2.connect(**database)
current = config.cursor()

create_table = '''
    CREATE TABLE snake(
        name VARCHAR(255),
        score VARCHAR(255),
        level VARCHAR(255)
    )
'''
current.execute(create_table)

current.close()
config.commit()
config.close()