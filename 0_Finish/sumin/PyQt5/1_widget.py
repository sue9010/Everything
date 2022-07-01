import sys
from PyQt5.QtCore import QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('click', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('툴팁입니다 <b>안녕하세요<b/>')
        btn.move(20,30)

        self.setGeometry(300,300,400,500)
        self.setWindowTitle("첫번째 학습시간")

        self.show()
    
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())