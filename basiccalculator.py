import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QMenuBar,QMessageBox

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.visuals()

        self.history = []

    def visuals(self):
        self.setWindowTitle('calculator')
        self.setGeometry(300, 300, 300, 300)

        self.one_btn = QPushButton('1')
        self.one_btn.clicked.connect(lambda: self.update_display('1'))
        self.two_btn = QPushButton('2')
        self.two_btn.clicked.connect(lambda: self.update_display('2'))
        self.three_btn = QPushButton('3')
        self.three_btn.clicked.connect(lambda: self.update_display('3'))
        self.four_btn = QPushButton('4')
        self.four_btn.clicked.connect(lambda: self.update_display('4'))
        self.five_btn = QPushButton('5')
        self.five_btn.clicked.connect(lambda: self.update_display('5'))
        self.six_btn = QPushButton('6')
        self.six_btn.clicked.connect(lambda: self.update_display('6'))
        self.seven_btn = QPushButton('7')
        self.seven_btn.clicked.connect(lambda: self.update_display('7'))
        self.eight_btn = QPushButton('8')
        self.eight_btn.clicked.connect(lambda: self.update_display('8'))
        self.nine_btn = QPushButton('9')
        self.nine_btn.clicked.connect(lambda: self.update_display('9'))
        self.zero_btn = QPushButton('0')
        self.zero_btn.clicked.connect(lambda: self.update_display('0'))
        self.calculate_btn = QPushButton('=')
        self.calculate_btn.clicked.connect(lambda: self.calculate())
        self.clear_btn = QPushButton('C')
        self.clear_btn.clicked.connect(lambda: self.clear_display())
        self.add_btn = QPushButton('+')
        self.add_btn.clicked.connect(lambda: self.update_display('+'))
        self.subtract_btn = QPushButton('-')
        self.subtract_btn.clicked.connect(lambda: self.update_display('-'))
        self.multiply_btn = QPushButton('*')
        self.multiply_btn.clicked.connect(lambda: self.update_display('*'))
        

        self.history_btn = QPushButton('History')
        self.history_btn.clicked.connect(self.History_show)
        

        self.display_txt = QLineEdit()
        self.display_txt.setReadOnly(True)

        grid_layout = QGridLayout()

        
        grid_layout.addWidget(self.display_txt, 0, 0, 1, 3)
        grid_layout.addWidget(self.history_btn, 0, 3)  # Add display to row 0, column 0, span 1 row and 4 columns
        grid_layout.addWidget(self.one_btn, 1, 0)
        grid_layout.addWidget(self.two_btn, 1, 1)
        grid_layout.addWidget(self.three_btn, 1, 2)
        grid_layout.addWidget(self.add_btn, 1, 3)
        grid_layout.addWidget(self.four_btn, 2, 0)
        grid_layout.addWidget(self.five_btn, 2, 1)
        grid_layout.addWidget(self.six_btn, 2, 2)
        grid_layout.addWidget(self.subtract_btn, 2, 3)
        grid_layout.addWidget(self.seven_btn, 3, 0)
        grid_layout.addWidget(self.eight_btn, 3, 1)
        grid_layout.addWidget(self.nine_btn, 3, 2)
        grid_layout.addWidget(self.multiply_btn, 3, 3)
        grid_layout.addWidget(self.zero_btn, 4, 0)
        grid_layout.addWidget(self.clear_btn, 4, 1)
        grid_layout.addWidget(self.calculate_btn, 4, 2, 1, 2)  # Span 1 row and 2 columns

        self.setLayout(grid_layout)

    def update_display(self, value):
        current_text = self.display_txt.text()
        self.display_txt.setText(current_text + value)

    def calculate(self):
        expression = self.display_txt.text()
        try:
            result = eval(expression)
            self.updatehistory(expression, result)
            self.display_txt.setText(str(result))
        except Exception as e:
            print(f"Error during calculation: {e}")

    def clear_display(self):
        self.display_txt.clear()
    
    def updatehistory(self, expression, result):
        self.history.append((expression, result))
        if len(self.history) > 5:
            self.history.pop(0)
    
    def History_show(self):
        history_text = "\n".join([f"{exp} = {res}" for exp, res in self.history])
        if history_text:
            self.display_txt.setText(history_text)
        else:
            print("History is empty")

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())
