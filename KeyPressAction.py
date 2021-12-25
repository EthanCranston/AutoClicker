from Instruction import Instruction
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from StyleSheets import *

from pynput.keyboard import Key, Controller

class KeyPress(Instruction):
    def __init__(self, parent):
        super(KeyPress, self).__init__("Press Key", parent)
        self.__key = None
        self.__EditWindow = KeyPressEditWindow(self)
        self.__EditWindow.show()
        self.__keyboard = Controller()


    def set_key(self, key):
        self.__key = key[1]
        self.update_title(f"Press {str(key)}") #From Instruction class

    def preform_action(self):
        print("Key Pressed:", self.__key)


class KeyPressEditWindow(QWidget):
    def __init__(self, parent):
        super(KeyPressEditWindow, self).__init__()
        self.__parent = parent
        self.setWindowTitle("Edit Key Press")
        self.__currentKey = None

        instruction = QLabel("  Press which key you would like to use.  ")
        instruction.setFont(mainFont)
        instruction.setStyleSheet(settingsCardBackgroundSS)
        instruction.setMinimumHeight(25)
        self.__currentKeyLabel = QLineEdit("None")
        self.__currentKeyLabel.setReadOnly(True)
        doneButton = QPushButton("Done")
        doneButton.clicked.connect(self.done_press)

        mainBox = QVBoxLayout()
        mainBox.addWidget(instruction)
        mainBox.addWidget(self.__currentKeyLabel)
        mainBox.addWidget(doneButton)

        self.setPalette(gradientPalette2)
        self.setLayout(mainBox)

        self.__keymap = {}
        for key, value in vars(Qt.Key).items():
            if isinstance(value, Qt.Key):
                self.__keymap[value] = key.partition('_')[2]

        self.__modmap = {
            'NoModifier': '',
            'ControlModifier': self.__keymap[Qt.Key.Key_Control],
            'AltModifier': self.__keymap[Qt.Key.Key_Alt],
            'ShiftModifier': self.__keymap[Qt.Key.Key_Shift],
            'MetaModifier': self.__keymap[Qt.Key.Key_Meta],
            'GroupSwitchModifier': self.__keymap[Qt.Key.Key_AltGr],
            'KeypadModifier': self.__keymap[Qt.Key.Key_NumLock],
        }


    def keyPressEvent(self, event):

        self.__currentKey = [event.key(), event.modifiers()]
        self.__currentKeyLabel.setText(self.currentKey_to_text())


    def done_press(self):
        if self.__currentKey == None: return

        self.__parent.set_key((self.__currentKey, self.currentKey_to_text()))
        self.close()

    def currentKey_to_text(self):
        text = ''
        if self.__currentKey[1] != Qt.KeyboardModifier.NoModifier:
            for x in str(self.__currentKey[1]).split('.')[1].split('|'):
                text += self.__modmap[x] + ' + '

        key = self.__keymap[self.__currentKey[0]]
        text += key
        if text[-len(key)*2-3: -len(key)-3] == key:
            text = text[-len(key):]

        return text
