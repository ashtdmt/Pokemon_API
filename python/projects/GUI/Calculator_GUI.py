import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()
        self.row5 = QHBoxLayout()

        self.layout = QVBoxLayout()

        self.setStyleSheet("background-color: black;")

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setObjectName("display")
        self.label.setGeometry(0, 0, 50, 30)
        self.layout.addWidget(self.label)

        self.zeros = QPushButton('0', self)
        self.zeros.setObjectName("zero")
        self.row5.addWidget(self.zeros)

        self.ones = QPushButton('1', self)
        self.ones.setObjectName("one")
        self.row4.addWidget(self.ones)

        self.twos = QPushButton('2', self)
        self.twos.setObjectName("two")
        self.row4.addWidget(self.twos)

        self.threes = QPushButton('3', self)
        self.threes.setObjectName("three")
        self.row4.addWidget(self.threes)

        self.fours = QPushButton('4', self)
        self.fours.setObjectName("four")
        self.row3.addWidget(self.fours)

        self.fives = QPushButton('5', self)
        self.fives.setObjectName("five")
        self.row3.addWidget(self.fives)

        self.sixes = QPushButton('6', self)
        self.sixes.setObjectName("six")
        self.row3.addWidget(self.sixes)

        self.sevens = QPushButton('7', self)
        self.sevens.setObjectName("seven")
        self.row2.addWidget(self.sevens)

        self.eights = QPushButton('8', self)
        self.eights.setObjectName("eight")
        self.row2.addWidget(self.eights)

        self.nines = QPushButton('9', self)
        self.nines.setObjectName("nine")
        self.row2.addWidget(self.nines)

        self.addition = QPushButton('+', self)
        self.addition.setObjectName("addition")
        self.row4.addWidget(self.addition)

        self.subtraction = QPushButton('-', self)
        self.subtraction.setObjectName("subtraction")
        self.row3.addWidget(self.subtraction)

        self.multiplication = QPushButton('X', self)
        self.multiplication.setObjectName("multiplication")
        self.row2.addWidget(self.multiplication)

        self.division = QPushButton('/', self)
        self.division.setObjectName("division")
        self.row1.addWidget(self.division)

        self.clear = QPushButton('AC', self)
        self.clear.setObjectName("clear")
        self.row1.addWidget(self.clear)

        self.point = QPushButton('.', self)
        self.point.setObjectName("point")
        self.row5.addWidget(self.point)

        self.backspace = QPushButton('<-', self)
        self.backspace.setObjectName("backspace")
        self.row1.addWidget(self.backspace)

        self.equals = QPushButton('=', self)
        self.equals.setObjectName("equals")
        self.row5.addWidget(self.equals)

        self.row5.addStretch()

        self.layout.addLayout(self.row1)
        self.layout.addLayout(self.row2)
        self.layout.addLayout(self.row3)
        self.layout.addLayout(self.row4)
        self.layout.addLayout(self.row5)

        self.initUI()

        self.zeros.clicked.connect(lambda: self.display_number(0))
        self.ones.clicked.connect(lambda: self.display_number(1))
        self.twos.clicked.connect(lambda: self.display_number(2))
        self.threes.clicked.connect(lambda: self.display_number(3))
        self.fours.clicked.connect(lambda: self.display_number(4))
        self.fives.clicked.connect(lambda: self.display_number(5))
        self.sixes.clicked.connect(lambda: self.display_number(6))
        self.sevens.clicked.connect(lambda: self.display_number(7))
        self.eights.clicked.connect(lambda: self.display_number(8))
        self.nines.clicked.connect(lambda: self.display_number(9))
        self.addition.clicked.connect(lambda: self.display_operator('+'))
        self.subtraction.clicked.connect(lambda: self.display_operator('-'))
        self.multiplication.clicked.connect(lambda: self.display_operator('x'))
        self.division.clicked.connect(lambda: self.display_operator('/'))
        self.clear.clicked.connect(self.clear_display)
        self.equals.clicked.connect(self.calculate_result)
        self.backspace.clicked.connect(self.backspace_display)
        self.point.clicked.connect(self.display_point)
        self.setLayout(self.layout)

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.label.setStyleSheet("font-size: 50px; background-color: #f0f0f0; border: 1px solid #ccc; padding: 10px; border-radius: 10px;")
        self.label.setText('0')

        self.setFixedSize(400, 600)

        self.QpushButton = (self.zeros, self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes, self.sevens, self.eights, self.nines,
                            self.addition, self.subtraction, self.multiplication, self.division, self.clear, self.point, self.backspace, self.equals)
        for btn in self.QpushButton:
            btn.setStyleSheet("background-color: #f0f0f0; font-size: 20px; border: 1px solid #ccc; padding: 10px; border-radius: 5px; font-weight: bold;")

        self.setStyleSheet("background-color: black;")
        self.zeros.setFixedSize(187,47)
        self.point.setFixedSize(85,47)
        self.equals.setFixedSize(93,47)
        self.label.setFixedHeight(80)

    def display_number(self, number):
        current_text = self.label.text()
        if current_text == '0' or current_text == 'Error':
            self.label.setText(str(number))
        elif current_text[-1] in '+-x/':
            self.label.setText(current_text + str(number))
        else:
            self.label.setText(current_text + str(number))


    def display_operator(self, operator):
        current_text = self.label.text()
        if current_text == 'Error':
            self.label.setText('0')
        elif current_text[-1] in '+-x/':
            self.label.setText(current_text + operator)
        else:
            self.label.setText(current_text + operator)

    def clear_display(self):
        self.label.setText('0')

    def calculate_result(self):
        current_text = self.label.text()
        try:
            if current_text == 'Error':
                self.label.setText('0')
                return
            expression = current_text.replace('x', '*')
            result = str(eval(expression))
            self.label.setText(result)
        except Exception:
            self.label.setText('Error')


    def display_operator(self, operator):
        current_text = self.label.text()
        if current_text == 'Error':
            self.label.setText('0')
        elif current_text[-1] in '+-x/':
            self.label.setText(current_text[:-1] + operator)
        else:
            self.label.setText(current_text + operator)

    def backspace_display(self):
        current_text = self.label.text()
        if len(current_text) > 1:
            self.label.setText(current_text[:-1])
        elif current_text == 'Error':
            self.label.setText('0')
        else:
            self.label.setText('0')

    def display_point(self):
        current_text = self.label.text()
        if '.' not in current_text.split()[-1]:
            self.label.setText(current_text + '.')


    def backspace(self):
        current_text = self.label.text()
        if len(current_text) > 0:
            if current_text[-1] in '+-x/':
                self.label.setText(current_text[:-1])
            else:
                self.label.setText(current_text[:-1])

    def display_point(self):
        current_text = self.label.text()
        last_segment = current_text.split('+')[-1].split('-')[-1].split('x')[-1].split('/')[-1]
        if '.' not in last_segment:
            self.label.setText(current_text + '.') 

    def point(self):
        current_text = self.label.text()
        if '.' not in current_text:
            self.label.setText(current_text + '.')
        else:
            self.label.setText(current_text)

    def append_operator(self, operator):
        current_text = self.label.text()
        if current_text and current_text[-1] not in '+-x/':
            self.label.setText(current_text + operator)

            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())