import sys #to brocker window evets
from PyQt6.QtWidgets import *

from MainWindow import MainWindow



app = QApplication(sys.argv)

window = MainWindow()
app.exec()