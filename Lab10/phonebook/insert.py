import psycopg2
from config import database
import csv

config = psycopg2.connect(**database)
current = config.cursor()
phone_list = []

insert_table = '''
INSERT INTO phonebook1 VALUES(%s, %s, %s);
'''

count = int(input())
if count == 1:
    username = str(input('Enter your username '))
    number = str(input('Enter your phone number '))
    city = str(input('Enter your city'))
    current.execute(insert_table, (username, number, city))
    
if count == 2:
    with open('example.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'name: {row[0]}, number: {row[1]}')
                phone_list.append((row[0], row[1]))
                line_count += 1


current.close()
config.commit()
config.close()