import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # 상태 표시줄 추가
        self.statusBar()
        self.statusBar().showMessage("준비")

        # 메뉴 추가
        menu = self.menuBar()               # 매뉴바 생성
        menu_file = menu.addMenu("File")    # 그룹 생성
        menu_edit = menu.addMenu("Edit")    # 그룹 생성

        # 메뉴 이름 등록
        file_new = QMenu("New", self)
        file_new_txt = QAction("텍스트 파일", self)
        file_new_python = QAction("파이썬 파일", self) 
        
        edit_do = QMenu("Do", self)
        edit_do_do = QAction("Do",self)
        edit_do_undo = QAction("Undo", self)

        # 디테일 동작 등록
        file_exit = QAction("Exit", self)   # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')     # 단축키 지정
        file_exit.setStatusTip('누르면 종료됩니다.') #상태표시줄에 내용 표시
        file_exit.triggered.connect(QCoreApplication.instance().quit) # 파일 메뉴 exit 를 선택하면 창이 종료됨

        # 메뉴 동작 등록
        menu_file.addMenu(file_new)         # 메뉴 등록 -> 하위 메뉴 생성 가능
        file_new.addAction(file_new_txt)    # 하위 메뉴의 동작 설정
        file_new.addAction(file_new_python) # 하위 메뉴의 동작 설정

        menu_file.addAction(file_exit)      # 메뉴 등록 -> 동작 실행

        menu_edit.addMenu(edit_do)          # 메뉴 등록 -> 하위 메뉴 생성 가능
        edit_do.addAction(edit_do_do)       # 하위 메뉴의 동작 설정
        edit_do.addAction(edit_do_undo)     # 하위 메뉴의 동작 설정



        # 창 기본 설정
        self.resize(450,500)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())

