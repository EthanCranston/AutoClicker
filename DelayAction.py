from Instruction import Instruction
from PyQt6.QtWidgets import *


class Delay(Instruction):
    def __init__(self, parent):
        super(Delay, self).__init__("Delay", parent)
        self.__time = 0
        self.__EditWindow = DelayEditWindow(self)
        self.__EditWindow.show()

    def preform_action(self):
        print("Delayed")

    def set_time(self, newTime):
        self.__time = int(newTime)
        self.update_title(f"Delay {str(newTime)}ms")  # From Instruction class

class DelayEditWindow(QWidget):
    def __init__(self, parent):
        super(DelayEditWindow, self).__init__()
        self.__parent = parent
        self.setWindowTitle("Edit Delay")

        instruction = QLabel("Enter delay in milliseconds.")
        self.__delayBox = QLineEdit()
        doneButton = QPushButton("Done")
        doneButton.clicked.connect(self.done_press)

        mainBox = QVBoxLayout()
        mainBox.addWidget(instruction)
        mainBox.addWidget(self.__delayBox)
        mainBox.addWidget(doneButton)

        self.setLayout(mainBox)

    def done_press(self):
        if self.__delayBox.text() == '' or not self.__delayBox.text().isdigit(): return
        self.__parent.set_time(self.__delayBox.text())
        self.close()
