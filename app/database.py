# imports
import sqlite3

class Database():
    DATABASE_NAME = "jspython.db"

    def getConn(self):
        try:
            return sqlite3.connect(self.DATABASE_NAME)
        except ValueError:
            print("Error de conexión DB")


    def createTables(self):
        """ Método de creación de tablas sqlite""" 
        try:
            tables = [
                """CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        lastname TEXT NOT NULL
                    )
                """
            ]
            conn = self.getConn()
            cursor = conn.cursor()
            for table in tables:
                cursor.execute(table)
        except ValueError:
            print(str(ValueError))





