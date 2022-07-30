from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout,
                               QPushButton, QMainWindow)
from qdarktheme import load_stylesheet

app = QApplication()
app.setStyleSheet(load_stylesheet())

def printar():
    print('botão clicado')

# encapsulando a janela para poder eventualmente reduzir a dimensão do arquivo
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        base = QWidget() # criamos um widget base que será composto por vários widget
        layout = QVBoxLayout() # escolhemos o layout que desejamos utilizar para posicionar os widgets internos

        menu = self.menuBar()
        file_menu = menu.addMenu('Menu')
        action = QAction('Ação')
        edit_menu = menu.addMenu('Editar')
        edit_action = QAction('Outra ação')
        file_menu.addAction(action)
        edit_menu.addAction(edit_action)

        # estabelecemos um tamanho de fonte
        font = QFont()
        font.setPixelSize(80)

        # criamos um widget de label (basicamente um campo de texto)
        self.label = QLabel('OIEEEE')
        self.label.setFont(font) # indicamos que queremos usar a fonte configurada anteriormente
        self.label.setAlignment(Qt.AlignCenter) # indicamento que queremos centralizar
        layout.addWidget(self.label) # inserimos o label no layout

        botao = QPushButton('Click me!')
        botao.setFont(font)
        botao.clicked.connect(self.muda_label)
        layout.addWidget(botao) # inserimos o botão no layout

        base.setLayout(layout) # indicamos qual o layout a ser utilizado pelo widget base
        self.setCentralWidget(base) # indicamos o widget principal dessa janela

    def muda_label(self):
        self.label.setText('Clicado!')

window = Window() # criamos um widget que aceita funcionalidades de janelas
window.show() # renderizamos a janela
app.exec()
