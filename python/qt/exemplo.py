from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout,
                               QPushButton, QMainWindow)
app = QApplication()
window = QMainWindow() # criamos um widget que aceita funcionalidades de janelas
base = QWidget() # criamos um widget base que será composto por vários widget
layout = QVBoxLayout() # escolhemos o layout que desejamos utilizar para posicionar os widgets internos

menu = window.menuBar()
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
label = QLabel('OIEEEE')
label.setFont(font) # indicamos que queremos usar a fonte configurada anteriormente
label.setAlignment(Qt.AlignCenter) # indicamento que queremos centralizar
layout.addWidget(label) # inserimos o label no layout

botao = QPushButton('Click me!')
botao.setFont(font)
layout.addWidget(botao) # inserimos o botão no layout

base.setLayout(layout) # indicamos qual o layout a ser utilizado pelo widget base
window.setCentralWidget(base) # indicamos o widget principal dessa janela
window.show() # renderizamos a janela
app.exec()
