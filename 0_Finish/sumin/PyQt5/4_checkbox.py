import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요")

        menu = self.menuBar()               #메뉴 바 생성
        menu_file = menu.addMenu('File')    #그룹 생성
        menu_edit = menu.addMenu('Edit')    #그룹 생성
        menu_view = menu.addMenu('View')    #그룹 생성

        file_exit = QAction('Exit', self)   #메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 종료됩니다.")
        file_new_txt = QAction('텍스트 파일', self)
        file_new_py = QAction('파이썬 파일', self)
        view_stat = QAction('상태표시줄', self, checkable=True)
        view_stat.setChecked(True)          #기본 상태 - 체크 되어있음
        
        file_exit.triggered.connect(qApp.quit)
        view_stat.triggered.connect(self.tglstat)

        file_new = QMenu('New',self)        #서브 그룹 객체 등록

        file_new.addAction(file_new_txt)    #서브 메뉴 객체 등록
        file_new.addAction(file_new_py)
        

        menu_file.addMenu(file_new)         #주 메뉴 추가
        menu_file.addAction(file_exit)      #액선 등록
        menu_view.addAction(view_stat)      #액선 등록
        self.resize(500,500)
        self.show()       

    def tglstat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
    
    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)

        quit = cm.addAction("Quit")

        action = cm.exec_(self.mapToParent(QContextMenuEvent.pos()))
        if action == quit:
            qApp.quit()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_()) 