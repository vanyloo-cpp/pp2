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

    while True:
        print("1.Function that returns all records based on a pattern")
        print("2.Insert new user by name and phone, update phone if user already exists")
        print("3.Insert many new users by list of name and phone.")
        print("4.Querying data from the tables with pagination")
        print("5.Deleting data from tables by username or phone")
        print("6.to quit")
        action = input("Enter the option number:")
        
        if action == '1':
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern varchar(50))
                                        RETURNS TABLE (name varchar(50), phone_number varchar(50)) AS $$
                                    BEGIN
                                        RETURN QUERY 
                                        SELECT phonebook.name, phonebook.phone_number FROM phonebook WHERE phonebook.name ILIKE '%' || pattern || '%' OR phonebook.phone_number LIKE '%' || pattern || '%';
                                    END;
                                    $$ LANGUAGE plpgsql;

                                    """)
                
                    pattern = input("Enter search pattern:")
                    cursor.execute("SELECT * FROM get_records_by_pattern(%s)", (pattern,))
                    records = cursor.fetchall()
                    if records:
                        print("Matching records:")
                        for record in records:
                            print(record)
                    else:
                        print("No matching records found.")
                        
                print("Function created successfully!")
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
        
        elif action == '2':
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""CREATE OR REPLACE FUNCTION insert_or_update_user(name_in TEXT, phone_in TEXT)
                                      RETURNS VOID AS $$
                                      BEGIN
                                          IF EXISTS (SELECT 1 FROM phonebook WHERE name = name_in) THEN
                                              UPDATE phonebook SET phone_number = phone_in WHERE name = name_in;
                                          ELSE
                                              INSERT INTO phonebook (name, phone_number) VALUES (name_in, phone_in);
                                          END IF;
                                      END;
                                      $$ LANGUAGE plpgsql;
                                    """) 
                
                # Вызываем процедуру, передавая ей аргументы
                name = input("Enter user name:")
                phone = input("Enter user phone number:")
                cursor.callproc("insert_or_update_user", [name, phone])
                print("Procedure called successfully!")
                print("Procedure created successfully!")
                
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)    
        
        elif action == '3':
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""CREATE OR REPLACE PROCEDURE insert_many_users(names_in TEXT[], phones_in TEXT[])
                                        AS $$
                                        DECLARE
                                            i INTEGER;
                                            name_text TEXT;
                                            phone_text TEXT;
                                        BEGIN
                                            FOR i IN 1..array_length(names_in, 1) LOOP
                                                name_text := names_in[i];
                                                phone_text := phones_in[i];

                                                -- Insert into the phonebook without checking the length of phone_text
                                                INSERT INTO phonebook (name, phone_number) VALUES (name_text, phone_text);

                                            END LOOP;
                                        END;
                                        $$ LANGUAGE plpgsql;""")
                print("Procedure created successfully!") 
                
                names = ['Alice', 'Bob', 'Charlie']
                phones = ['1234567890', '9876543210', '5555555555']
                cursor.callproc("insert_many_users", [names, phones])
                print("Procedure called successfully!")
                
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
        
        elif action == '4':
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""CREATE OR REPLACE FUNCTION get_records_with_pagination(limit_in INT, offset_in INT)
                                      RETURNS TABLE (name TEXT, phone_number TEXT) AS $$
                                      BEGIN
                                          RETURN QUERY 
                                          SELECT name, phone_number FROM phonebook ORDER BY name LIMIT limit_in OFFSET offset_in;
                                      END;
                                      $$ LANGUAGE plpgsql;""")
                print("Function created successfully!") 
                
                # Вызываем функцию, передавая ей аргументы
                limit = int(input("Enter limit:"))
                offset = int(input("Enter offset:"))
                cursor.execute("SELECT * FROM get_records_with_pagination(%s, %s)", (limit, offset))
                records = cursor.fetchall()
                if records:
                    print("Records with pagination:")
                    for record in records:
                        print(record)
                else:
                    print("No records found.")
                
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)  
        
        elif action == '5':
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""CREATE OR REPLACE PROCEDURE delete_data_by_username_or_phone(search_pattern TEXT)
                                      AS $$
                                      BEGIN
                                          DELETE FROM phonebook WHERE name = search_pattern OR phone_number = search_pattern;
                                      END;
                                      $$ LANGUAGE plpgsql;""")
                print("Procedure created successfully!") 
                
                # Вызываем процедуру, передавая ей аргументы
                search_pattern = input("Enter username or phone number to delete:")
                cursor.callproc("delete_data_by_username_or_phone", [search_pattern])
                print("Procedure called successfully!")
                
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
        elif action == '6':
            break
        else:
            print("Invalid option. Please enter a valid option number.")
                    
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
