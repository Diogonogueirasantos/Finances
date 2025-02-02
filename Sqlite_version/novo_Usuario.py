from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon, QMovie, QFont
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtCore import QSize




class New_User(QDialog):
    def __init__(self):
        super().__init__()
        self.InitializationUI()

    def InitializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle("Create account")
        self.create_UserSettings()
        self.show()

    def base_Informations(self):
        self.database_Connection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Connection.setDatabaseName('Users.db')
        if self.database_Connection.open():
            print('Conexão estabelecida!!')
        else:
            print(f'O banco de dados não foi encontrado ! {self.database_Connection.lastError().text()}')

    def create_UserSettings(self):
        self.user_Animation = QMovie('images/do-utilizador.gif')
        self.password_Animation = QMovie('images/cadeado.gif')
        self.createuser_Label = QLabel(self)
        self.password_Label = QLabel(self)
        self.createuser_Label.setMovie(self.user_Animation)
        self.password_Label.setMovie(self.password_Animation)
        self.user_Animation.setScaledSize(QSize(30, 30))
        self.password_Animation.setScaledSize(QSize(30, 30))
        self.user_Animation.start()
        self.password_Animation.start()
        self.createuser_Label.move(100, 100)
        self.password_Label.move(97, 150)
        self.createuser_Lineedit = QLineEdit(self)
        self.createpassword_Lineedit = QLineEdit(self)
        self.confirm_Userpassword_Lineedit = QLineEdit(self)
        self.createuser_Lineedit.move(130, 103)
        self.createpassword_Lineedit.move(133, 150)
        self.confirm_Userpassword_Lineedit.move(133, 195)
        self.createuser_Lineedit.setPlaceholderText('User name')
        self.createpassword_Lineedit.setPlaceholderText('password')
        self.confirm_Userpassword_Lineedit.setPlaceholderText('Confirm')
        self.createpassword_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_Userpassword_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.createuser_Button = QPushButton('Create', self)
        self.createuser_Button.move(150, 270)
        self.hidden_Password = QCheckBox('Show password', self)
        self.hidden_Password.move(100, 230)
        self.hidden_Password.toggled.connect(self.settings_box_lineedit)
        self.createuser_Button.clicked.connect(self.create_User)


    def settings_box_lineedit(self, checked):
        if checked:
            self.createpassword_Lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirm_Userpassword_Lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.createpassword_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirm_Userpassword_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)



    def create_User(self):
        self.sql_Cursor = QSqlQuery(self.base_Informations())
        add_NewUser = 'insert into Users (Name, user_Password) values (?, ?)'
        self.sql_Cursor.prepare(add_NewUser)
        if self.createpassword_Lineedit.text() == self.confirm_Userpassword_Lineedit.text():
            user_Name = self.createuser_Lineedit.text()
            Password = self.createpassword_Lineedit.text()
            self.sql_Cursor.addBindValue(user_Name)
            self.sql_Cursor.addBindValue(Password)
            if self.sql_Cursor.exec():
                self.database_Connection.commit()
                QMessageBox.information(self, 'Usuário criado com sucesso!', f'Seja muito bem vindo(a) {self.createuser_Lineedit.text()}', QMessageBox.StandardButton.Ok)
                self.close()

