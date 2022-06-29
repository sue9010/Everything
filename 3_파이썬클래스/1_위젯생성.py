# 기본 창 생성
# 위젯 창 생성, 메뉴 바가 없음

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # 버튼 생성
        btn = QPushButton('버튼 이름',self)

        # resize(): 버튼 크기 조정
        # sizeHint(): 버튼 안 글씨를 기준으로 버튼 크기를 설정
        btn.resize(btn.sizeHint())

        # settoolTip(): 버튼 위에 마우스를 올리면 나오는 글씨
        # html 태그가 들어갈 수 있음.
        btn.setToolTip('툴팁입니다.<b>안녕하세요<b>')
        
        # move(): 버튼 위치 조정
        btn.move(20,30)
        

        # 창 크기 조정
        self.setGeometry(300,300,400,500)
        # 창 이름 조정
        self.setWindowTitle('첫번째 수업 시간')
        # 창 띄우기
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())

