import mysql.connector
import getpass

class Database_manager:
    def __init__(self):
        self.Database_conection()

    def Database_conection(self):
        user = getpass.getpass(prompt="Por favor insira seu nome de usuário: ")
        password_User = getpass.getpass(prompt="Digite sua senha: ")
        self.conector = mysql.connector.connect(user=f'{user}', password=f'{password_User}',
                                                host='localhost', database='Clientes')
        self.cursor = self.conector.cursor()
        if self.conector.is_connected():
            print("Cenexão estabelecida!")




Instaciador = Database_manager()