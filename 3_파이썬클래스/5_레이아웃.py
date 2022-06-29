import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # # 절대 레이아웃
        # lbl1 = QLabel("Zetcode",self)
        # lbl1.move(15,10)

        # lbl2 = QLabel("tutorials", self)
        # lbl2.move(35,40)

        # lbl3 = QLabel("for programers", self)
        # lbl3.move(55,70)

        # # 스트레치 레이아웃
        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        # self.setLayout(vbox)

        # 그리드 레이아웃
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls','Bck','','Close',
                '7','8','9','/',
                '4','5','6','+',
                '1','2','3','-',
                '0','.','=','+']

        positions= [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if __name__ == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)

        self.move(300,150)
        # self.setGeometry(300,300,300,150)
        # self.resize(450,500)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())

