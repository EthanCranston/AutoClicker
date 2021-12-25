from Instruction import Instruction
from PyQt6.QtWidgets import *
from StyleSheets import *

class MicroDelay(Instruction):
    def __init__(self, parent):
        super(MicroDelay, self).__init__("Delay", parent)
        self.__time = 0
        self.__EditWindow = DelayEditWindow(self)
        self.__EditWindow.show()

    def preform_action(self):
        counter = 0
        for x in range(self.__time):
            for i in range(self.__time):
                counter += 1


    def set_time(self, newTime):
        self.__time = int(float(newTime))
        self.update_title(f"Micro Delay {str(newTime)}")  # From Instruction class

class DelayEditWindow(QWidget):
    def __init__(self, parent):
        super(DelayEditWindow, self).__init__()
        self.__parent = parent
        self.setWindowTitle("Edit Delay")

        instruction = QLabel("  Micro Delay is Unitless  ")
        instruction.setFont(mainFont)
        instruction.setStyleSheet(settingsCardBackgroundSS)
        instruction.setMinimumHeight(25)

        self.__delayBox = QLineEdit()
        doneButton = QPushButton("Done")
        doneButton.clicked.connect(self.done_press)

        mainBox = QVBoxLayout()
        mainBox.addWidget(instruction)
        mainBox.addWidget(self.__delayBox)
        mainBox.addWidget(doneButton)

        self.setPalette(gradientPalette2)
        self.setLayout(mainBox)

    def done_press(self):
        if self.__delayBox.text() == '' or not self.__delayBox.text().replace('.','').isdigit(): return
        self.__parent.set_time(self.__delayBox.text())
        self.close()
