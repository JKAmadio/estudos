import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 500
    height: 400
    font.pixelSize: 24

    Button {
        text: 'Botão'
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }
}