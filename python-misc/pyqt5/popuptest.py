# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\popuptest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 411)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.popup_button = QtWidgets.QPushButton(self.centralwidget)
        self.popup_button.setGeometry(QtCore.QRect(130, 80, 321, 171))
        self.popup_button.setObjectName("popup_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.popup_button.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.popup_button.setText(_translate("MainWindow", "Show Popup"))

    def show_popup(self):
        msg = QMessageBox() # start by making an instance of this class to make a msgbox
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main text")
        # msg.setIcon(QMessageBox.Critical) # critical popup, like an error, red stop sign
        # msg.setIcon(QMessageBox.Warning) # warning, with yellow triangle !
        # msg.setIcon(QMessageBox.Information) # Information, blue circle with i
        msg.setIcon(QMessageBox.Question) # Question, blue circle with ?

        # define which buttons will be on the msgbox (separate by | pipe)
        # QMessageBox.[] where [] can be: Ok, Open, Save, Cancel, Close, Yes, No, Abort, Retry, Ignore
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        # change order/default
        msg.setDefaultButton(QMessageBox.Ignore)
        # Show informative text
        msg.setInformativeText("Informative text, yeah.")
        # Show detailed text
        msg.setDetailedText("Details here")


        msg.buttonClicked.connect(self.pop_button)

        x = msg.exec_() # needed for the messagebox to actually open

    #print to console what button was used to close popup msgbox
    def pop_button(self, i):
        print(i.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())