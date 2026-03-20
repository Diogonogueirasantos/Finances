from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QPainter
from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QPieSeries, QBarSet
import sys
from login import Login



class main_App(QMainWindow):


    def __init__(self):
        super().__init__()
        self.InitializationUI()


    def InitializationUI(self):
        self.setFixedSize(1200, 1200)
        self.setWindowTitle('Your Finance')
        self.log_User()
        self.left_barWidgets()
        self.left_barWidgets_Settings()
        self.left_barWidgets_Layout()
        self.main_charts()
        self.main_charts_settings()
        self.main_layout_app()
        self.info_Widgets()
        self.info_Widgets_Settings()
        self.info_Widgets_Layout()
        self.show()



    def left_barWidgets(self):
        self.lateral_side_bar_contain = QFrame()
        self.cards = QPushButton(self)
        self.income = QPushButton(self)
        self.investments = QPushButton(self)
        self.costs = QPushButton(self)
        self.dollar_reserve = QPushButton(self)



    def left_barWidgets_Settings(self):
        self.lateral_side_bar_contain.setFixedSize(60, 900)
        self.lateral_side_bar_contain.setContentsMargins(10, 10, 10, 10)
        self.lateral_side_bar_contain.setFrameShape(QFrame.Shape.StyledPanel)
        self.lateral_side_bar_contain.setFrameShadow(QFrame.Shadow.Raised)
        self.lateral_side_bar_contain.setProperty('class', 'lateral_sidebar')
        self.cards.setIcon(QIcon('recursos/imagens/credit_card_26dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png'))
        self.income.setIcon(QIcon('recursos/imagens/money_bag_26dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png'))
        self.investments.setIcon(QIcon('recursos/imagens/finance_26dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png'))
        self.costs.setIcon(QIcon('recursos/imagens/payments_26dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png'))
        self.dollar_reserve.setIcon(QIcon('recursos/imagens/wallet_26dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png'))
        self.cards.setProperty('class', 'laretal_sidebar_buttons')
        self.income.setProperty('class', 'laretal_sidebar_buttons')
        self.investments.setProperty('class', 'laretal_sidebar_buttons'),
        self.costs.setProperty('class', 'laretal_sidebar_buttons')
        self.dollar_reserve.setProperty('class', 'laretal_sidebar_buttons')

    def left_barWidgets_Layout(self):
        self.left_sidebar = QVBoxLayout(self.lateral_side_bar_contain)
        self.left_sidebar.addWidget(self.cards)
        self.left_sidebar.addWidget(self.income)
        self.left_sidebar.addWidget(self.investments)
        self.left_sidebar.addWidget(self.costs)
        self.left_sidebar.addWidget(self.dollar_reserve)

    def main_charts(self):
        self.resume_month_pie = QPieSeries()
        self.format_charts_pie = QChart()
        self.visualization_pie = QChartView()
        self.resume_investiments = QBarSeries()
        self.format_charts_bar = QChart()
        self.visualization_bar = QChartView()
    def main_charts_settings(self):
        self.resume_month_pie.append('Gastos', 1345.77)
        self.resume_month_pie.append('Renda', 2789.89)
        self.resume_month_pie.append('Investimentos', 500)
        self.resume_month_pie.slices()[0].setExploded()


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
        self.format_charts_pie.createDefaultAxes()
        self.format_charts_pie.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        self.visualization_pie.setChart(self.format_charts_pie)
        self.visualization_pie.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.visualization_pie.setFixedSize(450, 450)
        self.visualization_bar.setFixedSize(450, 450)


    def main_layout_app(self):
        self.main_layout = QWidget()
        self.setCentralWidget(self.main_layout)
        self.main_contain = QHBoxLayout(self.main_layout)
        self.main_contain.addWidget(self.lateral_side_bar_contain)
        self.main_contain.addWidget(self.visualization_pie)
        self.main_contain.addWidget(self.visualization_bar)



    def info_Widgets(self):
        pass

    def info_Widgets_Settings(self):
        pass

    def info_Widgets_Layout(self):
        pass

    def log_User(self):
        self.start_Sesson = Login()
        self.start_Sesson.show()

if __name__ in '__main__':
    app = QApplication(sys.argv)
    with open('/home/dns/git_projects/Finances/form.css', 'r') as form:
        sheets_Styles = form.read()
    program = main_App()
    app.setStyleSheet(sheets_Styles)
    app.exit(app.exec())