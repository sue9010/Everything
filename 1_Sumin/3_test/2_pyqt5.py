import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 그리드 레이아웃
        # grid = QGridLayout()
        # self.setLayout(grid)

        # grid.addWidget(QLabel('Title:'), 0, 0)
        # grid.addWidget(QLabel('Author:'), 1, 0)
        # grid.addWidget(QLabel('Review:'), 2, 0)

        # grid.addWidget(QLineEdit(), 0, 1)
        # grid.addWidget(QLineEdit(), 1, 1)
        # grid.addWidget(QTextEdit(), 2, 1)  

        exitAction = QAction(QIcon(r'E:\PythonPractice\erp_project\test\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        editAction = QAction(QIcon(r'E:\PythonPractice\erp_project\test\edit.png'), 'Edit', self)
        editAction.setShortcut('Ctrl+E')
        editAction.setStatusTip('Edit appliction')
        editAction.triggered.connect(qApp.quit)

        # 메뉴 바
        # menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)

        # filemenu = menubar.addMenu('&File')
        # filemenu.addAction(exitAction)
        # editmenu = menubar.addMenu('&Edit')
        # viewmenu = menubar.addMenu('&View')
        # toolsmenu = menubar.addMenu('&Tools')
        # helpmenu = menubar.addMenu('&Help')

        # 툴 바
        # self.toolbar = self.addToolBar('Exit')
        # self.toolbar.addAction(exitAction)
        # self.toolbar = self.addToolBar('Edit')
        # self.toolbar.addAction(editAction)

        # 상태 바
        # self.statusBar().showMessage('Ready')

        # 버튼
        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('이 버튼은 <b>QWidget</b> 위젯입니다.')
        
        # btn = QPushButton('Quit', self)
        # btn.move(300, 150)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)

        # 탭 위젯
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)            
      

        # 창 기본 설정
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon(r'E:\PythonPractice\erp_project\test\web.png'))
        # self.resize(400, 200)
        self.setGeometry(300,300,300,200)
        self.center()
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
