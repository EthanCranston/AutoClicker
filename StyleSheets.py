from PyQt6.QtGui import QLinearGradient, QColor, QBrush, QPalette, QFont

gradientPalette1 = QPalette()
gradient1 = QLinearGradient(0, 0, 0, 400)
gradient1.setColorAt(0.0, QColor(56, 154, 193))
gradient1.setColorAt(1.0, QColor(25, 65, 81))
gradientPalette1.setBrush(QPalette.ColorRole.Window, QBrush(gradient1))

gradientPalette2 = QPalette()
gradient2 = QLinearGradient(0, 0, 0, 400)
gradient2.setColorAt(1.0, QColor(154, 154, 193))
gradient2.setColorAt(0, QColor(65, 65, 81))
gradientPalette2.setBrush(QPalette.ColorRole.Window, QBrush(gradient2))


transparentSS = 'background-color: #00000000'

mainCardBackgroundSS = 'background-color: #99f7f700; border-radius: 10%;'
settingsCardBackgroundSS = 'background-color: #99f7f7f7; border-radius: 10%;'

runningSS = 'background-color: #77b561'
notRunningSS = 'background-color: #b56163'

mainFont = QFont('Vendera', 10)