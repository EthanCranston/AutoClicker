from abc import abstractmethod

from PyQt6.QtWidgets import *



class Instruction(QHBoxLayout):
    def __init__(self, title, parent):
        super(Instruction, self).__init__()
        self.__next = None
        self.__prev = None
        self.__parent = parent

        self.__deleteButton = QPushButton("x")
        self.__deleteButton.clicked.connect(self.delete)
        self.addWidget(self.__deleteButton)


        self.__titleLabel = QLabel(title)
        self.addWidget(self.__titleLabel)
        self.__title = title

        self.__upButton = QPushButton("▲")
        self.__upButton.clicked.connect(self.shift_up)
        self.__downButton = QPushButton("▼")
        self.__downButton.clicked.connect(self.shift_down)


        buttonBox = QVBoxLayout()
        buttonBox.addWidget(self.__upButton)
        buttonBox.addWidget(self.__downButton)

        self.addLayout(buttonBox)


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
        self.hide()


    def hide(self):
        self.__deleteButton.hide()
        self.__titleLabel.hide()
        self.__downButton.hide()
        self.__upButton.hide()

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

