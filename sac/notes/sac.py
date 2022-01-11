import os
import sys

from PyQt5.QtGui import QPixmap, QPaintDevice
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

SOURCE_FILE = '../source_images/expRedVideo.svg'


def show_svg(svg_widget, file_to_show):
    # print(QApplication.desktop().width())
    # print(QApplication.desktop().height())
    width = svg_widget.renderer().viewBox().width()
    height = svg_widget.renderer().viewBox().height()
    title = os.path.basename(file_to_show)

    svg_widget.setWindowTitle(f'{width}x{height} - {title}')
    svg_widget.setGeometry(100, 100, int(width / 4), int(height / 4))

    svg_widget.show()


app = QApplication(sys.argv)

svgWidget = QSvgWidget()
svgWidget.renderer().load(SOURCE_FILE)

show_svg(svgWidget, SOURCE_FILE)

# qpm = QPixmap()
# test = svgWidget.render(qpm)
# # t1.show()
# qpm.save('test.png')

sys.exit(app.exec_())
