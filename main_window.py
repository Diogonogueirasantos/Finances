from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QGraphicsDropShadowEffect
from PyQt6.QtGui import QIcon, QPainter, QColor
from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QPieSeries, QBarSet
from PyQt6.QtCore import Qt
import sys
from login import Login
from cards import Cards
from config import Config
from renda import Renda
from gastos import Gastos
from investimentos import Investimentos



class main_App(QMainWindow):


    def __init__(self):
        super().__init__()
        self.initialization()


    def initialization(self):
        self.setGeometry(520, 520, 520, 520)
        self.setWindowTitle('Your Finance')
        self.left_barwidgets()
        self.left_barwidgets_settings()
        self.left_barwidgets_styles()
        self.left_barwidgets_layout()
        self.left_barwidgets_extra_styles()
        self.up_side_bar()
        self.up_side_bar_settings()
        self.up_side_bar_styles()
        self.up_side_bar_layout()
        self.up_sidebar_widgets_extra_styles()
        self.up_side_bar_signals()
        self.info_widgets()
        self.info_widgets_settings()
        self.info_widgets_styles()
        self.info_widgets_extra_styles()
        self.info_widgets_layout()
        self.info_widgets_signals()
        self.main_charts()
        self.main_charts_settings()
        self.pie_styles()
        self.main_layout_app()
        self.left_barwidgets_signals()
        self.show()



    def left_barwidgets(self):
        self.lateral_side_bar_contain = QFrame()
        self.cards = QPushButton(self)
        self.income = QPushButton(self)
        self.investments = QPushButton(self)
        self.costs = QPushButton(self)
        self.dollar_reserve = QPushButton(self)
        self.calendar = QPushButton(self)


    def left_barwidgets_settings(self):
        self.lateral_side_bar_contain.setFixedSize(60, 750)
        self.lateral_side_bar_contain.setContentsMargins(0, 10, 10, 10)
        self.lateral_side_bar_contain.setFrameShape(QFrame.Shape.StyledPanel)
        self.lateral_side_bar_contain.setFrameShadow(QFrame.Shadow.Raised)
        self.lateral_side_bar_contain.setProperty('class', 'sidebar')

        self.cards.setIcon(QIcon('recursos/imagens/credit_card_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.income.setIcon(QIcon('recursos/imagens/account_balance_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.investments.setIcon(QIcon('recursos/imagens/finance_mode_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.costs.setIcon(QIcon('recursos/imagens/paid_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.dollar_reserve.setIcon(QIcon('recursos/imagens/wallet_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.calendar.setIcon(QIcon('recursos/imagens/calendar_month_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))

    def left_barwidgets_styles(self):
        self.cards.setProperty('class', 'sidebar_buttons')
        self.income.setProperty('class', 'sidebar_buttons')
        self.investments.setProperty('class', 'sidebar_buttons'),
        self.costs.setProperty('class', 'sidebar_buttons')
        self.dollar_reserve.setProperty('class', 'sidebar_buttons')
        self.calendar.setProperty('class', 'sidebar_buttons')
        self.cards.setToolTip('Cartões')
        self.income.setToolTip('Renda')
        self.investments.setToolTip('Investimentos'),
        self.costs.setToolTip('Pagamentos'),
        self.calendar.setToolTip('Calendário')
        self.dollar_reserve.setToolTip('Carteira')

    def left_barwidgets_layout(self):
        self.left_sidebar = QVBoxLayout(self.lateral_side_bar_contain)
        self.left_sidebar.addWidget(self.cards)
        self.left_sidebar.addWidget(self.income)
        self.left_sidebar.addWidget(self.investments)
        self.left_sidebar.addWidget(self.costs)
        self.left_sidebar.addWidget(self.calendar)
        self.left_sidebar.addWidget(self.dollar_reserve)

    def left_barwidgets_extra_styles(self):
        self.left_extra_style = QGraphicsDropShadowEffect()
        self.left_extra_style.setBlurRadius(30)
        self.left_extra_style.setXOffset(5)
        self.left_extra_style.setYOffset(5)
        self.left_extra_style.setColor(QColor(0, 0, 0))
        self.lateral_side_bar_contain.setGraphicsEffect(self.left_extra_style)


    def left_barwidgets_signals(self):
        self.cards.clicked.connect(self.cards_window)
        self.income.clicked.connect(self.renda_window)
        self.costs.clicked.connect(self.gastos_window)
        self.investments.clicked.connect(self.investimentos_window)

    def main_charts(self):
        self.resume_month_pie = QPieSeries()
        self.format_charts_pie = QChart()
        self.visualization_pie = QChartView()
        self.resume_investiments = QBarSeries()
        self.format_charts_bar = QChart()
        self.visualization_bar = QChartView()

# refatorar esta função
    def main_charts_settings(self):
        self.resume_month_pie.setHoleSize(0.5)
        self.resume_month_pie.append('Gastos', 1345.77)
        self.resume_month_pie.append('Renda', 2789.89)
        self.resume_month_pie.append('Investimentos', 500)
        self.resume_month_pie.slices()[0].setExploded()
        self.resume_month_pie.append("temp", 0)
        self.resume_month_pie.remove(self.resume_month_pie.slices()[-1])



        self.mes_janeiro = QBarSet('Janeiro')
        self.mes_fevereiro = QBarSet('Fevereiro')
        self.mes_marco = QBarSet('Março')

        self.mes_janeiro << 235
        self.mes_fevereiro << 344
        self.mes_marco << 380

        self.resume_investiments.append(self.mes_janeiro)
        self.resume_investiments.append(self.mes_fevereiro)
        self.resume_investiments.append(self.mes_marco)

        self.format_charts_bar.addSeries(self.resume_investiments)
        self.visualization_bar.setChart(self.format_charts_bar)

        self.format_charts_pie.addSeries(self.resume_month_pie)
        self.format_charts_pie.setTitle('Resumo Mensal')
        self.format_charts_pie.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        self.visualization_pie.setChart(self.format_charts_pie)
        self.visualization_pie.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.visualization_pie.setFixedSize(450, 450)
        self.visualization_bar.setFixedSize(450, 450)
        self.resume_month_pie.hovered.connect(self.pie_effects)

    def pie_styles(self):
        self.visualization_pie.setProperty('class', 'pie_style')
        self.visualization_bar.setProperty('class', 'bar_style')

    def pie_effects(self, slice, state):
        slice.setExploded(state)
        slice.setLabelVisible(state)
        if state:
            slice.setBorderWidth(2)
        else:
            slice.setBorderWidth(1)


        for slice in self.resume_month_pie.slices():
            slice.setLabelVisible(True)
            slice.setLabel(f'R${slice.value():.2f} ')


    def up_side_bar(self):
        self.up_contain = QFrame()
        self.logout_button = QPushButton(self)
        self.config_button = QPushButton(self)
        self.theme_button = QCheckBox(self)
        self.login_button = QPushButton(self)

    def up_side_bar_settings(self):
        self.up_contain.setFixedSize(500, 60)
        self.logout_button.setIcon(QIcon('recursos/imagens/logout_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.config_button.setIcon(QIcon('recursos/imagens/settings_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.theme_button.setIcon(QIcon('recursos/imagens/dark_mode_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.login_button.setIcon(QIcon('recursos/imagens/account_circle_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.logout_button.setToolTip('Sair')
        self.config_button.setToolTip('Configurações')
        self.theme_button.setToolTip('Escuro/Claro')
        self.login_button.setToolTip('Login Usuário')


    def up_side_bar_styles(self):
        self.up_contain.setProperty('class', 'sidebar')
        self.logout_button.setProperty('class', 'sidebar_buttons')
        self.config_button.setProperty('class', 'sidebar_buttons')
        self.theme_button.setProperty('class', 'sidebar_buttons')
        self.login_button.setProperty('class', 'sidebar_buttons')


    def up_sidebar_widgets_extra_styles(self):
        self.up_sidebar_extra_styles = QGraphicsDropShadowEffect()
        self.up_sidebar_extra_styles.setBlurRadius(30)
        self.up_sidebar_extra_styles.setXOffset(5)
        self.up_sidebar_extra_styles.setYOffset(5)
        self.up_sidebar_extra_styles.setColor(QColor(0, 0, 0))
        self.up_contain.setGraphicsEffect(self.up_sidebar_extra_styles)

    def up_side_bar_layout(self):
        self.up_bar_layout = QHBoxLayout(self.up_contain)
        self.up_bar_layout.addWidget(self.theme_button)
        self.up_bar_layout.addWidget(self.config_button)
        self.up_bar_layout.addWidget(self.login_button)
        self.up_bar_layout.addWidget(self.logout_button)



    def up_side_bar_signals(self):
        self.logout_button.clicked.connect(self.logout_system)
        self.theme_button.toggled.connect(self.theme_set)
        self.login_button.clicked.connect(self.log_user)
        self.config_button.clicked.connect(self.config_window)



    def info_widgets(self):
        self.info_contain = QFrame()
        self.show_money_box = QCheckBox(self)
        self.show_money_line = QLineEdit(self)
        self.identifier_money = QLabel('R$', self)

    def info_widgets_settings(self):
        self.info_contain.setFixedSize(320, 60)
        self.show_money_box.setIcon(QIcon('recursos/imagens/visibility_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png'))
        self.show_money_line.setReadOnly(True)
        self.show_money_line.setText('1250.89')
        self.show_money_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.show_money_box.setToolTip('Enxergar/Ocultar')

    def info_widgets_styles(self):
        self.info_contain.setProperty('class', 'sidebar')
        self.show_money_box.setProperty('class', 'laretal_sidebar_buttons')
        self.show_money_box.setProperty('class', 'sidebar_buttons')
        self.show_money_line.setProperty('class', 'money_display')
        self.identifier_money.setProperty('class', 'identifier_money')

    def info_widgets_extra_styles(self):
        self.info_extra_styles = QGraphicsDropShadowEffect()
        self.info_extra_styles.setBlurRadius(30)
        self.info_extra_styles.setXOffset(5)
        self.info_extra_styles.setYOffset(5)
        self.info_extra_styles.setColor(QColor(0, 0, 0))
        self.info_contain.setGraphicsEffect(self.info_extra_styles)


    def info_widgets_layout(self):
        self.info_layout = QHBoxLayout(self.info_contain)
        self.info_layout.addWidget(self.show_money_box)
        self.info_layout.addWidget(self.identifier_money)
        self.info_layout.addWidget(self.show_money_line)


    def info_widgets_signals(self):
       self.show_money_box.toggled.connect(self.display_money_info)


    def main_layout_app(self):
        self.main_layout = QWidget()
        self.setCentralWidget(self.main_layout)
        self.subcontain = QHBoxLayout()
        self.main_contain = QVBoxLayout(self.main_layout)


        self.subcontain.addWidget(self.lateral_side_bar_contain)
        self.subcontain.addWidget(self.visualization_pie)
        self.subcontain.addWidget(self.visualization_bar)

        self.main_contain.addWidget(self.up_contain, alignment=Qt.AlignmentFlag.AlignRight)
        self.main_contain.addWidget(self.info_contain, alignment=Qt.AlignmentFlag.AlignRight)
        self.main_contain.addLayout(self.subcontain)


    def display_money_info(self, check=None):
        if check:
            self.show_money_line.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.show_money_line.setEchoMode(QLineEdit.EchoMode.Password)


    def theme_set(self, check=None):
        if check:
            with open('/home/dns/git_projects/Finances/dark.css', 'r') as dark_theme:
                set_dark_theme = dark_theme.read()

            app.setStyleSheet(set_dark_theme)
            self.format_charts_pie.setTheme(QChart.ChartTheme.ChartThemeDark)
            self.format_charts_bar.setTheme(QChart.ChartTheme.ChartThemeDark)

        else:
            with open('/home/dns/git_projects/Finances/light.css', 'r') as light_theme:
                set_light_theme = light_theme.read()
            app.setStyleSheet(set_light_theme)
            self.format_charts_pie.setTheme(QChart.ChartTheme.ChartThemeLight)
            self.format_charts_bar.setTheme(QChart.ChartTheme.ChartThemeLight)


    def logout_system(self):
        self.close()

    def log_user(self):
        self.start_sesson_login = Login()
        self.start_sesson_login.show()

    def cards_window(self):
        self.start_sesson_cards = Cards()
        self.start_sesson_cards.show()


    def config_window(self):
        self.start_sesson_config = Config()
        self.show()


    def renda_window(self):
        self.start_sesson_renda = Renda()
        self.start_sesson_renda.show()


    def gastos_window(self):
        self.start_Sesson_gastos = Gastos()
        self.start_Sesson_gastos.show()


    def investimentos_window(self):
        self.start_sesson_investimentos = Investimentos()
        self.start_sesson_investimentos.show()


if __name__ in '__main__':
    app = QApplication(sys.argv)
    with open('/home/dns/git_projects/Finances/light.css', 'r') as light_theme:
        sheets_Styles = light_theme.read()
    program = main_App()
    app.setStyleSheet(sheets_Styles)
    app.exit(app.exec())