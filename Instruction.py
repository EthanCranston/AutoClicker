from abc import abstractmethod

from PyQt6.QtCore import Qt
#from PyQt6.QtGui import Qt
from PyQt6.QtWidgets import *
from StyleSheets import *



class Instruction(QHBoxLayout):
    def __init__(self, title, parent):
        super(Instruction, self).__init__()
        self.__frame = QWidget()
        self.__frame.setStyleSheet("background-color: #99dbd225; border-radius: 10%;")
        self.__frame.setMaximumHeight(50)

        self.__mainBox = QHBoxLayout(self.__frame)

        self.__next = None
        self.__prev = None
        self.__parent = parent

        self.__deleteButton = QPushButton("X")
        self.__deleteButton.setStyleSheet(transparentSS)
        self.__deleteButton.clicked.connect(self.delete)

        self.__mainBox.addWidget(self.__deleteButton, alignment=Qt.AlignmentFlag.AlignLeft)

        self.__titleLabel = QLabel(title)
        self.__titleLabel.setStyleSheet(transparentSS)
        self.__mainBox.addWidget(self.__titleLabel)
        self.__title = title

        self.__upButton = QPushButton("▲")
        self.__upButton.setStyleSheet(transparentSS)
        self.__upButton.clicked.connect(self.shift_up)
        self.__downButton = QPushButton("▼")
        self.__downButton.setStyleSheet(transparentSS)
        self.__downButton.clicked.connect(self.shift_down)

        buttonBox = QVBoxLayout()
        buttonBox.addWidget(self.__upButton, alignment=Qt.AlignmentFlag.AlignRight)
        buttonBox.addWidget(self.__downButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.__mainBox.addLayout(buttonBox)
        self.addWidget(self.__frame)


    def set_next(self, next):
        self.__next = next

    def set_prev(self, prev):
        self.__prev = prev

    def next(self):
        return self.__next

    def prev(self):
        return self.__prev

    def shift_down(self):
        if self.next() == None: return #Cannot go down
        top = self.prev()
        bottom = self.next().next()

        self.next().set_next(self)
        self.next().set_prev(top)

        self.set_prev(self.next())
        self.set_next(bottom)

        if top != None: top.set_next(self.prev())
        if bottom != None: bottom.set_prev(self)


        self.__parent.update_elements()


    def shift_up(self):
        if self.prev() == None: return  # Cannot go down
        top = self.prev().prev()
        bottom = self.next()

        self.prev().set_next(bottom)
        self.prev().set_prev(self)

        self.set_next(self.prev())
        self.set_prev(top)

        if top != None: top.set_next(self)
        if bottom != None: bottom.set_prev(self.next())

        self.__parent.update_elements()

    def update_title(self, newTitle):
        self.__title = newTitle
        self.__titleLabel.setText(newTitle)

    def delete(self):
        if self.prev() != None: self.prev().set_next(self.next())
        if self.next() != None: self.next().set_prev(self.prev())

        self.__parent.update_elements()
        self.__frame.hide()


    @abstractmethod
    def preform_action(self):
        pass

    @abstractmethod
    def edit(self):
        pass


    def __repr__(self):
        return self.__title
    def __str__(self):
        return self.__title

