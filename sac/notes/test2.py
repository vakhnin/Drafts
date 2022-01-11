import os
import sys
import time

from PyQt5.QtCore import QSize, Qt, QDir, QPoint, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtSvg import QSvgRenderer, QSvgWidget
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

render = QSvgRenderer('../source_images/expRedVideo.svg')
svg_wdgt = QSvgWidget('../source_images/expRedVideo.svg')

size = QSize(render.defaultSize())
pix = QPixmap(size)
pix.fill(Qt.transparent)

# painter = QPainter(pix)
# painter.setRenderHint(QPainter.Antialiasing)
# render.setCurrentFrame(100)
# print(render.currentFrame())
# print(render.framesPerSecond())
# render.render(painter)
# painter.end()


# svg_wdgt.renderer().setCurrentFrame(1000)
# svg_wdgt.render(pix)
svg_wdgt.setGeometry(100, 100, int(size.width() / 4), int(size.height() / 4))
# svg_wdgt.show()

# svg_wdgt.render(pix)

# render.render(pix)
# pix.convertFromImage(render.render(painter))
# print(render.currentFrame())

svg_wdgt.renderer().setCurrentFrame(1)


print(svg_wdgt.renderer().currentFrame())
# pix = svg_wdgt.grab(QRect(QPoint(0, 0), size))
print(svg_wdgt.renderer().currentFrame())

label = QLabel()
label.setPixmap(pix)
label.setAlignment(Qt.AlignCenter)
label.setScaledContents(True)
label.setGeometry(100, 100, int(size.width() / 4), int(size.height() / 4))

dir_ = QDir()
if not dir_.exists('result'):
    dir_.mkdir('result')
pix.save('result' + os.sep + 'test.png', format='PNG')

label.show()

sys.exit(app.exec_())
