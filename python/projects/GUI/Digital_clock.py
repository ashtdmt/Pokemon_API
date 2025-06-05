import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime

class digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 200, 100)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.updateTime()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(1000) 

        self.setStyleSheet("background-color: black; color: Green; font-size: 50px; font-family: 'Courier New';")


    def updateTime(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = digitalclock()
    clock.show()
    sys.exit(app.exec_())
