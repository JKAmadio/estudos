from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication

# construimos essa classe Ponte para fazer a ligação
# entre o Javascript do onClicked no .qml para o Python daqui
class Ponte(QObject):
    @Slot(str, result=str)
    def fetch_image(self, pokemon_id):
        return 'Pikachu'

app = QGuiApplication()

engine = QQmlApplicationEngine()
engine.load('pokedex.qml')

# criamos um context na engine para que a classe Ponte
# possa ser reconhecida no arquivo .qml
ponte = Ponte()
context = engine.rootContext()
context.setContextProperty('ponte', ponte)

app.exec()