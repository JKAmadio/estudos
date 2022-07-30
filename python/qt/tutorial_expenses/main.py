import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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






if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec())