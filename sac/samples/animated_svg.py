import sys

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication

# if there is only ANIMATE below (without ANIMATETRANSFORM), animated() returns false and no animation is shown.
# with both, animated() returns true and only animateTransform plays.

svg_str = """
<svg width="120"
     height="120"
     viewBox="0 0 120 120"
     version="1.1"
     xmlns="http://www.w3.org/2000/svg">

  <rect x="10" y="10" width="100" height="100">
    <animateTransform
        attributeName="transform"
        begin="0s"
        dur="20s"
        type="rotate"
        from="0 60 60"
        to="360 60 60"
        repeatCount="indefinite"
        />
    <animate 
        attributeName="x"
        from="-100"
        to="120"
        dur="10s"
        repeatCount="indefinite"
        begin="0s" />
  </rect>
</svg>
"""

svg_bytes = bytearray(svg_str, encoding='utf-8')

app = QApplication(sys.argv)

svgWidget = QSvgWidget()
svgWidget.renderer().load(svg_bytes)
svgWidget.setGeometry(100, 100, 300, 300)
svgWidget.show()

print(svgWidget.renderer().isValid())
print(svgWidget.renderer().animated())

sys.exit(app.exec_())
