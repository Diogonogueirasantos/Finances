from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery



class users_Informations(QDialog):
    def __init__(self):
        super().__init__()

    def search_record(self, user, password):
        self.database_Conection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Conection.setDatabaseName('Users.db')
        self.database_Conection.open()
        self.search_User = QSqlQuery(self.database_Conection)
        login_Query = 'select name where name=? and user_Password=?'
        self.search_User.prepare(login_Query)
        self.search_User.bindValue(0, user)
        self.search_User.bindValue(1, password)
        if self.search_User.exec():
            if self.search_User.next():
               print(f'seja muito bem vindo(a) {user}')
        else:
            self.close()

    def new_user(self):
        print('Funcionou')