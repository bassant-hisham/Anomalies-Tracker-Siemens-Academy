from PyQt5.QtWidgets import *
from UIs.RunningConfigUI import Ui_RunningConfiguration
from CustomRuntime import CustomRuntimeWindow
from commonFunctions import *


class MyRunningConfigurations(QWidget, Ui_RunningConfiguration):

    def __init__(self, scrollLayoutRunning: QVBoxLayout):
        super(MyRunningConfigurations, self).__init__()
        self.custom_window = CustomRuntimeWindow()  # Creating an instance of CustomRuntimeWindow
        scrollLayoutRunning.addWidget(self.custom_window)
        self.custom_window.ui.groupBox.setTitle("Running Configuration " + str(scrollLayoutRunning.count()))
        self.custom_window.toolButtonBrowseOutput_2.clicked.connect(lambda: showFileDialog(self,self.custom_window.lineEditOutputDirectory_2))  
        

