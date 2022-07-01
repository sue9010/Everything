import sys
from PyQt5.QtWidgets import (QLabel, QLineEdit, QTextEdit, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QGridLayout)

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        '''
        절대좌표 레이아웃
        # lbl1 = QLabel('Zetcode',self)
        # lbl1.move(15,10)
        
        # lbl2 = QLabel('tutorials',self)
        # lbl2.move(35,40)
        
        # lbl3 = QLabel('for programmers',self)
        # lbl3.move(55,70)
        '''

        '''
        스트레치 레이아웃
        # okButton = QPushButton("Ok")
        # cancelButton = QPushButton("Cancel")

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        # self.setLayout(vbox)
        '''

        '''
        그리드 레이아웃 - 그룹으로 지정
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        
        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        '''

        '''
        그리드 레이아웃 - 개별 지정
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1,0)
        grid.addWidget(titleEdit ,1,1)

        grid.addWidget(author, 2,0)
        grid.addWidget(authorEdit ,2,1)       

        grid.addWidget(review, 3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)
        '''
        
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Review')
        # self.resize(500,500)
        self.show()       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_()) 