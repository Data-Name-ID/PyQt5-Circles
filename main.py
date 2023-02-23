import sys

from random import randint, choice
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_drawing = False
        self.colors = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Cyan',
            'Blue',
            'Magenta',
            'Purple',
            'Brown',
            'Black',
            'Pink',
        ]

        self.pushButton.clicked.connect(self.result)

    def result(self):
        self.is_drawing = True
        self.update()

    def paintEvent(self, event):
        if self.is_drawing:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        qp.setBrush(QColor(choice(self.colors)))

        for _ in range(randint(10, 20)):
            leigt = randint(30, 100)
            qp.drawEllipse(
                randint(0, self.width()),
                randint(0, self.height()),
                leigt,
                leigt,
            )

        self.is_drawing = False
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
