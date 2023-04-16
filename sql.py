import sqlite3 as sq
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_logonui import * 
from ui_sqlui import * 
from teacherui import *
from ui_studentui import *


_translate = QtCore.QCoreApplication.translate
class teWindow(QMainWindow, Ui_teacherWindow):
    def __init__(self, parent=None):
        super(teWindow, self).__init__(parent)
        self.setupUi(self)

        
class studentWindow(QMainWindow, Ui_studentWindow):
    def __init__(self, parent=None):
        super(studentWindow, self).__init__(parent)
        self.setupUi(self)
        self.fafther_window = MyWindow
        self.pushButton.clicked.connect(self.displayit)#############

    def displayit(self):
        conn = sq.connect('Dommanager.db')
        value = (x1,)
        cur = conn.cursor()
        cur.execute('SELECT * FROM userinfo WHERE Stunumber = ?',value)
        value1 = cur.fetchall()
        valset = "您查询到的学号为" + str(value1[0][0]) +"\n"+ "姓名为"+str(value1[0][1]) +"\n"+"寝室号为" +str(value1[0][2])+"\n"+" 专业为" + str(value1[0][3])
        self.textlabel.setText(_translate("MainWindow",valset))
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.child_window = sqlWindow()
        self.teacher_window = teWindow()
        self.student_window = studentWindow()

    def returnx(self):
        return self.username.text()
    def logonit(self):
        conn = sq.connect('Dommanager.db')
        cur = conn.cursor()
        global x1
        x1=self.username.text()
        y=self.password.text()
        cur.execute('SELECT * FROM U_PW WHERE USERNAME=? AND PASSWORD=? AND CHARACTOR="teacher"',(x1,y))
        if (cur.fetchall()):
                self.teacher_window.show()
        cur.execute('SELECT * FROM U_PW WHERE USERNAME=? AND PASSWORD=? AND CHARACTOR="student"',(x1,y))
        if (cur.fetchall()):
                self.student_window.show()
        if(self.username.text()=="admin" and  self.password.text()):
            
            cur.execute('SELECT * FROM U_PW WHERE USERNAME=? AND PASSWORD=?',(x1,y))
            if (cur.fetchall()):
                self.child_window.show()
            else:
                self.logonsele.setText(_translate("MainWindow", "账户或密码错误！"))

        
class sqlWindow(QMainWindow, Ui_childWindow):
    def __init__(self, parent=None):
        super(sqlWindow, self).__init__(parent)
        self.setupUi(self)
        self.isver.clicked.connect(self.verit)
    def verit(self):
        conn = sq.connect('Dommanager.db')
        cur = conn.cursor()
        
        x = (self.verbox.text(),)
        cur.execute('SELECT * FROM verifyis')
        cur.execute('drop table verifyis')
        cur.execute('CREATE TABLE verifyis (verifynum int primary key)')
        cur.execute('REPLACE INTO verifyis VALUES(?)',x)
        conn.commit()
        
           
def check(db_name,table_name):
    conn = sq.connect(db_name)
    cursor = conn.cursor()
    sql = '''SELECT tbl_name FROM sqlite_master WHERE type = 'table' '''
    cursor.execute(sql)
    values = cursor.fetchall()
    tables = []
    for v in values:
        tables.append(v[0])
    if table_name not in tables:
        return False # 可以建表
    else:
        return True # 不能建表



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.logon.clicked.connect(myWin.logonit)
    myWin.show()
    
    
    conn = sq.connect('Dommanager.db')
    cur = conn.cursor()
    if (check("Dommanager.db","userinfo") == False):
        cur.execute('CREATE TABLE userinfo (Stunumber int primary key,Name VARCHAR(255),roomnum int,major VARCHAR(255))')
    if (check("Dommanager.db","U_PW") == False):
        cur.execute('CREATE TABLE U_PW (USERNAME  primary key,PASSWORD VARCHAR(255),CHARACTOR VARCHAR(255))')
        cur.execute('INSERT INTO U_PW VALUES("admin","123456","adminstrator")')
        conn.commit()
    if (check("Dommanager.db","teacherinfo") == False):
        cur.execute('CREATE TABLE teacherinfo (teachernum VARCHAR(255) primary key,teachername VARCHAR(255))')
    if (check("Dommanager.db","verifyis") == False):
        cur.execute('CREATE TABLE verifyis (verifynum int primary key)')
    cur.close()
    conn.commit()
    conn.close()
    sys.exit(app.exec_())