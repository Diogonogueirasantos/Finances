import sqlite3
import Login_User

class Database_Users:
    def __init__(self):
        self.database_Conection()

    def database_Conection(self):
        self.create_Database = sqlite3.connect('Users.db')
        self.slq_Cursor = self.create_Database.cursor()

    def Create_newUser(self):
        self.slq_Cursor.execute(f'select * from client;')



inicializador = Database_Users()
inicializador.Create_newUser()