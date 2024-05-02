import psycopg2
from config import host, user, password, database 

try:
    # Connection to existing database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    connection.autocommit = True
    
    with connection.cursor() as cursor:
        cursor.execute(""" create table snake(
        username VARCHAR(255),
        score INT
    );""")
        
    print("[INFO] Table created successfully!")

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
