import sys, pymysql
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, QTreeView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt


class insert(QWidget):
    global w

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1400,330,250,180)
        self.setWindowTitle("데이터 추가")
        
        self.lbl번호 = QLabel("번호",self)  #라벨, 텍스트 박스  위치 설정
        self.lbl번호.move(25,25)
        self.txt번호 = QLineEdit(self)
        self.txt번호.move(25+49,22)
        self.txt번호.setReadOnly(True)
        self.lbl이름 = QLabel("이름",self)
        self.lbl이름.move(25,60)
        self.txt이름 = QLineEdit(self)
        self.txt이름.move(25+49,57)
        self.lbl주소 = QLabel("주소",self)
        self.lbl주소.move(25,95)
        self.txt주소 = QLineEdit(self)
        self.txt주소.move(25+49,92)

        self.btn입력 = QPushButton("입력", self)
        self.btn입력.move(85,130)
        self.btn입력.clicked.connect(self.into)

    def into(self):
        if(self.txt이름.text() != "") and (self.txt주소.text() != ""):
            try:
                self.cmd = "insert into test2(`no`,`name`,`add`) values({},'{}','{}')"\
                    .format(self.txt번호.text(), self.txt이름.text(), self.txt주소.text())
                print(self.cmd)
                w.cur.execute(self.cmd)
                w.conn.commit()
            except:
                QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요.", 
                                        QMessageBox.Yes, QMessageBox.Yes)
                return
        else:
            QMessageBox.information(self, "입력오류", "빈칸 없이 입력하세요.", 
                                    QMessageBox.Yes, QMessageBox.Yes)
            return
        self.close()


    def showEvent(self, QShowEvent):
        self.txt번호.setText(str(w.cnt+1))
        self.txt이름.clear()
        self.txt주소.clear()


