# Following along with:
# https://www.youtube.com/watch?v=ot94H3-d5d8

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Button & Label")
        # self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200,500,400)
        self.create_widgets()

    def create_widgets(self):
        btn = QPushButton("Click Me", self)
        btn.setGeometry(100,100,200,200)
        btn.setStyleSheet('background-color: red')
        btn.setIcon(QIcon("icon.png"))

        label = QLabel("My Label", self)
        label.setGeometry(100,75, 100,20)
        label.setStyleSheet('color: green')
        label.setFont(QFont("Monaco", 14))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())