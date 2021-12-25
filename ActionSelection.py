from PyQt6.QtWidgets import *
from ClickAction import Click
from KeyPressAction import KeyPress
from DelayAction import Delay
from MoveMouseAction import MoveMouse
from StyleSheets import *

class ActionSelection(QWidget):
    def __init__(self, parent, size):
        super(ActionSelection, self).__init__()
        self.__parent = parent
        self.setWindowTitle("Select Action")
        self.resize(size)

        actions = {'Click': Click, 'Key Press': KeyPress, 'Delay': Delay, 'Move Mouse': MoveMouse}

        mainBox = QVBoxLayout()
        for action in actions.items():
            newButton = QPushButton(action[0])
            newFunc = lambda: addActionFromSelection(self.sender())
            newButton.clicked.connect(newFunc)
            mainBox.addWidget(newButton)

        self.setPalette(gradientPalette2)
        self.setLayout(mainBox)

        def addActionFromSelection(sender):
            newClass = actions[sender.text()](self.__parent)
            self.__parent.add_instruction(newClass)
            self.close()

