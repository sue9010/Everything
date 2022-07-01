from PyQt5.QtWidgets import (QWidget, QPushButton,QLineEdit, QInputDialog, QApplication)
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):


        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input Dialog')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

