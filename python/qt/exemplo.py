from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()

# estabelecemos um tamanho de fonte
font = QFont()
font.setPixelSize(80)


# criamos um widget de label (basicamente um campo de texto)
label = QLabel('OIEEEE')
label.setFont(font) # indicamos que queremos usar a fonte configurada anteriormente
label.setAlignment(Qt.AlignCenter) # indicamento que queremos centralizar
label.show()

app.exec()
