from typing import Self

from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QFrame, QCheckBox, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class Cards(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initialization()



    def initialization(self):
        self.setBaseSize(800, 800)
        self.setWindowTitle('Cartões')
        self.cards_lots_containers()
        self.cards_lots_widgets()
        self.cards_lots_setting()
        self.cards_styles()
        self.cards_lots_containers_settings()
        self.cards_layout()
        self.show()


    def cards_lots_containers(self):
        self.slot_1 = QFrame()
        self.slot_2 = QFrame()
        self.slot_3 = QFrame()


    def cards_lots_widgets(self):
        self.card_box = QFrame()
        self.add_card = QPushButton(self)
        self.add_limit = QPushButton(self)
        self.delete_card = QPushButton(self)
        self.paycard = QPushButton(self)

        self.card_slot_1_flag = QLabel(self)
        self.card_slot_2_flag = QLabel(self)
        self.card_slot_3_flag = QLabel(self)

        self.card_slot_1_info = QLabel('8066', self)
        self.card_slot_2_info = QLabel('2542', self)
        self.card_slot_3_info = QLabel('3387', self)


    def cards_lots_setting(self):
        self.add_card.setFixedSize(50, 25)
        self.add_card.setIcon(QIcon('recursos/imagens/add_card_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))

        self.card_slot_1_flag.setPixmap(QPixmap('recursos/imagens/icons8-visa-73.png'))
        self.card_slot_2_flag.setPixmap(QPixmap('recursos/imagens/ma_symbol_opt_73_3x.png'))
        self.card_slot_3_flag.setPixmap(QPixmap('recursos/imagens/ma_symbol_opt_73_3x.png'))

        self.add_limit.setIcon(QIcon('recursos/imagens/credit_card_gear_32dp_FFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.delete_card.setIcon(QIcon('recursos/imagens/delete_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.paycard.setIcon(QIcon('recursos/imagens/payment_card_32dp_FFF_FILL0_wght400_GRAD0_opsz40.png'))

        self.add_card.setToolTip('Adicionar cartão')
        self.delete_card.setToolTip('Excluír Cartão')
        self.add_limit.setToolTip('Adicionar/Ajustar Limite')
        self.paycard.setToolTip('Pagar Fatura')

    def cards_styles(self):
        self.card_box.setProperty('class', 'sidebar')
        self.slot_1.setProperty('class', 'cards_contain')
        self.slot_2.setProperty('class', 'cards_contain')
        self.slot_3.setProperty('class', 'cards_contain')

    def cards_lots_containers_settings(self):
        self.slot_1.setFixedSize(520, 100)
        self.slot_2.setFixedSize(520, 100)
        self.slot_3.setFixedSize(520, 100)


    def cards_layout(self):
        self.main_container = QVBoxLayout()
        self.card_contain = QHBoxLayout(self.card_box)
        self.container_slot_1 = QHBoxLayout(self.slot_1)
        self.container_slot_2 = QHBoxLayout(self.slot_2)
        self.container_slot_3 = QHBoxLayout(self.slot_3)

        self.card_contain.addWidget(self.delete_card)
        self.card_contain.addWidget(self.add_limit)
        self.card_contain.addWidget(self.add_card)
        self.card_contain.addWidget(self.paycard)

        self.container_slot_1.addWidget(self.card_slot_1_flag)
        self.container_slot_1.addWidget(self.card_slot_1_info)

        self.container_slot_2.addWidget(self.card_slot_2_flag)
        self.container_slot_2.addWidget(self.card_slot_2_info)

        self.container_slot_3.addWidget(self.card_slot_3_flag)
        self.container_slot_3.addWidget(self.card_slot_3_info)

        self.main_container.addWidget(self.card_box, alignment=Qt.AlignmentFlag.AlignCenter)

        self.main_container.addWidget(self.slot_1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_container.addWidget(self.slot_2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_container.addWidget(self.slot_3, alignment=Qt.AlignmentFlag.AlignLeft)



        self.setLayout(self.main_container)

