from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication

app = QGuiApplication()

engine = QQmlApplicationEngine()
engine.load('pokedex.qml')

app.exec()