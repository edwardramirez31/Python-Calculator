from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 300)
        self.setWindowIcon(QIcon("icon4.png"))
        self.setStyleSheet("background-color : #99AAAB;")
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.mainLayout = QVBoxLayout()
        self.centralwidget.setLayout(self.mainLayout)
        # create the display line
        self._createDisplay()
        # create the buttons
        self._createButtons()

    def _createDisplay(self):
        """This method creates the calculator display line where the user can
        see the numbers, operations and results"""
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setReadOnly(True)
        self.display.setFont(QFont('Times', 15))
        self.display.setAlignment(Qt.AlignRight)
        self.mainLayout.addWidget(self.display)
        self.display.setStyleSheet("""
            background-color : #DAE0E2;
            border-radius : 10px;
            border : 1px solid white""")

    def _createButtons(self):
        self.buttons = {}
        self.buttonslayout = QGridLayout()
        """ Buttons dictionary where the key is the button text and the value is
        its grid location"""
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "CE": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4)
        }

        for button_text, location in buttons.items():
            self.button = QPushButton(button_text)
            self.button.setFixedSize(50, 50)
            self.button.setFont(QFont('Times', 15))
            # Style
            self.button.setStyleSheet("""QPushButton {
                                        background-color : #2C3335;
                                        color : white;

                                      }
                                      QPushButton:hover {
                                        background-color: #7B8788;
                                      }
                                      """)
            self.buttons[button_text] = self.button
            # add widget
            self.buttonslayout.addWidget(self.buttons[button_text], location[0], location[1])
        self.mainLayout.addLayout(self.buttonslayout)

    # Calculator Functionality
    def setDisplayText(self, text):
        """This method sets and updates the display Text"""
        self.display.setText(text)
        self.display.setFocus()

    def getDisplayText(self):
        """This method get the text shown in the display when the user
        clicks on '=' Button"""
        return self.display.text()

    def clearDisplay(self):
        """This method clears the display when somebody presses the 'C' Button"""
        self.display.setText('')

    def evaluateExpression(self):
        display_text = self.display.text()
        try:
            result = eval(display_text, {}, {})
            self.display.setText(str(result))
        except:
            self.display.setText("ERROR")


class Controller:
    def __init__(self, window):
        self._window = window
        self.connectSignals()

    def buildingText(self, button_text):
        if self._window.getDisplayText() == "ERROR":
            self._window.clearDisplay()

        display_text = self._window.getDisplayText()
        text_to_include = display_text + button_text
        self._window.setDisplayText(text_to_include)

    def connectSignals(self):
        for button_name, button_widget in self._window.buttons.items():
            if not (button_name == "CE" or button_name == "="):
                button_widget.clicked.connect(partial(self.buildingText, button_name))
            if button_name == "CE":
                button_widget.clicked.connect(self._window.clearDisplay)
            if button_name == "=":
                button_widget.clicked.connect(self._window.evaluateExpression)
        self._window.display.returnPressed.connect(self._window.evaluateExpression)


def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    controller = Controller(window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
