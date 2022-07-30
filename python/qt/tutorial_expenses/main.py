import sys
from turtle import right
from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QAction, QHeaderView,
        QHBoxLayout, QVBoxLayout,
        QWidget, QTableWidget, QPushButton, QLineEdit, QLabel, QTableWidgetItem
    )
from PyQt5.QtChart import QChartView, QChart, QPieSeries


class DataEntryForm(QWidget):
    def __init__(self):
        super().__init__()        

        # cria o layout
        self.layout = QHBoxLayout()

        self.items = 0
        self._data = {
            "Phone Bill": 50.5,
            "Gas": 250.5,
            "Rent": 1000,
            "Comcast": 105,
        }

        # cria a tabela
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(('Description', 'Price'))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # colunas se ajustam ao tamanho

        # cria layout da parte da direita
        self.right_layout = QVBoxLayout()

        # campo para descrição do gasto
        self.description_label = QLabel('Description')
        self.description_lineEdit = QLineEdit()
        self.description_lineEdit.textChanged[str].connect(self.check_disable)
        self.right_layout.addWidget(self.description_label)
        self.right_layout.addWidget(self.description_lineEdit)

        # campo para valor do gasto
        self.price_label = QLabel('Price')
        self.price_lineEdit = QLineEdit()
        self.price_lineEdit.textChanged[str].connect(self.check_disable)
        self.right_layout.addWidget(self.price_label)
        self.right_layout.addWidget(self.price_lineEdit)

        # botões de adicionar gasto e plotar gráfico
        self.add_button = QPushButton('Add')
        self.right_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_entry)
        self.plot_button = QPushButton('Plot')
        self.right_layout.addWidget(self.plot_button)
        self.plot_button.clicked.connect(self.generate_chart)

        # gráfico dos gastos
        self.chartView = QChartView()
        self.right_layout.addWidget(self.chartView)


        # botões de limpar tudo e para sair da aplicação
        self.clear_button = QPushButton('Clear')
        self.right_layout.addWidget(self.clear_button)
        self.clear_button.clicked.connect(self.reset_table)
        self.exit_button = QPushButton('Exit')
        self.right_layout.addWidget(self.exit_button)
        self.exit_button.clicked.connect(lambda: app.exit())

        # insere a tabela no layout
        self.layout.addWidget(self.table, 50)

        #insere right_layout no layout
        self.layout.addLayout(self.right_layout,50)

        self.setLayout(self.layout)
        self.check_disable()
        self.fill_table()


    def fill_table(self, data=None):
        # se não houver nenhum input em data, a tabela deve ser preenchida com _data (dummy)
        data = self._data if not data else data

        for description, price in data.items():
            descriptionItem = QTableWidgetItem(description)
            priceItem = QTableWidgetItem(f'R$ {int(price):.02f}')
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, descriptionItem)
            self.table.setItem(self.items, 1, priceItem)
            self.items += 1


    def add_entry(self):
        description = self.description_lineEdit.text()
        price = self.price_lineEdit.text()

        descriptionItem = QTableWidgetItem(description)
        priceItem = QTableWidgetItem(f'R$ {int(price):.02f}')
        self.table.insertRow(self.items)
        self.table.setItem(self.items, 0, descriptionItem)
        self.table.setItem(self.items, 1, priceItem)
        self.items += 1

        # após inserção apagamos os campos
        self.description_lineEdit.setText('')
        self.price_lineEdit.setText('')


    def check_disable(self):
        if self.description_lineEdit.text() and self.price_lineEdit.text():
            self.add_button.setEnabled(True)
        else:
            self.add_button.setEnabled(False)


    def reset_table(self):
        self.table.setRowCount(0)
        self.items = 0

        chart = QChart()
        self.chartView.setChart(chart)


    def generate_chart(self):
        series = QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            val = float(self.table.item(i, 1).text().replace('R$ ', ''))
            series.append(text, val)

        chart = QChart()
        chart.addSeries(series)
        chart.legend()
        self.chartView.setChart(chart)


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()

        self.resize(800, 600)

        # configurações da barra de menu
        self.menu_bar = self.menuBar()
        self.menu_item_file = self.menu_bar.addMenu('File')
        
        # configurações das ações do menu
        exportAction = QAction('Export to csv', self)
        exportAction.setShortcut('Ctrl+E')
        # todo: criar a função exportFile que será disparada quando o usuário clicar neste botão
        # exportAction.triggered.connect(exportFile)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(lambda: app.quit())

        self.menu_item_file.addAction(exportAction)
        self.menu_item_file.addAction(exitAction)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = DataEntryForm()    

    demo = MainWindow(widget)
    demo.show()
    sys.exit(app.exec())