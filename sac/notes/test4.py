from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

class MainWindow(QWidget):
    def __init__(self):
        # ...
        self.downloader = QNetworkAccessManager()

    def change_gif(self):
        self.loader_label.show()
        url = QUrl('https://path.to/animation.gif')
        self.device = self.downloader.get(QNetworkRequest(url))
        self.device.finished.connect(self.applyNewGif)

    def applyNewGif(self):
        self.loader_label.hide()
        self.newGif = QMovie()
        self.newGif.setDevice(self.device)
        self.gif_label.setMovie(self.newGif)
        self.newGif.start()
        self.gif_label.show()