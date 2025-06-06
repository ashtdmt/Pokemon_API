import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,QLabel, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtTest import QTest

class Slots(QWidget):
    def __init__(self):
        super().__init__()
        self.icons_list = ['🍒', '🍋', '🍊', '🍉', '🍇', '🍓', '🍎']
        self.icons = QLabel()
        self.layout = QHBoxLayout()
        self.vetrtical = QVBoxLayout()
        self.layout.addWidget(self.icons)
        self.icons.setAlignment(Qt.AlignCenter)
        self.icons.setStyleSheet("font-size: 50px; "
                                 "font-family: 'Courier New';"
                                 "color: Green; "
                                 "background-color: White;"
                                 )
        self.setLayout(self.layout)
        self.icons1 = QLabel()
        self.icons1.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.icons1)
        self.icons1.setStyleSheet("font-size: 50px; "
                                  "font-family: 'Courier New';"
                                  "color: Green; "
                                  "background-color: White;"
                                  )

        self.icons2 = QLabel()
        self.icons2.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.icons2)
        self.icons2.setStyleSheet("font-size: 50px; "
                                  "font-family: 'Courier New';"
                                  "color: Green; "
                                  "background-color: White;"
                                  )
        
        self.overlay_label = QLabel("", self)
        self.overlay_label.setAlignment(Qt.AlignCenter)
        self.overlay_label.setStyleSheet("""
            font-size: 60px;
            color: red;
            background: rgba(255,255,255,180);
        """)
        self.overlay_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.overlay_label.hide()

        self.vetrtical.addStretch()
        
        self.spin_button = QPushButton('Spin', self)
        self.spin_button.setStyleSheet("font-size: 50px; font-family: 'Courier New'; color: white; background-color: green;")
        self.spin_button.setFixedSize(200, 100)
        self.spin_button.setObjectName("spin_button")
        self.spin_button.clicked.connect(self.spin)
        self.layout.addWidget(self.spin_button, alignment=Qt.AlignCenter)

        self.setStyleSheet("background-color: Gray;")

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Slots Game')
        self.setFixedSize(700, 500)

        self.icons.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
        self.icons1.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
        self.icons2.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
    
    def spin(self):
        QTimer.singleShot(5000, self.enable_spin_button)
        QTimer.singleShot(500, self.update_icons)
        QTimer.singleShot(500, self.update_icons1)
        QTimer.singleShot(500, self.update_icons2)
    def update_icons(self):
        QTest.qWait(500)
        self.icons.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
        QTest.qWait(500)
        self.icons.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
    def update_icons1(self):
        self.icons1.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
        QTest.qWait(500)
        self.icons1.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
        QTest.qWait(500)
        self.icons1.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
    def update_icons2(self):
        self.icons2.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
        QTest.qWait(500)
        self.icons2.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))
        QTest.qWait(500)
        self.icons2.setText(' '.join(random.choice(self.icons_list) for _ in range(1)))

    def resizeEvent(self, event):
        self.overlay_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def show_overlay(self, message):
       self.overlay_label.setText(message)
       self.overlay_label.show()
       QTimer.singleShot(2000, self.hide_overlay)

    def enable_spin_button(self):
        self.spin_button.setDisabled(False)
        self.show_overlay("Spin Again!")
        if self.icons.text() == self.icons1.text() == self.icons2.text():
            self.show_overlay("You Win!")
        else:
            self.show_overlay("Try Again!")
        QTimer.singleShot(2000, self.overlay_label.clear)
        self.spin_button.setDisabled(False)

    def hide_overlay(self):
        self.overlay_label.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Gambaling = Slots()
    Gambaling.show()
    sys.exit(app.exec_()) 

