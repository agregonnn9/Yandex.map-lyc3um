import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
import requests
from ui import Ui_MainWindow
import os


class YandexMapApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixmap = None
        self.zoom = 10
        self.step_for_zoom = {0: 10.0, 1: 5.0, 2: 4.0, 3: 2.0, 4: 2.0, 5: 1.5, 6: 1.5, 7: 1.0, 8: 1.0, 9: 0.1, 10: 0.1,
                              11: 0.01, 12: 0.01, 13: 0.01, 14: 0.001, 15: 0.001, 16: 0.001, 17: 0.001, 18: 0.0001,
                              19: 0.0001, 20: 0.0001, 21: 0.0001}
        self.step = self.step_for_zoom[self.zoom]

        self.latitude, self.longitude = 68.97917, 33.09251
        self.show_yandex_map()
        self.PgUp.clicked.connect(self.zoom_pl)
        self.PgDown.clicked.connect(self.zoom_mn)

    def show_yandex_map(self):
        params = {
            'll': f'{self.longitude},{self.latitude}',
            'z': self.zoom,
            'l': 'map'
        }
        response = requests.get('https://static-maps.yandex.ru/1.x/', params=params)

        with open('map.png', 'wb') as f:
            f.write(response.content)

        self.pixmap = QPixmap('map.png')
        self.label.setPixmap(self.pixmap)

    def closeEvent(self, a0):
        os.remove('map.png')

    def zoom_pl(self):
        if self.zoom != 21:
            self.zoom += 1
            self.show_yandex_map()

    def zoom_mn(self):
        if self.zoom != 0:
            self.zoom -= 1
            self.show_yandex_map()

    def keyPressEvent(self, event):
        self.step = self.step_for_zoom[self.zoom]
        if event.key() == Qt.Key_W:
            if self.latitude + self.step <= 90:
                self.latitude += self.step
            else:
                self.latitude = 90
        elif event.key() == Qt.Key_S:
            if self.latitude - self.step >= -90:
                self.latitude -= self.step
            else:
                self.latitude = -90
        elif event.key() == Qt.Key_A:
            if self.longitude - self.step >= -180:
                self.longitude -= self.step
            else:
                self.longitude = -180

        elif event.key() == Qt.Key_D:
            if self.longitude + self.step <= 180:
                self.longitude += self.step
            else:
                self.longitude = 180
        self.show_yandex_map()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yam = YandexMapApp()
    yam.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
