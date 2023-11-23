import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt
from random import randint

class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.diameter = 0
        self.create_yellow_circle_button.clicked.connect(self.drawCircle)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)
        painter.setBrush(Qt.yellow)
        painter.drawEllipse(170, 50, self.diameter, self.diameter)

    def drawCircle(self):
        self.diameter = randint(20, 200)
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
