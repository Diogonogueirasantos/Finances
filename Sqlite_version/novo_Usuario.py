import sys

from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class New_User(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.InitializationUI()

    def InitializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle("Create account")
        self.create_user_Widgets()
        self.create_user_Widgets_Settings()
        self.create_user_Buttons()
        self.create_user_CheckBox()
        self.settings_CheckBox()
        self.settings_Button()
        self.layout_Widget()
        self.show()

    def base_Informations(self):
        self.database_Connection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Connection.setDatabaseName('customers_info')
        if self.database_Connection.open():
            print('Conexão estabelecida!!')
        else:
            print(f'O banco de dados não foi encontrado ! {self.database_Connection.lastError().text()}')

    def create_user_Widgets(self):
        self.create_user_Label = QLabel("Novo Usuário:", self)
        self.create_user_Line = QLineEdit(self)
        self.create_user_password_Label = QLabel("Senha:", self)
        self.create_user_password_Line = QLineEdit(self)
        self.confirm_user_password_Label = QLabel("Confirmar Senha:", self)
        self.confirm_user_password_Line = QLineEdit(self)

    def create_user_Widgets_Settings(self):
        self.create_user_Line.setClearButtonEnabled(True)
        self.create_user_password_Line.setClearButtonEnabled(True)
        self.confirm_user_password_Line.setClearButtonEnabled(True)
        self.create_user_Line.setPlaceholderText("Inserir E-mail")
        self.create_user_password_Line.setPlaceholderText("Inserir Senha")
        self.confirm_user_password_Line.setPlaceholderText("Confirmar Senha")
        self.create_user_Line.setProperty('class', 'place_holder')
        self.create_user_Line.textEdited.connect(self.settings_Button)
        self.create_user_password_Line.setProperty('class', 'place_holder')
        self.confirm_user_password_Line.setProperty('class', 'place_holder')

    def create_user_Buttons(self):
        self.create_user_Button = QPushButton("Criar", self)
        self.create_user_Button.setProperty('class', 'settings_Buttons')
        self.create_user_Button.setEnabled(False)
        self.create_user_Button.clicked.connect(self.insert_New_User)


    def create_user_CheckBox(self):
        self.hidden_user_Password = QCheckBox("Mostrar Senha", self)
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

# Refatorar função
    def layout_Widget(self):
        self.layout_Horizontal_Box_Fist = QHBoxLayout()
        self.layout_Horizontal_Box_Second = QHBoxLayout()
        self.layout_Horizontal_Box_thirth = QHBoxLayout()
        self.layout_Vertical_Box = QVBoxLayout()
        self.layout_Horizontal_Box_Fist.addWidget(self.create_user_Label)
        self.layout_Horizontal_Box_Fist.addWidget(self.create_user_Line)
        self.layout_Horizontal_Box_Second.addWidget(self.create_user_password_Label)
        self.layout_Horizontal_Box_Second.addWidget(self.create_user_password_Line)
        self.layout_Horizontal_Box_thirth.addWidget(self.confirm_user_password_Label)
        self.layout_Horizontal_Box_thirth.addWidget(self.confirm_user_password_Line)
        self.layout_Vertical_Box.addLayout(self.layout_Horizontal_Box_Fist)
        self.layout_Vertical_Box.addLayout(self.layout_Horizontal_Box_Second)
        self.layout_Vertical_Box.addLayout(self.layout_Horizontal_Box_thirth)
        self.layout_Vertical_Box.addWidget(self.create_user_Button)
        self.layout_Vertical_Box.addWidget(self.hidden_user_Password)
        self.setLayout(self.layout_Vertical_Box)

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

