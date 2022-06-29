import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 창 기본 설정
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon(r'E:\PythonPractice\erp_project\test\web.png'))
        # self.resize(400, 200)
        self.setGeometry(300,300,300,200)
        self.center()
        self.show()

        # 그리드 레이아웃
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('업체명:'), 0, 0)
        grid.addWidget(QLabel('국가:'), 1, 0)
        grid.addWidget(QLabel('주소:'), 2, 0)
        grid.addWidget(QLabel('파일:'), 3, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)  
        grid.addWidget(QTextEdit(), 3, 1) 

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
