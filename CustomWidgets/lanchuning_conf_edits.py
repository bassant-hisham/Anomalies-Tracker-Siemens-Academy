from lanchuining_conf_ui import Ui_lanchuning_config
from PyQt5 import QtCore, QtGui, QtWidgets
from AddDutConf import Add_DUTConfClass


class Ui_lanchuning_configEdits(Ui_lanchuning_config):
    def __init__(self, ui_lanchuning_config : Ui_lanchuning_config):
        self.ui_lanchuning_configObject=ui_lanchuning_config
        self.DutConfs_VLayout=QtWidgets.QVBoxLayout()
        self.ui_lanchuning_configObject.lanch_conf_VLayout.addLayout(self.DutConfs_VLayout)
        self.listGroupBoxes=list()
        self.DutConfCounter=0
        self.Add_DUTConf()
        self.RegisterSignals()

    def RegisterSignals(self) -> None:
        self.ui_lanchuning_configObject.Add_PushButton.clicked.connect(self.Add_DUTConf)

    def Add_DUTConf(self):
        self.DutConfCounter+=1
        self.DutObject=Add_DUTConfClass(self.ui_lanchuning_configObject,self.DutConfs_VLayout,self.DutConfCounter)
        self.listGroupBoxes.append(self.DutObject)
        


        


      


