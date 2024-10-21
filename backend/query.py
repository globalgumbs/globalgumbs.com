import mysql.connector

class Query:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                user='dev',
                password='PlanetComics89',
                host='34.130.114.87',
                database='hoops_db'
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def print_tables(self):
        if self.connection:
            self.cursor.execute("SHOW TABLES;")
            tables = self.cursor.fetchall()
            for table in tables:
                print(table)

    def get_team_stats(self, team_ids: list):
        """ Arg needs to be a list of valid team ID's or an empty list"""
        if not team_ids:
            return []
        placeholders = ', '.join(['%s'] * len(team_ids))
        query = f"SELECT * FROM Teams WHERE TeamID IN ({placeholders})"
        self.cursor.execute(query, team_ids)
        return self.cursor.fetchall()
    
    
# query = Query()
# result = query.get_team_stats([1610612743])
# if not result:
#     print("No data")
# else:
#     print(result)