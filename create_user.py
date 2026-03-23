from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QCheckBox, QMessageBox,QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap

class New_User(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initializationUI()

    def initializationUI(self):
        self.setFixedSize(350, 350)
        self.setWindowTitle('Novo Usuário')
        self.create_user_widgets()
        self.create_user_layout()
        self.create_user_widgets_settings()
        self.create_user_widgets_signals()
        self.show()


    def create_user_widgets(self):
        self.create_user_label = QLabel(self)
        self.create_user_line = QLineEdit(self)
        self.create_password_label = QLabel(self)
        self.create_password_line = QLineEdit(self)
        self.confirm_password_label = QLabel(self)
        self.confirm_password_line = QLineEdit(self)
        self.create_user_button = QPushButton('Criar', self)
        self.check_password = QCheckBox('Mostrar senha', self)

    def create_user_widgets_settings(self):
        self.create_user_label.setPixmap(QPixmap('recursos/imagens/account_circle_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.png'))
        self.create_password_label.setPixmap(QPixmap('recursos/imagens/password_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.png'))
        self.confirm_password_label.setPixmap(QPixmap('recursos/imagens/password_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.png'))
        self.create_user_line.setPlaceholderText('Nome do Usuário')
        self.create_password_line.setPlaceholderText('Insira sua senha')
        self.confirm_password_line.setPlaceholderText('Confirme a sua senha')
        self.create_user_line.setClearButtonEnabled(True)
        self.create_password_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.create_password_line.setClearButtonEnabled(True)
        self.confirm_password_line.setClearButtonEnabled(True)

        self.create_user_button.setEnabled(False)

    def create_user_widgets_signals(self):
        self.create_user_line.textEdited.connect(self.block_button_create)
        self.check_password.toggled.connect(self.show_password)


    def block_button_create(self):
        if self.create_user_line.text() != "":
            self.create_user_button.setEnabled(True)
        else:
            self.create_user_button.setEnabled(False)

    def show_password(self, check=None):
        if check:
            self.create_password_line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirm_password_line.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.create_password_line.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirm_password_line.setEchoMode(QLineEdit.EchoMode.Password)

    def create_user_layout(self):
        self.user_name_layout = QHBoxLayout()
        self.password_layout = QHBoxLayout()
        self.confirm_password_layout = QHBoxLayout()
        self.main_layout = QVBoxLayout()

        self.user_name_layout.addWidget(self.create_user_label)
        self.user_name_layout.addWidget(self.create_user_line)
        self.password_layout.addWidget(self.create_password_label)
        self.password_layout.addWidget(self.create_password_line)
        self.confirm_password_layout.addWidget(self.confirm_password_label)
        self.confirm_password_layout.addWidget(self.confirm_password_line)
        self.main_layout.addLayout(self.user_name_layout)
        self.main_layout.addLayout(self.password_layout)
        self.main_layout.addLayout(self.confirm_password_layout)
        self.main_layout.addWidget(self.check_password)
        self.main_layout.addWidget(self.create_user_button)

        self.setLayout(self.main_layout)