class sql(QWidget):
    cnt = 0
    global k
    list = []


    def __init__(self):
        super().__init__()
        self.sqlConnect()
        self.initUI()

    def sqlConnect(self):
        try:
            self.conn = pymysql.connect(host='localhost', user='user', password='user', db='cox', port =3306, charset='utf8')
        except:
            print("문제가 있네요")
            exit(1)
        print("연결 성공!")
        self.cur = self.conn.cursor()

    def initUI(self):
        self.w = 400
        self.h = 420
        self.btnSize =40
        self.setGeometry(300,300,self.w, self.h)
        self.setWindowTitle("데이터 베이스 활용 예제")

        self.lbl번호 = QLabel("번호",self)  #라벨, 텍스트 박스  위치 설정
        self.lbl번호.move(25,25)
        self.txt번호 = QLineEdit(self)
        self.txt번호.move(25+49,22)
        self.lbl이름 = QLabel("이름",self)
        self.lbl이름.move(25,60)
        self.txt이름 = QLineEdit(self)
        self.txt이름.move(25+49,57)
        self.lbl주소 = QLabel("주소",self)
        self.lbl주소.move(25,95)
        self.txt주소 = QLineEdit(self)
        self.txt주소.move(25+49,92)

        self.리스트 = QTreeView(self)
        self.리스트.setRootIsDecorated(False)       #번호 앞 빈칸 삭제
        self.리스트.setRootIsDecorated(True)
        self.리스트.setAlternatingRowColors(True)   
        self.리스트.resize(330,200)
        self.리스트.move(25,130)

        self.내용 = QStandardItemModel(0,3,self)    #가로 행 index 설정
        self.내용.setHeaderData(0, Qt.Horizontal, "번호")
        self.내용.setHeaderData(1, Qt.Horizontal, "이름")
        self.내용.setHeaderData(2, Qt.Horizontal, "주소")
        self.리스트.clicked.connect(self.slt)

        self.리스트.setModel(self.내용)    #가로 행 넓이 설정
        self.리스트.setColumnWidth(0,40)
        self.리스트.setColumnWidth(1,80)

        self.cmd이전 = QPushButton("이전", self)
        self.cmd이전.resize(self.btnSize, self.btnSize)
        self.cmd이전.clicked.connect(self.pre)
        self.cmd다음 = QPushButton("다음", self)
        self.cmd다음.resize(self.btnSize, self.btnSize)
        self.cmd다음.clicked.connect(self.next)
        self.cmd신규 = QPushButton("신규", self)
        self.cmd신규.clicked.connect(self.new)
        self.cmd신규.resize(self.btnSize, self.btnSize)
        self.cmd수정 = QPushButton("수정", self)
        self.cmd수정.clicked.connect(self.edit)
        self.cmd수정.resize(self.btnSize, self.btnSize)
        self.cmd삭제 = QPushButton("삭제", self)
        self.cmd삭제.resize(self.btnSize, self.btnSize)
        self.cmd삭제.clicked.connect(self.dlt)

        self.cur.execute("select max(no) from test2")
        self.conn.commit()
        self.cnt = self.cur.fetchone()[0]
        
        self.show()

    def dlt(self):
        a = QMessageBox.question(self, "삭제 확인", "정말로 삭제합니까?",
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if a == QMessageBox.Yes:
            self.cmd = "delete from test2 where `no` = {}".format(self.txt번호.text())
            print(self.cmd)
            self.cur.execute(self.cmd)
            self.conn.commit()
            self.cnt = self.cnt -1
            self.내용.removeRow(self.cnt)
            self.pre()

    def pre(self):
        if self.리스트.currentIndex().row()==0:
            return
        else:
            self.리스트.setCurrentIndex(self.내용.index(self.리스트.currentIndex().row()-1,0))
            self.slt()

    def next(self):
        if self.리스트.currentIndex().row() == self.cnt-1:
            return
        else:
            self.리스트.setCurrentIndex(self.내용.index(self.리스트.currentIndex().row()+1,0))
            self.slt()
    
    def edit(self):
        if(self.txt이름.text() != "") and (self.txt주소.text() !=""):
            try:
                self.cmd = "update test2 set `name` = '{}', `add` = '{}' where `no` ={}".format(self.txt이름.text(), self.txt주소.text(), self.txt번호.text())
                print(self.cmd)
                self.cur.execute(self.cmd)
                self.conn.commit()
            except:
                QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요", QMessageBox.Yes, QMessageBox.Yes)
                return
        else: 
            QMessageBox.information(self, "입력 오류", "빈칸 없이 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            return
        QMessageBox.information(self, "수정 성공", "수정되었습니다.", QMessageBox.Yes, QMessageBox.Yes)    
    
        

    def slt(self):
        self.txt번호.setText(str(self.내용.index(self.리스트.currentIndex().row(),0).data()))
        self.txt이름.setText(self.내용.index(self.리스트.currentIndex().row(),1).data())
        self.txt주소.setText(self.내용.index(self.리스트.currentIndex().row(),2).data())


    def new(self):
        # self.cur.execute("select count(*) from test2")
        # self.conn.commit()
        # self.cnt = self.cur.fetchone()
        k.show()

    def resizeEvent(self, QResizeEvent):
        self.btnX = self.width() - 220
        self.btnY = self.height() - 60

        self.cmd이전.move(self.btnX, self.btnY)      
        self.cmd다음.move(self.btnX+self.btnSize*1, self.btnY)
        self.cmd신규.move(self.btnX+self.btnSize*2, self.btnY)
        self.cmd수정.move(self.btnX+self.btnSize*3, self.btnY)
        self.cmd삭제.move(self.btnX+self.btnSize*4, self.btnY)        


    def closeEvent(self, QCloseEvent):
        # print('close!')
        self.conn.close()

    def enterEvent(self, QEvent):
        self.cmd = "select * from test2"
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

        for i in range(len(ar)):
            self.내용.removeRow(i)
            self.내용.insertRow(i)
            self.내용.setData(self.내용.index(i,0),ar[i][0])
            self.내용.setData(self.내용.index(i,1),ar[i][1])
            self.내용.setData(self.내용.index(i,2),ar[i][2])



# if __name__ == '__main__':
app = QApplication(sys.argv)
w = sql()
k = insert()
sys.exit(app.exec_())
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_()) 