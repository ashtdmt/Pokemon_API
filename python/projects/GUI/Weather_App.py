import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
import datetime

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(520, 590)
        self.setWindowTitle("Weather App")
        self.setGeometry(600, 400, 500, 500)

        self.layout = QVBoxLayout()

        self.city_input = QLineEdit(self)
        self.city_input.returnPressed.connect(self.get_weather)
        self.text = QLabel("☁️        Enter City Name:       ☁️")
        self.text.setObjectName("text")
        self.text.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.text)

        self.city_input.setPlaceholderText("Type city name here...")
        self.layout.addWidget(self.city_input)

        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.clicked.connect(self.get_weather)
        self.layout.addWidget(self.get_weather_button)

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True) 
        self.result_label.setObjectName("result_label")
        self.layout.addWidget(self.result_label)

        self.QWidget = QWidget()
        self.QWidget.setObjectName("QWidget")
        self.layout.addWidget(self.QWidget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timezone_offset = 0
        self.weather_info = {}

        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                background-color: "#87ceeb"; 
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
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 20px;          
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 30px;
                color: #333;
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 5px;
                font-family: Segoe UI emoji, Arial, sans-serif;
                           
            }
            QLabel#text {
                font-size: 24px;
                font-weight: bold;
                color: #333;
                background-color: #87ceeb;
                padding: 10px;
            }
            """)
        self.text.setFixedSize(500, 50)
        self.result_label.setFixedSize(500, 400)
        self.result_label.setAlignment(Qt.AlignCenter)
    

    def get_weather(self):
        city = self.city_input.text()
        if city:
            api_key = "74b6081b8af8e98fab540725c9e7c9b2"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    self.weather_description = data['weather'][0]['description']
                    self.temperature = data['main']['temp']
                    dayornight = data['weather'][0]['icon']
                    if dayornight.endswith('d'):
                        self.daytime = "Day☀️"
                    else:
                        self.daytime = "Night🌕"

                    self.timezone_offset = data['timezone']                        
                    current_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=self.timezone_offset)
                    formatted_time = current_time.strftime("%H:%M:%S")
                                   
                    self.emoji = ""
                    if self.weather_description == "clear sky":
                        self.emoji = "🌞"
                        self.result_label.setStyleSheet("background-color: #ffec99;")
                    elif self.weather_description == "few clouds":
                        self.emoji = "🌤️"
                        self.result_label.setStyleSheet("background-color: #b3e0ff;")
                    elif self.weather_description == "scattered clouds":
                        self.emoji = "🌥️"
                        self.result_label.setStyleSheet("background-color: #cce6ff;")
                    elif self.weather_description == "broken clouds":
                        self.emoji = "☁️"
                        self.result_label.setStyleSheet("background-color: #b0c4de;")
                    elif self.weather_description == "overcast clouds":
                        self.emoji = "☁️"
                        self.result_label.setStyleSheet("background-color: #a9a9a9;")
                    elif self.weather_description == "light rain":
                        self.emoji = "🌦️"
                        self.result_label.setStyleSheet("background-color: #b3c6ff;")
                    elif self.weather_description == "moderate rain":
                        self.emoji = "🌧️"
                        self.result_label.setStyleSheet("background-color: #7ec0ee;")
                    elif self.weather_description == "rain":
                        self.emoji = "🌧️"
                        self.result_label.setStyleSheet("background-color: #4682b4;")
                    elif self.weather_description == "heavy rain":
                        self.emoji = "🌧️"
                        self.result_label.setStyleSheet("background-color: #27408b;")
                    elif self.weather_description == "snow":
                        self.emoji = "❄️"
                        self.result_label.setStyleSheet("background-color: #f0f8ff;")
                    elif self.weather_description == "light snow":
                        self.emoji = "🌨️"
                        self.result_label.setStyleSheet("background-color: #e0f7fa;")
                    elif self.weather_description == "heavy snow":
                        self.emoji = "❄️"
                        self.result_label.setStyleSheet("background-color: #e6e6fa;")
                    elif self.weather_description == "clouds":
                        self.emoji = "☁️"
                        self.result_label.setStyleSheet("background-color: #b0c4de;")
                    elif self.weather_description == "thunderstorm":
                        self.emoji = "⛈️"
                        self.result_label.setStyleSheet("background-color: #4b0082; color: #fff;")
                    elif self.weather_description == "drizzle":
                        self.emoji = "🌦️"
                        self.result_label.setStyleSheet("background-color: #b3c6ff;")
                    elif self.weather_description == "fog":
                        self.emoji = "🌫️"
                        self.result_label.setStyleSheet("background-color: #d3d3d3;")
                    elif self.weather_description == "mist":
                        self.emoji = "🌁"
                        self.result_label.setStyleSheet("background-color: #e0e0e0;")
                    elif self.weather_description == "haze":
                        self.emoji = "🌫️"
                        self.result_label.setStyleSheet("background-color: #f5f5dc;")
                    elif self.weather_description == "smoke":
                        self.emoji = "🌫️"
                        self.result_label.setStyleSheet("background-color: #a9a9a9;")
                    elif self.weather_description == "sand":
                        self.emoji = "🌪️"
                        self.result_label.setStyleSheet("background-color: #f4e2d8;")
                    elif self.weather_description == "dust":
                        self.emoji = "🌪️"
                        self.result_label.setStyleSheet("background-color: #e5c07b;")
                    elif self.weather_description == "ash":
                        self.emoji = "🌋"
                        self.result_label.setStyleSheet("background-color: #b2beb5;")
                    elif self.weather_description == "squalls":
                        self.emoji = "🌬️"
                        self.result_label.setStyleSheet("background-color: #b0e0e6;")
                    elif self.weather_description == "tornado":
                        self.emoji = "🌪️"
                        self.result_label.setStyleSheet("background-color: #808080; color: #fff;")
                    elif self.weather_description == "hurricane":
                        self.emoji = "🌪️"
                        self.result_label.setStyleSheet("background-color: #708090; color: #fff;")
                    elif self.weather_description == "tropical storm":
                        self.emoji = "🌪️"
                        self.result_label.setStyleSheet("background-color: #00ced1;")
                    elif self.weather_description == "blizzard":
                        self.emoji = "❄️"
                        self.result_label.setStyleSheet("background-color: #e0ffff;")
                    elif self.weather_description == "freezing rain":
                        self.emoji = "❄️"
                        self.result_label.setStyleSheet("background-color: #b0e0e6;")
                    elif self.weather_description == "sleet":
                        self.emoji = "🌨️"
                        self.result_label.setStyleSheet("background-color: #c0c0c0;")
                    elif self.weather_description == "hail":
                        self.emoji = "🌨️"
                        self.result_label.setStyleSheet("background-color: #e6e6fa;")
                    elif self.weather_description == "windy":
                        self.emoji = "💨"
                        self.result_label.setStyleSheet("background-color: #f0e68c;")
                    else:
                        self.emoji = "🌈"
                        self.result_label.setStyleSheet("background-color: #87ceeb;")

                    self.result_label.setText(f"Weather: {self.weather_description}<br><span style='font-size:70px'>{self.emoji}</span><br><br>Temperature: {self.temperature}°C<br>{self.daytime}<br>Time: {formatted_time}")
                    self.timer.start(1000)
                    self.result_label.setTextFormat(Qt.RichText)
                    self.weather_info = {"set": True}
                else:
                    self.result_label.setText("<span style='font-size:80px; font-weight:bold;'>CITY NOT FOUND.</span>")
                    self.result_label.setStyleSheet("background-color: #ffcccc; color: #ff0000;")
                    self.timer.stop()
                    self.weather_info = {}
            except requests.exceptions.RequestException as e:
                self.result_label.setText("<span style='font-size:70px; font-weight:bold;'>Network error. Please try again.</span>")
                self.result_label.setStyleSheet("background-color: #ffcccc; color: #ff0000;")
                self.timer.stop()
                self.weather_info = {}
        else:
            self.result_label.setText("Please enter a city name.")

    def update_time(self):
        if not self.weather_info:
            return
        current_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=self.timezone_offset)
        formatted_time = current_time.strftime("%H:%M:%S")
        self.result_label.setText(f"Weather: {self.weather_description}<br><span style='font-size:70px'>{self.emoji}</span><br><br>Temperature: {self.temperature}°C<br>{self.daytime}<br>Time: {formatted_time}")
        self.result_label.setTextFormat(Qt.RichText)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())



