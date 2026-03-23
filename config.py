from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class Config(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initialization()



    def initialization(self):
        self.setFixedSize(450, 450)
        self.setWindowTitle('Configurações')
        self.config_widgets()
        self.config_settings()
        self.config_styles()
        self.config_layout()
        self.show()


    def config_widgets(self):
        self.content_lang = QFrame()
        self.lang = QComboBox(self)
        self.lang_label = QLabel('Selecione o idioma', self)
        self.delete_account = QPushButton(self)
        self.reset_password = QPushButton(self)
        self.backup_account = QPushButton(self)
        self.api_config = QPushButton(self)



    def config_settings(self):
        languages = ['Português', 'Inglês', 'Japonês']
        self.lang.addItems(languages)
        self.delete_account.setFixedSize(250, 25)
        self.reset_password.setFixedSize(250, 25)
        self.backup_account.setFixedSize(250, 25)
        self.api_config.setFixedSize(250, 25)

        self.delete_account.setToolTip('Exluir Conta')
        self.reset_password.setToolTip('Redefinir Senha')
        self.backup_account.setToolTip('Backup')
        self.api_config.setToolTip('Incluir Chave API')


    def config_styles(self):
        self.delete_account.setIcon(QIcon('recursos/imagens/delete_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.reset_password.setIcon(QIcon('recursos/imagens/lock_reset_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.backup_account.setIcon(QIcon('recursos/imagens/backup_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.api_config.setIcon(QIcon('recursos/imagens/key_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))


        self.lang_label.setStyleSheet('color:#fff;')
        self.content_lang.setProperty('class', 'sidebar')
        self.content_lang.setFixedSize(350, 100)

        self.delete_account.setStyleSheet('QPushButton{background:#A60A17;} QPushButton:hover{background:#D92938;} QPushButton:pressed{background:#73020C;}')
        self.backup_account.setStyleSheet('QPushButton{background:#467326;} QPushButton:hover{background:#B2F252;} QPushButton:pressed{background:#79A637;}')



    def config_layout(self):
        self.main_layout = QVBoxLayout()
        self.micro_layout = QHBoxLayout(self.content_lang)
        self.micro_layout.addWidget(self.lang_label)
        self.micro_layout.addWidget(self.lang)
        self.main_layout.addWidget(self.content_lang, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.delete_account, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.reset_password, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.backup_account, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.api_config, alignment=Qt.AlignmentFlag.AlignCenter)


        self.setLayout(self.main_layout)

