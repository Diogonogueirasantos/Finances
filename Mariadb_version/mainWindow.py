from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QMessageBox, QPushButton
from PyQt6.QtGui import QIcon
import sys
import Interface

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializationUI()

    def InitializationUI(self):
        self.setGeometry(500, 500, 750, 750)
        self.setWindowTitle('Your Finances')
        self.setWindowIcon(QIcon('resources/images/casa.png'))
        self.text()
        self.show()

    def text(self):
        self.cursor = Interface.Login()
        self.nome = self.cursor.login_Lineedit.text()
        self.texto = QLabel(f'Olá, {self.nome()}!', self)

