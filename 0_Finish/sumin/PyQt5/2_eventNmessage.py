import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton("눌러주세요", self)
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.resize(500,500)
        self.setWindowTitle("테스트")        
        self.show()
    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes : 
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())