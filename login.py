from PyQt6.QtWidgets import QDialog, QLabel,QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox
from PyQt6.QtGui import QPixmap, QIcon
from create_user import New_User

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initialization()


    def initialization(self):
        self.setFixedSize(350, 350)
        self.setWindowTitle('Login')
        self.login_widgets()
        self.login_widgets_settings()
        self.login_Widgets_layout()
        self.login_widgets_signals()
        self.block_login_button()
        self.show()

    def login_widgets(self):
        self.user_login_label = QLabel(self)
        self.user_login_line = QLineEdit(self)
        self.user_login_button = QPushButton('Login', self)
        self.password_user_label = QLabel(self)
        self.password_user_line = QLineEdit(self)
        self.create_newuser_button = QPushButton(self)
        self.check_password = QCheckBox('Mostrar senha', self)

    def login_widgets_settings(self):
        self.user_login_line.setProperty('class', 'QlineStyle')
        self.user_login_label.setPixmap(QPixmap('recursos/imagens/account_circle_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.png'))
        self.password_user_label.setPixmap(QPixmap('recursos/imagens/password_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.png'))
        self.create_newuser_button.setIcon(QIcon('recursos/imagens/person_add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png'))
        self.user_login_line.setPlaceholderText('Nome do usuário')
        self.password_user_line.setPlaceholderText('Senha do usuário')
        self.user_login_line.setClearButtonEnabled(True)
        self.password_user_line.setClearButtonEnabled(True)
        self.password_user_line.setEchoMode(QLineEdit.EchoMode.Password)

    def login_widgets_signals(self):
        self.user_login_line.textEdited.connect(self.block_login_button)
        self.check_password.toggled.connect(self.show_password)
        self.create_newuser_button.clicked.connect(self.new_user)


    def block_login_button(self):
        if self.user_login_line.text() != "":
            self.user_login_button.setEnabled(True)
        else:
            self.user_login_button.setEnabled(False)


    def show_password(self, check=None):
        if check:
            self.password_user_line.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_user_line.setEchoMode(QLineEdit.EchoMode.Password)


    def new_user(self):
        self.start_sesson = New_User()
        self.show()

    def login_Widgets_layout(self):

        self.login_layout = QHBoxLayout()
        self.password_layout= QHBoxLayout()
        self.main_layout = QVBoxLayout()

        self.login_layout.addWidget(self.user_login_label)
        self.login_layout.addWidget(self.user_login_line)
        self.password_layout.addWidget(self.password_user_label)
        self.password_layout.addWidget(self.password_user_line)
        self.main_layout.addLayout(self.login_layout)
        self.main_layout.addLayout(self.password_layout)
        self.main_layout.addWidget(self.check_password)
        self.main_layout.addWidget(self.user_login_button)
        self.main_layout.addWidget(self.create_newuser_button)

        self.setLayout(self.main_layout)

