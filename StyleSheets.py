from PyQt6.QtGui import QLinearGradient, QColor, QBrush, QPalette, QConicalGradient

gradientPalette = QPalette()
gradient = QLinearGradient(0, 0, 0, 400)
gradient.setColorAt(0.0, QColor(56, 154, 193))
gradient.setColorAt(1.0, QColor(25, 65, 81))
gradientPalette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))

transparentSS = 'background-color: #00000000'