# from dataclasses import dataclass
# import mysql.connector


# @dataclass
# class Sql:
#     """SQL query dataclass."""
#     query: str
#     def __init__(self):
#         self.mydb = mysql.connector.connect(
#             host="Jemcarlo.mysql.pythonanywhere-services.com",
#             user="Jemcarlo",
#             password="admin*1234",
#             database='Jemcarlo$default'
#         )
#         self.cursor = self.mydb.cursor()

#     def execute(self,query:str):
#         try:
#             self.cursor.execute(query)
#             self.mydb.commit()
#             return True
#         except Exception as e:
#             print(f"Error: {e}")
            
import mysql.connector
from dataclasses import dataclass

@dataclass
class Sql:
    """SQL query dataclass."""
    db_name: str
    mydb: mysql.connector.MySQLConnection = None
    cursor: mysql.connector.cursor = None

    def __post_init__(self):
        self.connect()

    def connect(self):
        """Establish a connection to the MySQL database."""
        self.mydb = mysql.connector.connect(
            host="Jemcarlo.mysql.pythonanywhere-services.com",
            user="Jemcarlo",
            password="admin*1234",
            database=self.db_name
        )
        self.cursor = self.mydb.cursor()

    def create_database(self, database_name: str):
        """Create a new database."""
        self.execute(f"CREATE DATABASE {database_name}")

    def delete_database(self, database_name: str):
        """Delete an existing database."""
        self.execute(f"DROP DATABASE {database_name}")

    def create_table(self, table_name: str, columns: str):
        """Create a new table."""
        self.execute(f"CREATE TABLE {table_name} ({columns})")

    def delete_table(self, table_name: str):
        """Delete an existing table."""
        self.execute(f"DROP TABLE {table_name}")

    def execute(self, query: str):
        """Execute a SQL query."""
        try:
            self.cursor.execute(query)
            self.mydb.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def fetch_all(self, query: str):
        """Fetch all results from a SQL query."""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def last_insert_id(self):
        """Get the last inserted row ID."""
        return self.cursor.lastrowid

    def close(self):
        """Close the database connection."""
        self.cursor.close()
        self.mydb.close()