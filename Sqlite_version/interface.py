from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSize
import sys

from novo_Usuario import New_User


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initializationUI()


    def initializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle('Login')
        self.login_Interface_Widgets()
        self.login_interface_Widgets_Positions()
        self.longin_interface_Buttons()
        self.login_interface_Widgets_Settings()
        self.login_interface_CheckBox()
        self.create_Account_Settings()
        self.show()

    def base_Informations(self):
        self.database_Connection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Connection.setDatabaseName('customers_info')
        if self.database_Connection.open():
            print('Conexão estabelecida!!')
        else:
            print(f'O banco de dados não foi encontrado ! {self.database_Connection.lastError().text()}')

    def login_Interface_Widgets(self):
        self.user_Label = QLabel("User:", self)
        self.user_Line = QLineEdit(self)
        self.password_user_Label = QLabel("Password:", self)
        self.password_user_Line = QLineEdit(self)

    def login_interface_Widgets_Positions(self):
        self.user_Label.move(85, 110)
        self.user_Line.move(130, 103)
        self.password_user_Label.move(55, 150)
        self.password_user_Line.move(133, 147)

    def login_interface_Widgets_Settings(self):
        self.user_Line.setPlaceholderText("Email user")
        self.password_user_Line.setPlaceholderText("User Password")
        self.user_Line.setClearButtonEnabled(True)
        self.password_user_Line.setClearButtonEnabled(True)
        self.user_Line.textEdited.connect(self.settings_Enable_box_line)
        self.password_user_Line.setEchoMode(QLineEdit.EchoMode.Password)

    def longin_interface_Buttons(self):
        self.login_Button = QPushButton("Login", self)
        self.login_Button.setProperty('class', 'settings_Buttons')
        self.login_Button.move(165, 200)
        self.login_Button.clicked.connect(self.search_User)


    def login_interface_CheckBox(self):
        self.hidden_Password = QCheckBox("Show Password", self)
        self.hidden_Password.toggled.connect(self.settings_hidden_CheckBox)
        self.hidden_Password.move(20, 200)


    def settings_hidden_CheckBox(self, checked=None):
        if checked:
            self.password_user_Line.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_user_Line.setEchoMode((QLineEdit.EchoMode.Password))

    def settings_Enable_box_line(self):
        if  self.user_Line.text() != "":
            self.login_Button.setEnabled(True)
        else:
            self.login_Button.setEnabled(False)

    def search_User(self):
        self.sql_cursor = QSqlQuery(self.base_Informations())
        sql_login_Query = "select email_client, password_client from customers_records where email_client=? and password_client=?;"
        self.sql_cursor.prepare(sql_login_Query)
        self.sql_cursor.bindValue(0, self.user_Line.text())
        self.sql_cursor.bindValue(1, self.password_user_Line.text())
        if self.sql_cursor.exec():
            if self.sql_cursor.next():
                QMessageBox.information(self, "Usuário encontrado!", f"seja bem-vindo(a) {self.user_Line.text()}",
                                        QMessageBox.StandardButton.Ok)
                self.linke = Main_Window()
                self.close()
            else:
                QMessageBox.question(self, "Usuário não encotrado!", """<p>Infelizmente não foi possíviel encontra o usuário!</p>
                        <p>Deseja tentar novamente?</p>""",
                                     QMessageBox.StandardButton.Yes | \
                                     QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.Yes)
        else:
            QMessageBox.information(self, "o processo falhou!", "iInfelizmente parece que o processo falhou",
                                    QMessageBox.StandardButton.Ok)




    def create_Account_Settings(self):
        self.create_User_Label = QLabel("Don't have a account?", self)
        self.create_User_Button = QPushButton('Create', self)
        self.create_User_Button.setProperty('class', 'settings_Buttons')
        self.create_User_Label.move(30, 280)
        self.create_User_Button.move(165, 315)
        self.create_User_Button.clicked.connect(self.send_newWindow)


    def send_newWindow(self, event):
        self.link_Class = New_User()
        self.link_Class.show()






class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitializationUI()

    def InitializationUI(self):
        self.setGeometry(850, 850, 900, 900)
        self.setWindowTitle("Your finance")
        self.menu_Bar()
        self.show()

    def menu_Bar(self):

        fechar_Programa = QAction('Sair', self)
        fechar_Programa.setShortcut('Ctrl+Q')
        fechar_Programa.setStatusTip('Encerrar programa')
        fechar_Programa.triggered.connect(self.close)

        main_Menu =  self.menuBar()
        main_Menu.setProperty('class', 'main_menu')
        investimentos = main_Menu.addMenu('Investimentos')
        renda = main_Menu.addMenu('Renda')
        extrato = main_Menu.addMenu('Extrato')
        cartoes = main_Menu.addMenu('Cartões')
        ajuda = main_Menu.addMenu('Ajuda')
        sair = main_Menu.addMenu("&Sair")
        sair.addAction(fechar_Programa)




if __name__ in "__main__":
    app = QApplication(sys.argv)
    program = Login()
    with open('style.css', 'r') as arquivo:
        style = arquivo.read()
        app.setStyleSheet(style)
    sys.exit(app.exec())
