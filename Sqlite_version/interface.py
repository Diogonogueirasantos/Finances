from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtGui import QIcon, QMovie, QFont
from PyQt6.QtCore import QSize
import sys
from novo_Usuario import New_User
from database_Manager import users_Informations



class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initializationUI()

        with open('style.css', 'r') as load_file:
            FormatationonPyqt6 = load_file.read()
            self.setStyleSheet(FormatationonPyqt6)


    def initializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle('Login')
        self.login_Settings()
        self.create_Account_Settings()
        self.show()

    def login_Settings(self):
        self.user_Animation = QMovie('images/do-utilizador.gif')
        self.password_Animation = QMovie('images/cadeado.gif')
        self.user_Label = QLabel(self)
        self.password_Label = QLabel(self)
        self.user_Label.setMovie(self.user_Animation)
        self.password_Label.setMovie(self.password_Animation)
        self.user_Animation.setScaledSize(QSize(30, 30))
        self.password_Animation.setScaledSize(QSize(30, 30))
        self.user_Animation.start()
        self.password_Animation.start()
        self.user_Line = QLineEdit(self)
        self.password_Line = QLineEdit(self)
        self.hidden_password = QCheckBox('Show Password', self)
        self.user_Botton = QPushButton('Login', self)
        self.user_Label.move(100, 100)
        self.password_Label.move(97, 150)
        self.user_Line.move(130, 103)
        self.password_Line.move(133, 150)
        self.hidden_password.move(95, 195)
        self.user_Botton.move(155, 230)
        self.user_Line.setPlaceholderText('User name')
        self.password_Line.setPlaceholderText('Password')
        self.password_Line.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_Botton.clicked.connect(self.search_User)
        self.hidden_password.toggled.connect(self.settings_box_lineedit)


    def settings_box_lineedit(self, checked):
        if checked:
            self.password_Line.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_Line.setEchoMode((QLineEdit.EchoMode.Password))


    def search_User(self):
        self.link_Database = users_Informations()
        self.link_Database.search_record(self.user_Line.text(), self.password_Line.text())

    def create_Account_Settings(self):
        self.create_User_Label = QLabel("Don't have a account?", self)
        self.create_User_Button = QPushButton('Create', self)
        self.create_User_Label.move(30, 280)
        self.create_User_Button.move(150, 315)
        self.create_User_Button.clicked.connect(self.send_newWindow)

    def send_newWindow(self):
        self.link_Class = New_User()
        self.link_Class.show()





class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializationUI()

    def InitializationUI(self):
        self.setGeometry(850, 850, 900, 900)
        self.setWindowTitle("Your finance")
        self.show()

if __name__ in "__main__":
    app = QApplication(sys.argv)
    program = Login()
    app.styleSheet()
    app.exec()





