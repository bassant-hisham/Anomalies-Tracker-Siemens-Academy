from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from launching_conf import Ui_launching_config
from lanchuning_conf_edits import Ui_lanchuning_configEdits


class LaunchingConfigurations(QtWidgets.QWidget,Ui_launching_config):
    def __init__(self):
        super(LaunchingConfigurations, self).__init__()
        self.setupUi(self)
        self.lanchuning_conf_editsObject = Ui_lanchuning_configEdits(self)
        self.launching_configurations = {}
    # def saveConfiguration(self):
    #     self.launching_configurations['']
    # def closeEvent(self, event):
    #     # This method is called when the window is about to be closed
    #     # self.saveConfiguration()
        # print(self.lanchuning_conf_editsObject.listGroupBoxes[0])
    #     event.accept()
        