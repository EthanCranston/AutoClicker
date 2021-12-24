from Instruction import Instruction
from pynput.mouse import Button, Controller



class Click(Instruction):
    def __init__(self, parent):
        super(Click, self).__init__("Click", parent)
        self.__mouse = Controller()

    def preform_action(self):
        #print("click")
        self.__mouse.click(Button.left)

