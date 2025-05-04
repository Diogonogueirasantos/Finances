import sys

from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


style = """
    .settings_Buttons{
      background:#000;
      color:#fff;
      padding: 5px;
      border-radius: 7px;
    }
    
    .settings_Buttons:hover{
      background: #7c7a7a;
      color: #fff;
    }
"""

class New_User(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.InitializationUI()

    def InitializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle("Create account")
        self.create_user_Widgets()
        self.create_user_Widgets_Position()
        self.create_user_Widgets_Settings()
        self.create_user_Buttons()
        self.show()

    def base_Informations(self):
        self.database_Connection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Connection.setDatabaseName('customers_info')
        if self.database_Connection.open():
            print('Conexão estabelecida!!')
        else:
            print(f'O banco de dados não foi encontrado ! {self.database_Connection.lastError().text()}')

    def create_user_Widgets(self):
        self.create_user_Label = QLabel("New User:", self)
        self.create_user_Line = QLineEdit(self)
        self.create_user_password_Label = QLabel("Password:", self)
        self.create_user_password_Line = QLineEdit(self)
        self.confirm_user_password_Label = QLabel("Confirm:", self)
        self.confirm_user_password_Line = QLineEdit(self)

    def create_user_Widgets_Position(self):
        self.create_user_Label.move(55, 107)
        self.create_user_Line.move(130, 103)
        self.create_user_password_Label.move(55, 150)
        self.create_user_password_Line.move(133, 147)
        self.confirm_user_password_Label.move(70, 190)
        self.confirm_user_password_Line.move(133, 185)


    def create_user_Widgets_Settings(self):
        self.create_user_Line.setClearButtonEnabled(True)
        self.create_user_password_Line.setClearButtonEnabled(True)
        self.confirm_user_password_Line.setClearButtonEnabled(True)
        self.create_user_Line.setPlaceholderText("Insert email")
        self.create_user_password_Line.setPlaceholderText("Insert password")
        self.confirm_user_password_Line.setPlaceholderText("Confirm Password")

    def create_user_Buttons(self):
        self.create_user_Button = QPushButton("Create", self)
        self.create_user_Button.setProperty('class', 'settings_Buttons')
        self.create_user_Button.move(165, 235)
        self.create_user_Button.clicked.connect(self.insert_New_User)


    def create_user_CheckBox(self):
        self.hidden_user_Password = QCheckBox("Show Password", self)
        self.hidden_user_Password.toggled.connect(self.settings_CheckBox)

    def settings_CheckBox(self, checked=None):
        if checked:
            self.create_user_password_Line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirm_user_password_Line.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.create_user_password_Line.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirm_user_password_Line.setEchoMode(QLineEdit.EchoMode.Password)

    def settings_Button(self):
        if self.create_user_Line.text() != "":
            self.create_user_Button.setEnabled(True)
        else:
            self.create_user_Button.setEnabled(False)

    def insert_New_User(self):
        self.sql_Cursor = QSqlQuery(self.base_Informations())
        add_NewUser = 'insert into customers_records(email_client, Password_client) values (?, ?)'
        self.sql_Cursor.prepare(add_NewUser)
        if self.create_user_password_Line.text() == self.confirm_user_password_Line.text():
            user_Name = self.create_user_Line.text().strip()
            Password = self.create_user_password_Line.text().strip()
            self.sql_Cursor.addBindValue(user_Name)
            self.sql_Cursor.addBindValue(Password)
            if self.sql_Cursor.exec():
                self.database_Connection.commit()
                QMessageBox.information(self, 'Usuário criado com sucesso!', f'Seja muito bem vindo(a) {self.create_user_Line.text().strip()}', QMessageBox.StandardButton.Ok)
                self.close()
        elif self.create_user_password_Line.text() != self.confirm_user_password_Line.text():
            QMessageBox.information(self, 'Falha ao criar o usuário!', 'Ops... parece que as senhas não se coincidem!', QMessageBox.StandardButton.Ok)


