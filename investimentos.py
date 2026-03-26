from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QFrame, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt

class Investimentos(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initialization()


    def initialization(self):
        self.setGeometry(850, 850, 850, 850)
        self.setWindowTitle('Investimentos')
        self.show()


    def invests_widgets(self):
        pass


    def invests_widgets_settings(self):
        pass

    def invests_widgets_style(self):
        pass


    def invests_graphs(self):
        pass
