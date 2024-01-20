from UIs.ComodelsConfigBoxUI import Ui_ComodelsConfigBox
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class MyComodelsConfigGroupBox(QtWidgets.QGroupBox, Ui_ComodelsConfigBox):
    def __init__(self,id):
        super(MyComodelsConfigGroupBox, self).__init__()
        self.setupUi(self)
        self.setTitle("Config " + str(id))
