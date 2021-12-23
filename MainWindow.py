from PyQt6.QtWidgets import *
from ActionSelection import ActionSelection


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__headInstruction = None
        self.setWindowTitle("Ethan's Auto Clicker")

        addButton = QPushButton("Add")
        addButton.clicked.connect(self.launch_action_selection)

        runButton = QPushButton("Run")
        runButton.clicked.connect(self.run)

        buttonBox = QHBoxLayout()
        buttonBox.addWidget(runButton)
        buttonBox.addWidget(addButton)

        self.__instructionBox = QVBoxLayout()

        mainBox = QVBoxLayout()

        mainBox.addLayout(self.__instructionBox)
        mainBox.addLayout(buttonBox)

        self.setLayout(mainBox)


        self.update_elements()
        self.show()


    def update_head(self):

        if self.__headInstruction == None: return
        while self.__headInstruction.prev() != None:
            self.__headInstruction = self.__headInstruction.prev()

    def update_elements(self):
        self.update_head()
        currentInstruction = self.__headInstruction


        self.clear_instruction_box()
        while currentInstruction != None:
            self.__instructionBox.addLayout(currentInstruction)
            currentInstruction = currentInstruction.next()



    def add_instruction(self, insruction):
        if self.__headInstruction == None:
            self.__headInstruction = insruction
        else:
            currentInstruction = self.__headInstruction
            count = 0
            while currentInstruction.next() != None:
                currentInstruction = currentInstruction.next()
                count += 1

            insruction.set_prev(currentInstruction)
            currentInstruction.set_next(insruction)

        self.update_elements()

    def print_instructions(self):
        currentInstruction = self.__headInstruction
        if currentInstruction == None: return

        while currentInstruction.next() != None:
            print(currentInstruction, end=' - ')
            currentInstruction = currentInstruction.next()
        print(currentInstruction)

    def clear_instruction_box(self):
        for i in reversed(range(self.__instructionBox.count())):
            current = self.__instructionBox.takeAt(i)
            self.__instructionBox.removeItem(current)

    def launch_action_selection(self):
        self.selector = ActionSelection(self)
        self.selector.show()

    def run(self):
        pass
