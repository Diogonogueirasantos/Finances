from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtGui import QIcon, QMovie, QFont
from PyQt6.QtCore import QSize
import sys





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

    def User_Informations(self):
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
        self.sql_cursor = QSqlQuery(self.User_Informations())
        sql_login_Query = "select name, user_Password from Users where name=? and user_Password=?;"
        self.sql_cursor.prepare(sql_login_Query)
        self.sql_cursor.bindValue(0, self.user_Line.text())
        self.sql_cursor.bindValue(1, self.password_Line.text())
        if self.sql_cursor.exec():
            if self.sql_cursor.next():
                QMessageBox.information(self, "Usuário encontrado!", f"seja bem-vindo(a) {self.user_Line.text()}", QMessageBox.StandardButton.Ok)
                self.linke = Main_Window()

            else:
                QMessageBox.question(self, "Usuário não encotrado!", """<p>Infelizmente não foi possíviel encontra o usuário!</p>
                <p>Deseja tentar novamente?</p>""",
                    QMessageBox.StandardButton.Yes | \
                    QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.Yes)
        else:
            QMessageBox.information(self, "o processo falhou!", "iInfelizmente parece que o processo falhou", QMessageBox.StandardButton.Ok)

    def create_Account_Settings(self):
        self.create_User_Label = QLabel("Don't have a account?", self)
        self.create_User_Button = QPushButton('Create', self)
        self.create_User_Label.move(30, 280)
        self.create_User_Button.move(150, 315)
        self.create_User_Button.clicked.connect(self.send_newWindow)

    def send_newWindow(self):
        self.link_Class = New_User()

class New_User(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializationUI()

    def InitializationUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle("Create account")
        self.create_UserSettings()
        self.show()

    def User_Informations(self):
        self.database_Connection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Connection.setDatabaseName('Users.db')
        if self.database_Connection.open():
            self.create_User()

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
        self.createuser_Button.clicked.connect(self.User_Informations)


    def create_User(self):
        self.sql_Cursor = QSqlQuery(self.database_Connection)
        add_NewUser = "insert into (name, user_password) values(?, ?);"
        self.sql_Cursor.prepare(add_NewUser)
        self.sql_Cursor.bindValue(":name", self.createuser_Lineedit.text())
        self.sql_Cursor.bindValue("user_Password", self.createpassword_Lineedit.text())
        if self.sql_Cursor.exec():
            if self.sql_Cursor.next():
                self.database_Connection.commit()
                QMessageBox.information(self, 'Usuário cadastrado', 'seja muito bem-vindo(a)!', QMessageBox.StandardButton.Ok)



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
    app.exec()



