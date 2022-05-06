import psycopg2, csv, re 
from config import database
config = psycopg2.connect(**database) 
current = config.cursor() 
 
search = """ 
CREATE OR REPLACE FUNCTION getT(pname VARCHAR) 
    RETURNS TABLE (  
        name VARCHAR,  
        number VARCHAR 
) 
AS $$ 
BEGIN 
    RETURN QUERY SELECT * FROM phonebook WHERE phonebook.name ILIKE pname OR phonebook.number ILIKE pname; 
END; $$ 
 
LANGUAGE PLPGSQL; 
 
SELECT * FROM getT (%s); 
""" 
 
update = """ 
CREATE OR REPLACE PROCEDURE insertT(pname VARCHAR, phone VARCHAR) 
AS $$ 
BEGIN 
    IF EXISTS (SELECT * FROM phoneBook WHERE name = pname) THEN 
        UPDATE phoneBook SET number = phone WHERE name = pname; 
    ELSE 
        INSERT INTO phonebook VALUES(pname, phone); 
    END IF; 
END; $$ 
LANGUAGE PLPGSQL; 
 
CALL insertT(%s, %s); 
""" 
 
def check(s): 
    return bool(re.match(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", s)) 
 
delete = """ 
CREATE OR REPLACE PROCEDURE deleteT(pname VARCHAR) 
AS $$ 
BEGIN 
    DELETE FROM PhoneBook WHERE Phonebook.name = pname OR phonebook.number = pname; 
END; $$ 
LANGUAGE PLPGSQL; 
 
CALL deleteT(%s); 
""" 
 
pagination = """ 
SELECT * FROM phonebook LIMIT %s OFFSET %s; 
""" 
      
while True: 
    command = input("search, iou, insert, pagination, delete, exit\n") 
     
    if command == 'search': 
        n = input("Введите имя или номер\n") 
        word = '%' + n + '%' 
        current.execute(search, [word]) 
        print(*current.fetchall(), sep = '\n') 
             
    if command == 'iou':  
        name = input("Введите имя: ")  
        phone_number = input("Введите номер: ") 
        current.execute(update, (name, phone_number)) 
 
    if command == 'insert': 
        with open("phonebook.csv", "r") as f: 
            reader = csv.reader(f, delimiter=",") 
            for row in reader: 
                if check(row[1]): 
                    current.execute(update, row) 
                else: 
                    print(*row) 
            config.commit() 
    if command == 'delete': 
        name = input("Введите имя или номер что удалить: ") 
        current.execute(delete, [name]) 
        config.commit() 
    if command == 'exit': 
        break 
    if command == 'pagination': 
        a, b = map(int, input("LIMIT, OFFSET: ").split()) 
        current.execute(pagination, (a, b)) 
        print(*current.fetchall(), sep = '\n') 
         
current.close() 
config.commit() 
config.close()