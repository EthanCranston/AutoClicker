from PyQt6.QtWidgets import *
from ClickAction import Click
from KeyPressAction import KeyPress
from DelayAction import Delay

class ActionSelection(QWidget):
    def __init__(self, parent):
        super(ActionSelection, self).__init__()
        self.__parent = parent
        self.setWindowTitle("Select Action")

        actions = {'Click': Click, 'Key Press': KeyPress, 'Delay': Delay}

        mainBox = QVBoxLayout()
        for action in actions.items():
            newButton = QPushButton(action[0])
            newFunc = lambda: addActionFromSelection(self.sender())
            newButton.clicked.connect(newFunc)
            mainBox.addWidget(newButton)

        self.setLayout(mainBox)

        def addActionFromSelection(sender):
            newClass = actions[sender.text()](self.__parent)
            self.__parent.add_instruction(newClass)
            self.close()

