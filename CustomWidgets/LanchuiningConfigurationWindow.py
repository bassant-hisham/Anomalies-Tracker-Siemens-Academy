from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from launching_conf import Ui_launching_config
from lanchuning_conf_edits import Ui_lanchuning_configEdits
from commonFunctions import *

class LaunchingConfigurations(QtWidgets.QWidget,Ui_launching_config):
    def __init__(self):
        super(LaunchingConfigurations, self).__init__()
        self.setupUi(self)
        self.lanchuning_conf_editsObject = Ui_lanchuning_configEdits(self)
        self.launching_configurations = {}
        self.lanchuning_conf_editsObject.DutObject.DutConfgObject.ReplyDir_toolButton.clicked.connect(lambda: showFileDialog(self,self.lanchuning_conf_editsObject.DutObject.DutConfgObject.ReplyDir_lineEdit))  
        self.lanchuning_conf_editsObject.DutObject.DutConfgObject.RecordDir_toolButton.clicked.connect(lambda: showDirectoryDialog(self,self.lanchuning_conf_editsObject.DutObject.DutConfgObject.ReplyDir_lineEdit))  
    # def saveConfiguration(self):
    #     self.launching_configurations['']
    # def closeEvent(self, event):
    #     # This method is called when the window is about to be closed
    #     # self.saveConfiguration()
        # print(self.lanchuning_conf_editsObject.listGroupBoxes[0])
    #     event.accept()
        