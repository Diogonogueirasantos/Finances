from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon, QMovie, QFont
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
        self.createuser_Button = QPushButton('Create', self)
        self.createuser_Button.move(150, 250)
        self.createuser_Button.clicked.connect(self.create_User)


    def create_User(self):
        print('Olá, mundo!')
