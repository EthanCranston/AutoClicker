from Instruction import Instruction
import mouse



class LeftClick(Instruction):
    def __init__(self, parent):
        super(LeftClick, self).__init__("Left Click", parent)

    def preform_action(self):
        mouse.click('left')


