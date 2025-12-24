from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox, QMainWindow, QVBoxLayout, QHBoxLayout
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSize
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QBarSeries, QBarSet
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
        self.longin_interface_Buttons()
        self.login_interface_Widgets_Settings()
        self.login_interface_CheckBox()
        self.create_Account_Settings()
        self.settings_Enable_box_line()
        self.layout_Widgets()
        self.show()

    def base_Informations(self):
        self.database_Connection = QSqlDatabase.addDatabase('QSQLITE')
        self.database_Connection.setDatabaseName('customers_info')
        if self.database_Connection.open():
            print('Conexão estabelecida!!')
        else:
            print(f'O banco de dados não foi encontrado ! {self.database_Connection.lastError().text()}')

    def login_Interface_Widgets(self):
        self.user_Label = QLabel("Usuário:", self)
        self.user_Line = QLineEdit(self)
        self.password_user_Label = QLabel("Senha:", self)
        self.password_user_Line = QLineEdit(self)

    def login_interface_Widgets_Settings(self):
        self.user_Line.setPlaceholderText("E-mail Do usuário")
        self.password_user_Line.setPlaceholderText("Senha Do Usuário")
        self.user_Line.setClearButtonEnabled(True)
        self.password_user_Line.setClearButtonEnabled(True)
        self.user_Line.textEdited.connect(self.settings_Enable_box_line)
        self.password_user_Line.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_Line.setProperty('class', 'place_holder')
        self.password_user_Line.setProperty('class', 'place_holder')

    def longin_interface_Buttons(self):
        self.login_Button = QPushButton("Login", self)
        self.login_Button.setProperty('class', 'settings_Buttons')
        self.login_Button.clicked.connect(self.search_User)


    def login_interface_CheckBox(self):
        self.hidden_Password = QCheckBox("Monstrar Senha", self)
        self.hidden_Password.toggled.connect(self.settings_hidden_CheckBox)


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

#refatorar função
    def layout_Widgets(self):
        self.First_Horizontal_Layout_Box = QHBoxLayout()
        self.Second_Horizontal_Layout_Box = QHBoxLayout()
        self.Thirth_Horizontal_Layout_Box = QHBoxLayout()
        self.Vertical_Box = QVBoxLayout()
        self.First_Horizontal_Layout_Box.addWidget(self.user_Label)
        self.First_Horizontal_Layout_Box.addWidget(self.user_Line)
        self.Second_Horizontal_Layout_Box.addWidget(self.password_user_Label)
        self.Second_Horizontal_Layout_Box.addWidget(self.password_user_Line)
        self.Thirth_Horizontal_Layout_Box.addWidget(self.create_User_Label)
        self.Vertical_Box.addLayout(self.First_Horizontal_Layout_Box)
        self.Vertical_Box.addLayout(self.Second_Horizontal_Layout_Box)
        self.Vertical_Box.addWidget(self.login_Button)
        self.Vertical_Box.addWidget(self.hidden_Password)
        self.Vertical_Box.addLayout(self.Thirth_Horizontal_Layout_Box)
        self.Vertical_Box.addWidget(self.create_User_Button)
        self.setLayout(self.Vertical_Box)


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
        self.create_User_Label = QLabel("Não possui uma conta?", self)
        self.create_User_Button = QPushButton('Novo Usuário', self)
        self.create_User_Button.setProperty('class', 'settings_Buttons')
        self.create_User_Button.clicked.connect(self.send_newWindow)


    def send_newWindow(self, event):
        self.link_Class = New_User()
        self.link_Class.show()




# refatorar para uma script separado

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitializationUI()

    def InitializationUI(self):
        self.setGeometry(850, 850, 900, 900)
        self.setWindowTitle("Your finance")
        self.menu_Bar()
        self.charts_test_PieCHart()
        self.chart_teste_Bar()
        self.layout_charts()
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


    def charts_test_PieCHart(self):
        self.PieChart = QPieSeries()
        self.PieChart.append("Renda", 1459.85)
        self.PieChart.append("Gastos", 938.75)
        self.PieChart.append("Investimentos", 455.63)

        self.PieChart.setHoleSize(0.5)

        self.chart = QChart()
        self.chart.addSeries(self.PieChart)
        self.chart.setTitle('Resumo Mensal')
        self.chart.setMinimumSize(140, 140)
        self.chart.setMaximumSize(330,  330)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        self.chart.setAnimationOptions(QChart.AnimationOption.GridAxisAnimations)
        self.viewer_Chart = QChartView(self.chart)  


    def chart_teste_Bar(self):
        self.Janeiro = QBarSet("Janeiro")
        self.Fevereiro = QBarSet("Fevereiro")
        self.Marco = QBarSet("Março")

        self.Janeiro.append(328.78)
        self.Fevereiro.append(442.99)
        self.Marco.append(653.87)

        self.Bar_chart = QBarSeries()
        self.Bar_chart.append(self.Janeiro)
        self.Bar_chart.append(self.Fevereiro)
        self.Bar_chart.append(self.Marco)

        self.Shape_Chart = QChart()
        self.Shape_Chart.addSeries(self.Bar_chart)
        self.Shape_Chart.setTitle("Crescimento Financeiro")
        self.Shape_Chart.setMaximumSize(330, 330)

        self.represent_chart = QChartView(self.Shape_Chart)

    def layout_charts(self):
        Main_Layout_Windown = QWidget()
        self.setCentralWidget(Main_Layout_Windown)


        self.charts_Layout = QHBoxLayout()
        self.charts_Layout.addWidget(self.viewer_Chart)
        self.charts_Layout.addWidget(self.represent_chart)
        self.charts_Layout.setSpacing(1)
        self.charts_Layout.setContentsMargins(4, 4, 4, 4)
        Main_Layout_Windown.setLayout(self.charts_Layout)




if __name__ in "__main__":
    app = QApplication(sys.argv)
    program = Login()
    with open('style.css', 'r') as arquivo:
        style = arquivo.read()
        app.setStyleSheet(style)
    sys.exit(app.exec())
