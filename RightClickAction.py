from Instruction import Instruction
import mouse



class RightClick(Instruction):
    def __init__(self, parent):
        super(RightClick, self).__init__("Click", parent)

    def preform_action(self):
        mouse.click('right')