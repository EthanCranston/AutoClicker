from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time
import traceback
import sys

class Worker(QRunnable):

    def __init__(self, fn):
        super(Worker, self).__init__()
        self.fn = fn

    @pyqtSlot()
    def run(self):
        self.fn()

