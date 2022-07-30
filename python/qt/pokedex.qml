import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    font.pixelSize: 24

    Row {
        id: header
        spacing: 20
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: parent.top // estabelecemos qual a base que queremos para o topo do elemento
            topMargin: 20 // para depois estabelecer a margem em relação a base
        }

        TextField {
            id: pokemon_id_input
            placeholderText: 'Pokemon id...'
            width: 200      
        }
        Button {
            id: get_pokemon
            text: 'Get!'
            width: 150
        }
    }

    Label {
        id: pokemon_name
        text: 'nome do pokemon'
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: header.bottom // a parte de baico do cabeçalho é a base para o topo do nome
            topMargin: 20
        }
    }

    Image {
        id: pokemon_image
        width: 100
        height: 100
    }
}