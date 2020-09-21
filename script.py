from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 300)
        self.setWindowIcon(QIcon("icon4.png"))
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.mainLayout = QVBoxLayout()
        self.centralwidget.setLayout(self.mainLayout)
        # create the display line
        self._createDisplay()

    def _createDisplay(self):
        """This method creates the calculator display line where the user can
        see the numbers, operations and results"""
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setReadOnly(True)
        self.mainLayout.addWidget(self.display)


def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
