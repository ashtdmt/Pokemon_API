import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import requests
from io import BytesIO
import os

class Pokemon(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(520, 590)
        self.setWindowTitle("PokeDex")
        self.setGeometry(600, 400, 500, 500)

        self.layout = QVBoxLayout()

        self.text = QLabel("Pokemon")
        self.text.setObjectName("text")
        self.text.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.text)

        self.label = QLabel()
        self.pixmap = QPixmap()
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.label.hide()

        self.info = QLabel("")
        self.info.setObjectName("info")
        self.info.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.info)
        self.info.hide()

        self.input = QLineEdit(self)
        self.input.returnPressed.connect(self.get_pokemon)
        self.input.setPlaceholderText("Type Pokemon Name Here.....")
        self.layout.addWidget(self.input)

        self.button = QPushButton("Search", self)
        self.button.clicked.connect(self.get_pokemon)
        self.layout.addWidget(self.button)

        self.refresh = QPushButton("Refresh", self)
        self.refresh.clicked.connect(self.restart)
        self.layout.addWidget(self.refresh, alignment=Qt.AlignCenter)
        self.refresh.hide()

        self.QWidget = QWidget()
        self.QWidget.setObjectName("QWidget")
        self.layout.addWidget(self.QWidget)

        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #8B0000; 
                font-size: 20px;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f0f0f0;
            }
            QPushButton {
                padding: 10px;
                background-color: #FFDE00;
                color: Black;
                border: none;
                border-radius: 5px;
                font-size: 20px;          
            }
            QPushButton:hover {
                background-color: #B3A125;
            }
            QLabel {
                font-size: 30px;
                background-color: #3B4CCA;
                padding: 10px;
                border: 7px solid #D3D3D3;
                border-radius: 5px;
            }
            QLabel#text {
                font-size: 30px;
                font-weight: bold;
                color: black;
                background-color: #8B0000;
                padding: 10px;
                border: 2px solid #8B0000;
            }
            QLabel#info{
                font-size: 30px;
                background-color: #FFDE00;
                padding: 10px;
                border-radius: 5px; 
            }
        """)

    def get_pokemon(self):
        self.input.hide()
        self.button.hide()
        self.label.show()
        self.info.show()
        base_url = "https://pokeapi.co/api/v2/"
        url = f"{base_url}pokemon/{self.input.text().lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            name = data['name'].capitalize()
            poke_id = data['id']
            types = ', '.join([t['type']['name'].capitalize() for t in data['types']])
            height = data['height']
            weight = data['weight']
            image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
            response = requests.get(image_url)
            img_data = response.content
            self.text.setText(name)
            self.pixmap.loadFromData(img_data)
            scaled_pixmap = self.pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(scaled_pixmap)
            self.label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.label)
            info = (
                f"Type(s): {types}\n"
                f"Height: {height}m\n"
                f"Weight: {weight}kg"
            )
            self.layout.removeWidget(self.label)
            self.layout.insertWidget(1, self.label)
            self.info.show()
            self.info.setText(info)
            self.refresh.show()
            
        else:
            self.text.setText("Pokémon not found.")
            self.input.hide()
            self.button.hide()
            self.label.hide()
            self.info.hide()
            self.refresh.show()

    def restart(self):
        self.text.setText("Pokemon")
        self.text.setText("pokemon")
        self.label.hide()
        self.info.hide()
        self.input.clear()
        self.input.show()
        self.button.show()
        self.refresh.hide()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Pokemon = Pokemon()
    Pokemon.show()
    sys.exit(app.exec_())
