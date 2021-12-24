import sys #to brocker window evets
from PyQt6.QtWidgets import *
from MainWindow import MainWindow

from pynput import keyboard



app = QApplication(sys.argv)
window = MainWindow()


def on_press(key):
    #print(key)
    window.keyPressEvent(key)

# Collect events until released
listener = keyboard.Listener(on_press=on_press)
listener.start()


app.exec()
