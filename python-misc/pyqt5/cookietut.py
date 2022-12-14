# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\cookietest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 691, 421))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(".\\images/cookie.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.cookie = QtWidgets.QPushButton(self.centralwidget)
        self.cookie.setGeometry(QtCore.QRect(150, 450, 121, 51))
        self.cookie.setObjectName("cookie")
        self.garden = QtWidgets.QPushButton(self.centralwidget)
        self.garden.setGeometry(QtCore.QRect(410, 450, 141, 51))
        self.garden.setObjectName("garden")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # defined a few lines down
        self.cookie.clicked.connect(self.show_cookie)
        self.garden.clicked.connect(self.show_garden)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #define image button methods
    def show_cookie(self):
        self.photo.setPixmap(QtGui.QPixmap(".\\images/cookie.png"))
    def show_garden(self):
        self.photo.setPixmap(QtGui.QPixmap(".\\images/farm.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cookie.setText(_translate("MainWindow", "Cookie"))
        self.garden.setText(_translate("MainWindow", "Garden"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
