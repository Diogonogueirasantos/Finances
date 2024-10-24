from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QMessageBox, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.InicializadorUI()

    def InicializadorUI(self):
        self.setGeometry(500, 500, 850, 850)
        self.setWindowTitle("Finance")
        self.setWindowIcon(QIcon("resources/images/window-maximize-solid.svg"))
        self.show()




if __name__ =="__main__":
    app = QApplication(sys.argv)
    Program = Window()
    app.exec()