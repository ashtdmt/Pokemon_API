import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QRadioButton
from PyQt5.QtCore import Qt

class QuizGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quiz Game')
        self.setFixedSize(500, 400)
        
        self.layout = QVBoxLayout()
        
        self.question_label = QLabel('What is the capital of France?', self)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.question_label)
        
        self.option1 = QRadioButton('Berlin', self)
        self.option2 = QRadioButton('Madrid', self)
        self.option3 = QRadioButton('Paris', self)
        self.option4 = QRadioButton('Rome', self)
        
        self.layout.addWidget(self.option1)
        self.layout.addWidget(self.option2)
        self.layout.addWidget(self.option3)
        self.layout.addWidget(self.option4)
        
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.check_answer1)
        self.layout.addWidget(self.submit_button)
        
        self.overlay_label = QLabel("", self)
        self.overlay_label.setWordWrap(True)
        self.overlay_label.setAlignment(Qt.AlignCenter)
        self.overlay_label.setStyleSheet("""
            font-size: 60px;
            color: red;
            background: rgba(255,255,255,180);
        """)
        self.overlay_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.overlay_label.hide()

        self.next_button = QPushButton('Next Question', self)
        self.next_button.clicked.connect(self.question2)
        self.layout.addWidget(self.next_button)
        self.next_button.hide()

        self.setLayout(self.layout)
        self.answers = 0
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: lightblue; font-size: 16px; font-family: 'Arial';")
        self.question_label.setStyleSheet("font-weight: bold; font-size: 30px; margin: 10px;")
        self.option1.setStyleSheet("margin: 5px; font-weight: bold;")
        self.option2.setStyleSheet("margin: 5px; font-weight: bold;")
        self.option3.setStyleSheet("margin: 5px; font-weight: bold;")
        self.option4.setStyleSheet("margin: 5px; font-weight: bold;")
        self.submit_button.setStyleSheet("background-color: green; color: white; font-weight: bold; padding: 10px;")
        self.next_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; padding: 10px;")
        self.setLayout(self.layout)

    def check_answer1(self):
        if self.option3.isChecked():
            self.show_overlay('Correct!')
            self.answers = 1
            self.next_button.show()
            self.overlay_label.show()
            self.submit_button.setDisabled(True)
        else:
            self.show_overlay('Wrong! The correct answer is Paris.')
            self.answers = 0
            self.next_button.show()
            self.overlay_label.show()
            self.submit_button.setDisabled(True)

    def show_overlay(self, message):
       self.overlay_label.setText(message)
       self.overlay_label.show()

    def question2(self):
        self.next_button.hide()
        self.overlay_label.hide()
        self.submit_button.setDisabled(False)
        self.question_label.setText('What is the capital of Spain?')
        self.option1.setText('Berlin')
        self.option2.setText('Madrid')
        self.option3.setText('Paris')
        self.option4.setText('Rome')
        
        for option in [self.option1, self.option2, self.option3, self.option4]:
            option.setAutoExclusive(False)
            option.setChecked(False)
            option.setAutoExclusive(True)
        
        self.submit_button.clicked.disconnect()
        self.submit_button.clicked.connect(self.check_answer2)

    def check_answer2(self):
        if self.option2.isChecked():
            self.show_overlay('Correct!')
            self.answers += 1
            self.next_button.clicked.connect(self.question3)
            self.next_button.show()
            self.overlay_label.show()
            self.submit_button.setDisabled(True)
        else:
            self.show_overlay('Wrong! The correct answer is Madrid.')
            self.answers = self.answers
            self.next_button.clicked.connect(self.question3)
            self.next_button.show()
            self.overlay_label.show()
            self.submit_button.setDisabled(True)

    def question3(self):
        self.next_button.hide()
        self.overlay_label.hide()
        self.submit_button.setDisabled(False)
        self.question_label.setText('What is the capital of Italy?')
        self.option1.setText('Berlin')
        self.option2.setText('Madrid')
        self.option3.setText('Rome')
        self.option4.setText('Paris')
        
        for option in [self.option1, self.option2, self.option3, self.option4]:
            option.setAutoExclusive(False)
            option.setChecked(False)
            option.setAutoExclusive(True)
        
        self.submit_button.clicked.disconnect()
        self.submit_button.clicked.connect(self.check_answer3)

    def check_answer3(self):
        if self.option3.isChecked():
            self.show_overlay('Correct!')
            self.answers += 1
            self.next_button.clicked.connect(self.question4)
            self.next_button.show()
            self.overlay_label.show()
            self.submit_button.setDisabled(True)
        else:
            self.show_overlay('Wrong! The correct answer is Rome.')
            self.answers = self.answers
            self.next_button.clicked.connect(self.question4)
            self.next_button.show()
            self.overlay_label.show()
            self.submit_button.setDisabled(True)
        
    def question4(self):
        self.next_button.hide()
        self.overlay_label.hide()
        self.submit_button.setDisabled(False)
        self.question_label.setText('What is the capital of Germany?')
        self.option1.setText('Berlin')
        self.option2.setText('Madrid')
        self.option3.setText('Rome')
        self.option4.setText('Paris')
        
        for option in [self.option1, self.option2, self.option3, self.option4]:
            option.setAutoExclusive(False)
            option.setChecked(False)
            option.setAutoExclusive(True)
        
        self.submit_button.clicked.disconnect()
        self.submit_button.clicked.connect(self.check_answer4)

    def check_answer4(self):
        if self.option1.isChecked():
            self.show_overlay('Correct!')
            self.answers += 1
            self.overlay_label.show()
            self.submit_button.setDisabled(True)
        else:
            self.show_overlay('Wrong! The correct answer is Berlin.')
            self.answers = self.answers
            self.next_button.hide()
            self.overlay_label.show()
        self.show_overlay(f'You answered {self.answers} questions correctly.')

    def resizeEvent(self, event):
        self.overlay_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quiz_game = QuizGame()
    quiz_game.show()
    sys.exit(app.exec_())
