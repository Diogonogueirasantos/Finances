from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QMessageBox, QPushButton, QCheckBox, QMenu
from PyQt6.QtGui import QIcon
import sys
import Database


import mainWindow
import Database


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.InicializadorUI()

    def InicializadorUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("resources/images/do-utilizador.png"))
        self.login_Settings()
        self.createuser_Settings()
        self.show()

    def login_Settings(self):
        self.login_Label = QLabel('Login:', self)
        self.login_Lineedit = QLineEdit(self)
        self.password_Label = QLabel('Password: ', self)
        self.password_Lineedit = QLineEdit(self)
        self.password_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_Hidden = QCheckBox('Show Password', self)
        self.login_Botton = QPushButton('Login', self)
        self.login_Label.move(100, 100)
        self.login_Lineedit.move(145, 95)
        self.password_Label.move(75, 130)
        self.password_Lineedit.move(145, 127)
        self.password_Hidden.move(75, 160)
        self.login_Botton.move(155, 200)
        self.password_Hidden.toggled.connect(self.checkhidden_Password)
        self.login_Botton.clicked.connect(self.link_MainWindow)

    def checkhidden_Password(self, cliked):
        if cliked:
            self.password_Lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif cliked == False:
            self.password_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)

    def createuser_Settings(self):
        self.createuser_Label = QLabel("Don't hava an account?", self)
        self.createuser_Botton = QPushButton('Create', self)
        self.createuser_Label.move(30, 250)
        self.createuser_Botton.move(155, 280)
        self.createuser_Botton.clicked.connect(self.link_createAccount)

    def link_MainWindow(self):
        self.ponte = MainWindow()


    def link_createAccount(self):
        self.linkcreate_User = create_Account()

class create_Account(QWidget):
    def __init__(self):
        super().__init__()
        self.initializationUI()

    def initializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowIcon(QIcon('resources/images/do-utilizador.png'))
        self.setWindowTitle('Create User')
        self.createuser_Widgets()
        self.show()

    def createuser_Widgets(self):
        self.createuser_Label = QLabel('Create:', self)
        self.createuser_Linnedit = QLineEdit(self)
        self.createpassworduser_Label = QLabel('Password:', self)
        self.createpassworduser_Lineedit = QLineEdit(self)
        self.createpassworduser_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmpassworduser_Label = QLabel('Confirm Password:', self)
        self.confirmpassworduser_Lineedit = QLineEdit(self)
        self.confirmpassworduser_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.hidden_Passaword = QCheckBox('Show Passwors', self)
        self.createuser_Botton = QPushButton('Create', self)
        self.createuser_Label.move(100, 100)
        self.createuser_Linnedit.move(150,95)
        self.createpassworduser_Label.move(80, 135)
        self.createpassworduser_Lineedit.move(150, 130)
        self.confirmpassworduser_Label.move(23, 167)
        self.confirmpassworduser_Lineedit.move(150, 165)
        self.createuser_Botton.move(150, 255)
        self.hidden_Passaword.move(50, 200)
        self.hidden_Passaword.toggled.connect(self.password_Box)
        self.createuser_Botton.clicked.connect(self.Insert_Values)

    def password_Box(self, cliked):
        if cliked:
            self.createpassworduser_Lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirmpassworduser_Lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif not cliked:
            self.createpassworduser_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirmpassworduser_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)


    def Insert_Values(self):
        self.connection = Database.Database_manager
        print(self.connection.cursor.execute('select name from Users where id_user = 3;'))
        self.connection.cursor.fetchall()




class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializationUI()

    def initializationUI(self):
        self.setGeometry(500, 500, 750, 750)
        self.setWindowTitle('Your Finance')
        self.setWindowIcon(QIcon('resources/images/casa.png'))
        self.tools_Bar()
        self.show()

    def tools_Bar(self):
        self.ferramentas = QMenu('ferramentas', self)
        self.ferramentas.addMenu(self.ferramentas)




if __name__ =="__main__":
    app = QApplication(sys.argv)
    Program = Login()
    app.exec()