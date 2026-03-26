from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QFrame, QComboBox, QHBoxLayout, QVBoxLayout, QDateEdit, QScrollArea, QDoubleSpinBox
from PyQt6.QtCore import Qt

class Gastos(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initialization()



    def initialization(self):
        self.setGeometry(850, 850, 850, 850)
        self.setWindowTitle('Gastos')
        self.costs_widgets()
        self.costs_widgets_settings()
        self.costs_widgets_styles()
        self.costs_widgets_layout()
        self.show()



    def costs_widgets(self):
        self.main_box_widgets = QFrame()
        self.sub_box_widgets = QFrame()
        self.costs_label = QLabel('Informar Gasto', self)
        self.category_cost_label = QLabel('Categoria', self)
        self.category_cost = QComboBox(self)
        self.costs_dspin = QDoubleSpinBox(self)
        self.payment_date = QDateEdit(self)
        self.confirm_payment = QPushButton('Confirmar', self)
        self.source_cost_label = QLabel('Origem', self)
        self.source_cost_line = QLineEdit(self)
        self.payment_way = QComboBox(self)
        self.payment_way_label = QLabel('Forma de pagamento', self)
        self.costs_info = QScrollArea(self)

    def up_side_bar(self):
        self.contain_bar = QFrame()
        self.resume = QPushButton(self)




    def costs_widgets_settings(self):
        categories = ['Mercado', 'Moradia', 'Itens para Casa', 'Lazer',
                      'Celular', 'Telefone', 'Educação', 'Água', 'Luz', 'Gás', 'Imprevistos',
                      'Farmácia', 'Convênio', 'Pets', 'Transporte', 'Mecânica']


        way_payment = ['Debito', 'Credito', 'Transferência', 'Pix', 'Dinheiro']

        self.category_cost.addItems(categories)

        self.payment_way.addItems(way_payment)

        self.costs_dspin.setRange(0, 999999.99)
        self.costs_dspin.setDecimals(2)
        self.costs_dspin.setPrefix('R$ ')
        self.payment_date.setCalendarPopup(True)
        self.sub_box_widgets.setFixedSize(650, 40)
        self.source_cost_line.setPlaceholderText('Informe o destinatário')
        self.source_cost_line.setClearButtonEnabled(True)

    def costs_widgets_styles(self):
        self.main_box_widgets.setProperty('class', 'sidebar')
        self.category_cost_label.setStyleSheet('color:#fff; max-width:90px;')
        self.costs_label.setStyleSheet('background:#fff; border-radius:7px; color:#000; max-width:120px;')
        self.sub_box_widgets.setProperty('class', 'sidebar')
        self.source_cost_label.setStyleSheet('color:#fff;')
        self.payment_way_label.setStyleSheet('color:#fff;')

    def costs_widgets_layout(self):
        self._main_layout = QVBoxLayout()
        self.box_layout = QHBoxLayout(self.main_box_widgets)
        self.box_layout.addWidget(self.costs_label)
        self.box_layout.addWidget(self.category_cost_label)
        self.box_layout.addWidget(self.category_cost)
        self.box_layout.addWidget(self.costs_dspin)
        self.box_layout.addWidget(self.payment_date)

        self.sub_box_layout = QHBoxLayout(self.sub_box_widgets)
        self.sub_box_layout.addWidget(self.source_cost_label)
        self.sub_box_layout.addWidget(self.source_cost_line)
        self.sub_box_layout.addWidget(self.payment_way_label)
        self.sub_box_layout.addWidget(self.payment_way)
        self.sub_box_layout.addWidget(self.confirm_payment)

        self._main_layout.addWidget(self.main_box_widgets)
        self._main_layout.addWidget(self.sub_box_widgets)
        self._main_layout.addWidget(self.costs_info)
        self.setLayout(self._main_layout)


    def up_side_bar(self):
        pass