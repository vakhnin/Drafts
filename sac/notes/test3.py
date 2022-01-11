import os
import sys

from PyQt5.QtCore import QSize, Qt, QDir, QByteArray
from PyQt5.QtGui import QPixmap, QPainter, QMovie
from PyQt5.QtSvg import QSvgRenderer, QSvgWidget
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

render = QSvgRenderer('../source_images/expRedVideo.svg')
svg_wdgt = QSvgWidget('../source_images/expRedVideo.svg')


size = QSize(render.defaultSize())
pix = QPixmap(size)
pix.fill(Qt.transparent)

label = QLabel()
label.setPixmap(pix)
label.setAlignment(Qt.AlignCenter)
label.setScaledContents(True)
label.setGeometry(100, 100, int(size.width()/4), int(size.height() /4))

newGif = QMovie('../source_images/expRedVideo.svg', QByteArray(), label)
print(newGif.supportedFormats())
# newGif.setDevice(self.device)
label.setMovie(newGif)
newGif.start()
newGif.loopCount()
label.show()
#
# dir_ = QDir()
# if not dir_.exists('result'):
#     dir_.mkdir('result')
# pix.save('result' + os.sep + 'test.png', format='PNG')
#
# label.show()

sys.exit(app.exec_())
