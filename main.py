import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests
from ui import Ui_MainWindow
import os


class YandexMapApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixmap = None
        self.latitude, self.longitude = 68.97917, 33.09251
        self.zoom = 10
        self.show_yandex_map()
        self.PgUp.clicked.connect(self.zoom_pl)
        self.PgDown.clicked.connect(self.zoom_mn)

    def show_yandex_map(self):
        params = {
            'll': f'{self.latitude},{self.longitude}',
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yam = YandexMapApp()
    yam.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
