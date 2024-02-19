from PyQt5 import QtCore, QtGui, QtWidgets

from src.frontend.CustomWidgets.UIs.CustomComodelsConfigUI import Ui_CustomComodelsConfig_Form
from src.frontend.CustomWidgets.ComodelsConfigBox import MyComodelsConfigGroupBox

class CustomCoModelsConfig(QtWidgets.QWidget, Ui_CustomComodelsConfig_Form):
    def __init__(self):
        super(CustomCoModelsConfig, self).__init__()
        self.setupUi(self)
        self.comodelsList=list()
        coModelObj=MyComodelsConfigGroupBox(self.ConfigVLayout.count()+1,self.comodelsList,self.ConfigVLayout)
        self.ConfigVLayout.addWidget(coModelObj)
        self.CustomComodelsAdd_PushButton.clicked.connect(self.add_comodel_config)
        self.comodelsList.append(coModelObj)
        

        
    def add_comodel_config(self):
        coModelObj=MyComodelsConfigGroupBox(self.ConfigVLayout.count()+1,self.comodelsList,self.ConfigVLayout)
        self.ConfigVLayout.addWidget(coModelObj)
        self.comodelsList.append(coModelObj)


        