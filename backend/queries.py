import mysql.connector

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            user='dev',
            password='PlanetComics89',
            host='34.130.114.87',
            database='hoops_db'
        )
        print("Connected to MySQL database!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def print_tables(connection):
    if connection:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        for table in tables:
            print(table)
        connection.close()



connection = connect_to_mysql()
print_tables(connection)