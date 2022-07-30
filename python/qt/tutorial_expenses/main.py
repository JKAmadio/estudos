import sys
from turtle import right
from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QAction, QHeaderView,
        QHBoxLayout, QVBoxLayout,
        QWidget, QTableWidget, QPushButton, QLineEdit, QLabel
    )
from PyQt5.QtChart import QChartView


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
        self.right_layout.addWidget(self.description_label)
        self.right_layout.addWidget(self.description_lineEdit)

        # campo para valor do gasto
        self.price_label = QLabel('Price')
        self.right_layout.addWidget(self.price_label)
        self.price_lineEdit = QLineEdit()
        self.right_layout.addWidget(self.price_lineEdit)

        # botões de adicionar gasto e plotar gráfico
        self.add_button = QPushButton('Add')
        self.right_layout.addWidget(self.add_button)
        self.plot_button = QPushButton('Plot')
        self.right_layout.addWidget(self.plot_button)

        # gráfico dos gastos
        self.chart = QChartView()
        self.right_layout.addWidget(self.chart)


        # botões de limpar tudo e para sair da aplicação
        self.clear_button = QPushButton('Clear')
        self.right_layout.addWidget(self.clear_button)
        self.exit_button = QPushButton('Exit')
        self.right_layout.addWidget(self.exit_button)

        # insere a tabela no layout
        self.layout.addWidget(self.table, 50)

        #insere right_layout no layout
        self.layout.addLayout(self.right_layout,50)

        self.setLayout(self.layout)
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