from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QDoubleSpinBox, QComboBox, QMessageBox, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea, QDateEdit, QTableView
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
        self.sub_box_widgets = QFrame()
        self.income_label = QLabel('Informar Renda')
        self.type_income = QComboBox(self)
        self.salary = QDoubleSpinBox(self)
        self.receive_date = QDateEdit(self)
        self.source_income_label = QLabel('Origem')
        self.source_income_line = QLineEdit(self)
        self.confirm_income = QPushButton('Confirmar', self)

        self.info_income = QTableView()


    def income_settings(self):
        types_income = ['Renda Fixa', 'Renda Variável', 'Renda Extra']
        self.type_income.addItems(types_income)
        self.salary.setRange(0, 999999.99)
        self.salary.setDecimals(2)
        self.salary.setPrefix('R$ ')
        self.receive_date.setCalendarPopup(True)
        self.source_income_label.setStyleSheet('color:#fff;')
        self.source_income_line.setPlaceholderText('Informe a Origem da Renda')


    def income_style(self):
        self.box_widgets.setProperty('class', 'sidebar')
        self.sub_box_widgets.setProperty('class', 'sidebar')
        self.sub_box_widgets.setFixedSize(380, 50)
        self.type_income.setStyleSheet('border-radius:7px;')
        self.receive_date.setStyleSheet('border-radius:7px;')
        self.income_label.setStyleSheet('color:#fff;')


    def income_layout(self):
        self.main_layout = QVBoxLayout()
        self.add_income_layout = QHBoxLayout(self.box_widgets)
        self.sub_box_layout = QHBoxLayout(self.sub_box_widgets)
        self.add_income_layout.addWidget(self.income_label)
        self.add_income_layout.addWidget(self.type_income)
        self.add_income_layout.addWidget(self.salary)
        self.add_income_layout.addWidget(self.receive_date)

        self.sub_box_layout.addWidget(self.source_income_label)
        self.sub_box_layout.addWidget(self.source_income_line)
        self.sub_box_layout.addWidget(self.confirm_income)

        self.main_layout.addWidget(self.box_widgets)
        self.main_layout.addWidget(self.sub_box_widgets)
        self.main_layout.addWidget(self.info_income)

        self.setLayout(self.main_layout)

    def income_signals(self):
        self.confirm_income.clicked.connect(self.teste)

    def teste(self):
        data_selecionada = self.receive_date.date().toPyDate()
        print(data_selecionada)