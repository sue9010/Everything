import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요")

        menu = self.menuBar()               #메뉴 바 생성
        menu_file = menu.addMenu('File')    #그룹 생성
        menu_edit = menu.addMenu('Edit')
        
        file_exit = QAction('Exit', self)   #메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 종료됩니다.")
        file_new_txt = QAction('텍스트 파일', self)
        file_new_py = QAction('파이썬 파일', self)
        
        file_exit.triggered.connect(QCoreApplication.instance().quit)

        file_new = QMenu('New',self)        #서브 그룹 객체 등록

        file_new.addAction(file_new_txt)    #서브 메뉴 객체 등록
        file_new.addAction(file_new_py)

        menu_file.addMenu(file_new)         #주 메뉴 추가
        menu_file.addAction(file_exit)      #액선 등록
        self.resize(500,500)
        self.show()       

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_()) 