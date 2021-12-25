from Instruction import Instruction
from PyQt6.QtWidgets import *
from StyleSheets import *
from PyQt6.QtGui import QCursor

class MoveMouse(Instruction):
    def __init__(self, parent):
        super(MoveMouse, self).__init__("Move Mouse", parent)
        self.__editWindow = MoveMouseEditWindow(self)
        self.__editWindow.show()
        self.__mousePos = QCursor.pos()

    def set_mouse_position(self, pos):
        self.__mousePos = pos
        self.update_title(f"Move to {pos.x()}, {pos.y()}")  # From Instruction class

    def preform_action(self):
        QCursor.setPos(self.__mousePos)



class MoveMouseEditWindow(QWidget):
    def __init__(self, parent):
        super(MoveMouseEditWindow, self).__init__()
        self.__parent = parent
        self.setWindowTitle("Edit Mouse Location")
        self.__currentLocation = None

        instruction = QLabel("  Hover your mouse and press enter to set  ")
        instruction.setFont(mainFont)
        instruction.setStyleSheet(settingsCardBackgroundSS)
        instruction.setMinimumHeight(25)
        self.__currentPosLabel = QLineEdit("None")
        self.__currentPosLabel.setReadOnly(True)
        doneButton = QPushButton("Done")
        doneButton.clicked.connect(self.done_press)

        mainBox = QVBoxLayout()
        mainBox.addWidget(instruction)
        mainBox.addWidget(self.__currentPosLabel)
        mainBox.addWidget(doneButton)

        self.setPalette(gradientPalette2)
        self.setLayout(mainBox)



    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.__currentLocation = QCursor.pos()
            print(self.__currentLocation)
            self.__currentPosLabel.setText(f'{self.__currentLocation.x()}, {self.__currentLocation.y()}')




    def done_press(self):
        if self.__currentLocation == None: return

        self.__parent.set_mouse_position(self.__currentLocation)
        self.close()




