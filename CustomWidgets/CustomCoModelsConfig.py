from PyQt5 import QtCore, QtGui, QtWidgets

from UIs.CustomComodelsConfigUI import Ui_CustomComodelsConfig_Form
from ComodelsConfigBox import MyComodelsConfigGroupBox

class CustomCoModelsConfig(QtWidgets.QWidget, Ui_CustomComodelsConfig_Form):
    def __init__(self):
        super(CustomCoModelsConfig, self).__init__()
        self.setupUi(self)
        self.CustomComodelsAdd_PushButton.clicked.connect(self.add_comodel_config)
        
    def add_comodel_config(self):
        self.ConfigVLayout.addWidget(MyComodelsConfigGroupBox(self.ConfigVLayout.count() + 2))
        