import sqlite3 as sq
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_childWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("childWindow")
        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.shangchuan = QtWidgets.QPushButton(self.centralwidget)
        self.shangchuan.setGeometry(QtCore.QRect(100, 280, 93, 28))
        self.shangchuan.setObjectName("shangchuan")
        self.shangchuan.clicked.connect(self.upload)

        self.isfind = QtWidgets.QPushButton(self.centralwidget)
        self.isfind.setGeometry(QtCore.QRect(540, 320, 93, 28))
        self.isfind.setObjectName("isfind")
        self.isfind.clicked.connect(self.findit)

        self.ischange = QtWidgets.QPushButton(self.centralwidget)
        self.ischange.setGeometry(QtCore.QRect(270, 470, 93, 28))
        self.ischange.setObjectName("ischange")
        self.ischange.clicked.connect(self.changeit)

        self.isdelete = QtWidgets.QPushButton(self.centralwidget)
        self.isdelete.setGeometry(QtCore.QRect(130, 470, 93, 28))
        self.isdelete.setObjectName("ischange")
        self.isdelete.clicked.connect(self.deleteit)
        
        self.isver = QtWidgets.QPushButton(self.centralwidget)
        self.isver.setGeometry(QtCore.QRect(360, 590, 93, 28))
        self.isver.setObjectName("isver")
        

        self.displayall = QtWidgets.QPushButton(self.centralwidget)
        self.displayall.setGeometry(QtCore.QRect(620, 420, 141, 101))
        self.displayall.setObjectName("displayall")
        self.displayall.clicked.connect(self.displayitall)




        self.verlab = QtWidgets.QLabel(self.centralwidget)
        self.verlab.setGeometry(QtCore.QRect(200,540,491, 31))
        self.verlab.setObjectName("verlab")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 61, 31))
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 71, 41))
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 72, 15))
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 220, 72, 15))
        self.label_4.setObjectName("label_4")


        self.sushe = QtWidgets.QLineEdit(self.centralwidget)
        self.sushe.setGeometry(QtCore.QRect(130, 70, 121, 31))
        self.sushe.setObjectName("sushe")


        self.xuehao = QtWidgets.QLineEdit(self.centralwidget)
        self.xuehao.setGeometry(QtCore.QRect(130, 120, 121, 31))
        self.xuehao.setObjectName("xuehao")


        self.xingmin = QtWidgets.QLineEdit(self.centralwidget)
        self.xingmin.setGeometry(QtCore.QRect(130, 170, 121, 31))
        self.xingmin.setObjectName("xingmin")


        self.zhuanye = QtWidgets.QLineEdit(self.centralwidget)
        self.zhuanye.setGeometry(QtCore.QRect(130, 210, 121, 31))
        self.zhuanye.setObjectName("zhuanye")

        self.verbox = QtWidgets.QLineEdit(self.centralwidget)
        self.verbox.setGeometry(QtCore.QRect(200, 590, 121, 31))
        self.verbox.setObjectName("verbox")


        self.stucheck = QtWidgets.QCheckBox(self.centralwidget)
        self.stucheck.setGeometry(QtCore.QRect(70, 250, 91, 19))
        self.stucheck.setObjectName("stucheck")


        self.teachercheck = QtWidgets.QCheckBox(self.centralwidget)
        self.teachercheck.setGeometry(QtCore.QRect(170, 250, 91, 19))
        self.teachercheck.setObjectName("teachercheck")

        self.numfind = QtWidgets.QCheckBox(self.centralwidget)
        self.numfind.setGeometry(QtCore.QRect(590, 50, 91, 19))
        self.numfind.setObjectName("numfind")


        self.score = QtWidgets.QCheckBox(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(590, 80, 91, 19))
        self.score.setObjectName("score")


        self.name = QtWidgets.QCheckBox(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(590, 110, 91, 19))
        self.name.setObjectName("name")


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(590, 140, 91, 19))
        self.checkBox.setObjectName("checkBox")


        self.findbox = QtWidgets.QLineEdit(self.centralwidget)
        self.findbox.setGeometry(QtCore.QRect(410, 80, 151, 51))
        self.findbox.setObjectName("findbox")





        self.display = QtWidgets.QTextBrowser(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(410, 160, 361, 151))
        self.display.setObjectName("display")




        self.score_2 = QtWidgets.QLabel(self.centralwidget)
        self.score_2.setGeometry(QtCore.QRect(70, 380, 91, 19))
        self.score_2.setObjectName("score_2")





        self.old = QtWidgets.QLineEdit(self.centralwidget)
        self.old.setGeometry(QtCore.QRect(140, 360, 151, 51))
        self.old.setObjectName("old")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 380, 72, 15))
        self.label_5.setObjectName("label_5")


        self.new_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(480, 360, 151, 51))
        self.new_2.setObjectName("new_2")





        self.score_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.score_3.setGeometry(QtCore.QRect(300, 370, 91, 19))
        self.score_3.setObjectName("score_3")


        self.name_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.name_3.setGeometry(QtCore.QRect(300, 400, 91, 19))
        self.name_3.setObjectName("name_3")


        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(300, 430, 91, 19))
        self.checkBox_3.setObjectName("checkBox_3")


        self.numfind_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.numfind_3.setGeometry(QtCore.QRect(300, 340, 91, 19))
        self.numfind_3.setObjectName("numfind_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")


        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")


        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.sushe)
        self.label_2.setBuddy(self.xuehao)
        self.label_3.setBuddy(self.xingmin)
        self.label_4.setBuddy(self.zhuanye)
        self.label_5.setBuddy(self.zhuanye)

        self.showtext = QtWidgets.QLabel(self.centralwidget)
        self.showtext.setGeometry(QtCore.QRect(10, 0, 171, 61))
        self.showtext.setObjectName("showtext")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def deleteit(self):
        conn = sq.connect('Dommanager.db')
        cur = conn.cursor()
        y=(self.new_2.text(),)
        if y:
            if self.numfind_3.isChecked():#宿舍号删除
           
                cur.execute('DELETE FROM userinfo WHERE roomnum= ? ',y)
                conn.commit()
                self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "删除成功"))

            if self.score_3.isChecked():#学号删除
            
                cur.execute('DELETE FROM userinfo WHERE Stunumber = ?',y)
                conn.commit()
                self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "删除成功"))

            if self.name_3.isChecked():#姓名删除
            
                cur.execute('DELETE FROM userinfo WHERE Name = ?',y)
                conn.commit()
                self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "删除成功"))
                
            if self.checkBox_3.isChecked():#专业删除
            
                cur.execute('DELETE FROM userinfo WHERE major = ?',y)
                conn.commit()
                self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "删除成功"))
        else:
            self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "删除内容为空！请重新输入"))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shangchuan.setText(_translate("MainWindow", "上传"))
        self.verlab.setText(_translate("MainWindow", "验证码"))
        self.label.setText(_translate("MainWindow", "宿舍号"))
        self.label_2.setText(_translate("MainWindow", "学号"))
        self.label_3.setText(_translate("MainWindow", "姓名"))
        self.label_4.setText(_translate("MainWindow", "专业"))
        self.numfind.setText(_translate("MainWindow", "宿舍号"))
        self.score.setText(_translate("MainWindow", "学号"))
        self.stucheck.setText(_translate("MainWindow", "学生"))
        self.teachercheck.setText(_translate("MainWindow", "老师"))
        self.name.setText(_translate("MainWindow", "姓名"))
        self.checkBox.setText(_translate("MainWindow", "专业"))
        self.isfind.setText(_translate("MainWindow", "查找"))
        self.isver.setText(_translate("MainWindow", "更改"))
        self.isdelete.setText(_translate("MainWindow", "删除"))
        self.score_2.setText(_translate("MainWindow", "学号"))

        self.label_5.setText(_translate("MainWindow", "更改为"))
        self.ischange.setText(_translate("MainWindow", "更改"))
        self.score_3.setText(_translate("MainWindow", "学号"))
        self.name_3.setText(_translate("MainWindow", "姓名"))
        self.checkBox_3.setText(_translate("MainWindow", "专业"))
        self.numfind_3.setText(_translate("MainWindow", "宿舍号"))
        self.displayall.setText(_translate("MainWindow", "显示所有"))


    def upload(self):#增加
        def check1(db_name,num):
            conn1 = sq.connect(db_name)
            cursor1 = conn1.cursor()
            sql = '''SELECT Stunumber FROM userinfo '''
            cursor1.execute(sql)
            values = cursor1.fetchall()
            nums = []
            for v in values:
                nums.append(v[0])
            if num not in nums:
                return False # 可以增加
            else:
                return True # 不能增加

        def check2(db_name,num):
            conn1 = sq.connect(db_name)
            cursor1 = conn1.cursor()
            sql = '''SELECT teachernum FROM teacherinfo '''
            cursor1.execute(sql)
            values = cursor1.fetchall()
            nums = []
            for v in values:
                nums.append(v[0])
            if num not in nums:
                return False # 可以增加
            else:
                return True # 不能增加

        _translate = QtCore.QCoreApplication.translate
        stunum = self.xuehao.text()
        roomnum = self.sushe.text()
        name = self.xingmin.text()
        major = self.zhuanye.text()
        data=(stunum,name,roomnum,major)
        if(stunum and roomnum and name and major):
            if(self.stucheck.isChecked()):
                if (check1("Dommanager.db",int(stunum)) == False):
                    conn = sq.connect('Dommanager.db')
                    cur = conn.cursor()
                    cur.execute('INSERT INTO userinfo values(?,?,?,?)',data)
                    conn.commit()
                    self.showtext.setText(_translate("MainWindow", "uploaded!"))
                else:
                    self.showtext.setText(_translate("MainWindow", "重复学号!"))
        elif (stunum and name):
            if(self.teachercheck.isChecked()):
                if (check2("Dommanager.db",int(stunum)) == False):
                        data1=(stunum,name)
                        conn = sq.connect('Dommanager.db')
                        cur = conn.cursor()
                        cur.execute('INSERT INTO teacherinfo values(?,?)',data1)
                        conn.commit()
                        self.showtext.setText(_translate("MainWindow", "uploaded!"))
                else:
                        self.showtext.setText(_translate("MainWindow", "重复工号!"))
            else:
                self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "新建内容为空！请重新输入"))
        else:
            self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "新建内容为空！请重新输入"))

    def findit(self, MainWindow):
        conn = sq.connect('Dommanager.db')
        cur = conn.cursor()
        cache = []
        x=(self.findbox.text(),)
        y=self.findbox.text()
        if y:
            self.display.append("学号，姓名，宿舍号，专业")
            if self.numfind.isChecked():#宿舍号查询
            
                cur.execute('SELECT * FROM userinfo WHERE roomnum=?',x)
                i=0
                values = cur.fetchall()
                print(values)
                while i<len(values):
                    self.display.append(str(values[i]))
                    i=i+1
                cache.append("宿舍号 ")

            if self.score.isChecked():#学号查询
            
                cur.execute('SELECT * FROM userinfo WHERE Stunumber=?',x)
                i=0
                values = cur.fetchall()
                print(values)
                while i<len(values):
                    self.display.append(str(values[i]))
                    i=i+1
                cache.append("学号 ")

            if self.name.isChecked():#姓名查询
            
                cur.execute('SELECT * FROM userinfo WHERE Name=?',x)
                i=0
                values = cur.fetchall()
                print(values)
                while i<len(values):
                    self.display.append(str(values[i]))
                    i=i+1
                cache.append("姓名 ")

            if self.checkBox.isChecked():#专业查询
            
                cur.execute('SELECT * FROM userinfo WHERE major=?',x)
                i=0
                values = cur.fetchall()
                print(values)
                while i<len(values):
                    self.display.append(str(values[i]))
                    i=i+1
                cache.append("专业 ")

            self.display.append("以上查询内容：")
            self.display.append(str(cache))
            self.display.append(self.findbox.text())
        else:
            self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "查询内容为空！请重新输入"))

    def changeit(self, MainWindow):
        conn = sq.connect('Dommanager.db')
        cur = conn.cursor()
        x=(self.old.text())
        y=(self.new_2.text())
        if(x and y):
            if self.numfind_3.isChecked():#宿舍号修改
           
                print(x)
                cur.execute('UPDATE userinfo SET roomnum = ? WHERE Stunumber = ?',(y,x))
                conn.commit()

            if self.score_3.isChecked():#宿舍号修改
            
                print(x)
                cur.execute('UPDATE userinfo SET Stunumber = ? WHERE Stunumber = ?',(y,x))
                conn.commit()

            if self.name_3.isChecked():#姓名修改
            
                print(x)
                cur.execute('UPDATE userinfo SET Name = ? WHERE Stunumber = ?',(y,x))
                conn.commit()

            if self.checkBox_3.isChecked():#专业修改
            
                print(x)
                cur.execute('UPDATE userinfo SET major = ? WHERE Stunumber = ?',(y,x))
                conn.commit()
        else:
            self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "修改内容为空！请重新输入"))
    def displayitall(self, MainWindow):
        conn = sq.connect('Dommanager.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM userinfo')
        values = cur.fetchall()
        self.display.setText("学号   姓名   宿舍号    专业")
        i=0
        while i<len(values):
                self.display.append(str(values[i]))
                i=i+1
        self.showtext.setText(QtCore.QCoreApplication.translate("MainWindow", "显示成功"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_childWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())