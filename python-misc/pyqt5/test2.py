from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(1500,500,500,500)
        self.setWindowTitle("F26")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label.")
        self.label.move(100,100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.move(100,150)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button.")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()