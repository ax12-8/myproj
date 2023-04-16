from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sq
from ui_sqlui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(140, 150, 171, 31))
        self.username.setObjectName("username")


        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(140, 230, 171, 31))
        self.password.setObjectName("password")



        self.logon = QtWidgets.QPushButton(self.centralwidget)
        self.logon.setGeometry(QtCore.QRect(110, 290, 93, 28))
        self.logon.setObjectName("logon")
       

        

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 160, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 72, 15))
        self.label_2.setObjectName("label_2")
        self.username_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.username_2.setGeometry(QtCore.QRect(550, 110, 171, 31))
        self.username_2.setObjectName("username_2")
        self.password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_2.setGeometry(QtCore.QRect(550, 180, 171, 31))
        self.password_2.setObjectName("password_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 120, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 190, 72, 15))
        self.label_4.setObjectName("label_4")
        self.verified = QtWidgets.QLineEdit(self.centralwidget)
        self.verified.setGeometry(QtCore.QRect(550, 250, 171, 31))
        self.verified.setObjectName("verified")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 260, 72, 15))
        self.label_5.setObjectName("label_5")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(540, 340, 93, 28))
        self.register_2.setObjectName("register_2")
        self.register_2.clicked.connect(self.registerit)
        self.logonsele = QtWidgets.QLabel(self.centralwidget)
        self.logonsele.setGeometry(QtCore.QRect(50, 410, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(28)
        self.logonsele.setFont(font)
        self.logonsele.setText("")
        self.logonsele.setObjectName("logonsele")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logon.setText(_translate("MainWindow", "logon"))
        self.label.setText(_translate("MainWindow", "学号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "学号"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.label_5.setText(_translate("MainWindow", "验证码"))
        self.register_2.setText(_translate("MainWindow", " register"))
    
    def registerit(self):
        conn = sq.connect('Dommanager.db')
        cur = conn.cursor()
        regius=(self.username_2.text(),)
        regipw=(self.password_2.text(),)
        cur.execute('SELECT * FROM userinfo WHERE Stunumber = ?',regius)
        if (cur.fetchall()):
            cur.execute('INSERT INTO U_PW VALUES(?,?,"student")',(regius[0],regipw[0]))
        conn.commit()
        cur.execute('SELECT * FROM verifyis')
        x=cur.fetchall()
        print(self.verified.text())
        if(self.verified.text()):
            if int(self.verified.text())==int(x[0][0]):
                cur.execute('INSERT INTO U_PW VALUES(?,?,"teacher")',(regius[0],regipw[0]))
                conn.commit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
   