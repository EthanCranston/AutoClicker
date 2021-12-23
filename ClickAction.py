from Instruction import Instruction


class Click(Instruction):
    def __init__(self, parent):
        super(Click, self).__init__("Click", parent)

    def preform_action(self):
        print("Clicked")