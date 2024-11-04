from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QCheckBox, QMessageBox, QPushButton, QWidget
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys

class login_User(QWidget):
    def __init__(self):
        super().__init__()
        self.InicializacaoUI()

    def InicializacaoUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle('Login User')
        self.setWindowIcon(QIcon('images/do-utilizador.png'))
        self.login_Widgets()
        self.createUsers_Widgets()
        self.show()

    def login_Widgets(self):
        self.login_Label = QLabel('Login:', self)
        self.login_Lineedit = QLineEdit(self)
        self.login_Botton = QPushButton('Login', self)
        self.password_Label = QLabel('Password:', self)
        self.password_Lineedit = QLineEdit(self)
        self.password_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_Hidden = QCheckBox('Show Password', self)
        self.login_Label.move(80, 100)
        self.login_Lineedit.move(123, 97)
        self.password_Label.move(50, 129)
        self.password_Lineedit.move(123, 127)
        self.password_Hidden.move(60, 159)
        self.login_Botton.move(140, 199)
        self.password_Hidden.toggled.connect(self.hidden_Password)

    def createUsers_Widgets(self):
        self.createUser_Label = QLabel('Dont have an account?', self)
        self.createUser_Label.move(0, 240)
        self.createUser_Botton = QPushButton('Create', self)
        self.createUser_Botton.move(140, 280)
        self.createUser_Botton.clicked.connect(self.create_UserWindow)

    def create_UserWindow(self): #Renomear quando possível
        self.createUser = Create_User()

    def hidden_Password(self, cliked):
        if cliked:
            self.password_Lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif cliked == False:
            self.password_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)



class Create_User(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializationUI()

    def InitializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle('Create User')
        self.setWindowIcon(QIcon('images/do-utilizador.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = login_User()
    app.exec()