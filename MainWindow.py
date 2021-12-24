from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from ActionSelection import ActionSelection
from KeyPressAction import KeyPressEditWindow
from StyleSheets import *
from Worker import Worker


from PyQt6.QtGui import *
from PyQt6.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__headInstruction = None
        self.setWindowTitle("Ethan's Auto Clicker")

        self.__running = False
        self.__threadPool = QThreadPool()

        addButton = QPushButton("Add")
        addButton.clicked.connect(self.launch_action_selection)

        self.__startStopButton = QPushButton("Start/Stop")
        self.__startStopButton.clicked.connect(self.start_stop)

        buttonBox = QHBoxLayout()
        buttonBox.addWidget(self.__startStopButton)
        buttonBox.addWidget(addButton)

        self.__stopCommand = 'Escape'
        self.__stopLabel = QLabel('Start/Stop Command: ' + self.__stopCommand)
        self.__stopLabel.setFont(mainFont)
        self.__stopLabel.setStyleSheet(transparentSS)
        stopEditButton = QPushButton("Edit")
        stopEditButton.clicked.connect(self.change_stop_key)
        stopEditButton.setStyleSheet(transparentSS)

        stopFrame = QWidget()
        stopFrame.setStyleSheet(settingsCardBackgroundSS)
        stopFrame.setMaximumHeight(50)
        stopBox = QVBoxLayout(stopFrame)
        stopBox.addWidget(stopEditButton, alignment= Qt.AlignmentFlag.AlignLeft)
        stopBox.addWidget(self.__stopLabel)

        self.__instructionBox = QVBoxLayout()



        mainBox = QVBoxLayout()

        mainBox.addLayout(self.__instructionBox)
        mainBox.addLayout(buttonBox)
        mainBox.addWidget(stopFrame)

        self.setLayout(mainBox)


        self.setPalette(gradientPalette1)

        self.update_elements()
        self.show()


    def update_head(self):

        if self.__headInstruction == None: return
        while self.__headInstruction.prev() != None:
            self.__headInstruction = self.__headInstruction.prev()

    def update_elements(self):
        self.update_head()
        self.setMinimumHeight(40 * self.count_instruction() + 130)
        currentInstruction = self.__headInstruction


        self.clear_instruction_box()
        while currentInstruction != None:
            self.__instructionBox.addLayout(currentInstruction)
            currentInstruction = currentInstruction.next()

    def count_instruction(self):
        currentInstruction = self.__headInstruction
        count = 0
        while currentInstruction != None:
            currentInstruction = currentInstruction.next()
            count += 1
        return count

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
        self.selector = ActionSelection(self, self.size()*0.8)
        self.selector.show()

    def run(self):
        currentInstruction = None
        while self.__running:
            if currentInstruction == None:
                currentInstruction = self.__headInstruction
            currentInstruction.preform_action()
            currentInstruction = currentInstruction.next()

    def change_stop_key(self):
        self.__escapeEditWindow = KeyPressEditWindow(self) #Uses this window because it is the same
        self.__escapeEditWindow.show()

    def set_key(self, escapeKey): #Made to match function from KeyPressAction
        self.__stopCommand = escapeKey
        self.__stopLabel.setText('Stop command: ' + self.__stopCommand)

    def start_stop(self):
        if self.__headInstruction == None: return #cannot run without instruction
        self.__running = not self.__running
        if self.__running:
            self.__startStopButton.setStyleSheet(runningSS)

            worker = Worker(self.run)  # Any other args, kwargs are passed to the run function
            self.__threadPool.start(worker)

        else:
            self.__startStopButton.setStyleSheet('')
            self.__threadPool.clear()



