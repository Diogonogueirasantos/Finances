from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox, QHBoxLayout, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtGui import QIcon, QMovie, QFont, QPixmap, QAction
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
        self.login_Settings()
        self.create_Account_Settings()
        self.show()

    def base_Informations(self):
        self.database_Connection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Connection.setDatabaseName('Users.db')
        if self.database_Connection.open():
            print('Conexão estabelecida!!')
        else:
            print(f'O banco de dados não foi encontrado ! {self.database_Connection.lastError().text()}')

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
        self.user_Line.setClearButtonEnabled(True)
        self.password_Line = QLineEdit(self)
        self.password_Line.setClearButtonEnabled(True)
        self.hidden_password = QCheckBox('Show Password', self)
        self.user_Botton = QPushButton('Login', self)
        self.user_Botton.setProperty('class', 'settings_Buttons')
        self.user_Botton.setEnabled(False)
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
        self.hidden_password.toggled.connect(self.settings_hidden_check_box)
        self.user_Line.textEdited.connect(self.settings_Enable_box_line)



    def settings_hidden_check_box(self, checked):
        if checked:
            self.password_Line.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_Line.setEchoMode((QLineEdit.EchoMode.Password))

    def settings_Enable_box_line(self):
        if  self.user_Line.text() != "":
            self.user_Botton.setEnabled(True)
        else:
            self.user_Botton.setEnabled(False)

    def search_User(self):
        self.sql_cursor = QSqlQuery(self.base_Informations())
        sql_login_Query = "select name, user_Password from Users where name=? and user_Password=?;"
        self.sql_cursor.prepare(sql_login_Query)
        self.sql_cursor.bindValue(0, self.user_Line.text())
        self.sql_cursor.bindValue(1, self.password_Line.text())
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
        self.create_User_Button.move(150, 315)
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





