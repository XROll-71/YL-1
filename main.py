from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image, ImageDraw
import random


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawellips)

    def drawellips(self):
        image_width = 721
        image_height = 451

        image = Image.new('RGBA', (image_width, image_height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)

        circle_diameter = random.randint(20, 100)
        circle_center = (image_width // 2, image_height // 2)
        circle_color = (255, 255, 0, 255)

        draw.ellipse((circle_center[0] - circle_diameter // 2, circle_center[1] - circle_diameter // 2,
                      circle_center[0] + circle_diameter // 2, circle_center[1] + circle_diameter // 2),
                     fill=circle_color)

        pixmap = QPixmap.fromImage(
            QImage(image.tobytes("raw", "RGBA"), image_width, image_height, QImage.Format_RGBA8888))
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
