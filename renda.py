from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea, QDateEdit, QTableView,
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class Renda(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initialization()




    def initialization(self):
        self.setGeometry(850, 850, 850, 850)
        self.setWindowTitle('Renda')
        self.income_widgets()
        self.income_settings()
        self.income_style()
        self.income_layout()
        self.income_signals()
        self.show()


    def income_widgets(self):
        self.box_widgets = QFrame()
        self.type_income = QComboBox(self)
        self.salary = QLineEdit(self)
        self.receive_date = QDateEdit(self)
        self.confirm_income = QPushButton('Confirmar', self)

        self.info_income = QTextTableFormat()


    def income_settings(self):
        self.box_widgets.setFixedSize(850, 100)
        types_income = ['Renda Fixa', 'Renda Variável', 'Renda Extra']
        self.type_income.addItems(types_income)
        self.salary.setPlaceholderText('Informe o valor da renda com duas casas decimais')
        self.receive_date.setCalendarPopup(True)


    def income_style(self):
        self.box_widgets.setProperty('class', 'sidebar')
        self.type_income.setStyleSheet('border-radius:7px;')
        self.receive_date.setStyleSheet('border-radius:7px;')


    def income_layout(self):
        self.main_layout = QVBoxLayout()
        self.add_income_layout = QHBoxLayout(self.box_widgets)

        self.add_income_layout.addWidget(self.type_income)
        self.add_income_layout.addWidget(self.salary)
        self.add_income_layout.addWidget(self.receive_date)
        self.add_income_layout.addWidget(self.confirm_income)

        self.main_layout.addWidget(self.box_widgets)
        self.main_layout.addWidget(self.info_income)

        self.setLayout(self.main_layout)

    def income_signals(self):
        self.confirm_income.clicked.connect(self.teste)

    def teste(self):
        data_selecionada = self.receive_date.date().toPyDate()
        print(data_selecionada)