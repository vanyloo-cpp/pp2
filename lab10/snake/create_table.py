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
        cursor.execute(""" CREATE TABLE Snakedata(
            user_login VARCHAR(255) NOT NULL,
            last_score INT,
            last_level INT,
            last_FPS INT,
            snake_len INT,
            wall_len INT,
            snake_x INT,
            snake_y INT,
            record INT
        );""")
        
    print("[INFO] Table created successfully!")

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
