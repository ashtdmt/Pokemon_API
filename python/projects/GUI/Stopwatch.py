import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.elapsed_time = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)

    def initUI(self):
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100, 100, 300, 150)

        self.label = QLabel('00:00:000', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 50px; "
                                "font-family: 'Courier New';"
                                "color: Green; "
                                "background-color: black;"
                                )

        start_button = QPushButton('Start', self)
        start_button.clicked.connect(self.start)

        stop_button = QPushButton('Stop', self)
        stop_button.clicked.connect(self.stop)

        reset_button = QPushButton('Reset', self)
        reset_button.clicked.connect(self.reset)

        self.QPushButton = (start_button, stop_button, reset_button)

        for button in self.QPushButton:
            button.setStyleSheet(
                "background-color: Green;"
            )

        self.setStyleSheet("background-color: black;")

        button_layout = QHBoxLayout()
        button_layout.addWidget(start_button)
        button_layout.addWidget(stop_button)
        button_layout.addWidget(reset_button)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

    def stop(self):
        if self.timer.isActive():
            self.timer.stop()

    def updateTime(self):
            self.elapsed_time += 10  # increment by 10 ms
            minutes, remainder = divmod(self.elapsed_time, 60000)
            seconds, milliseconds = divmod(remainder, 1000)
            time_string = f'{minutes:02}:{seconds:02}:{milliseconds:03}'
            self.label.setText(time_string)

    def start(self):
        if not self.timer.isActive():
             self.timer.start(10)  # Update every 10 ms

    def reset(self):
        self.stop()
        self.elapsed_time = 0
        self.label.setText('00:00:000')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
