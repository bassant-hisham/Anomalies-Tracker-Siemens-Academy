from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.UIs.RunningConfigUI import Ui_RunningConfiguration
from src.frontend.CustomWidgets.RunBox import MyRunBox
from src.frontend.CustomWidgets.commonFunctions import *


class MyRunningConfigurations(QWidget, Ui_RunningConfiguration):

    def __init__(self, scrollLayoutRunning: QVBoxLayout):
        super(MyRunningConfigurations, self).__init__()
        self.custom_window = MyRunBox()  # Creating an instance of MyRunBox
        scrollLayoutRunning.addWidget(self.custom_window)
        self.custom_window.ui.groupBox.setTitle("Running Configuration " + str(scrollLayoutRunning.count()))
        self.custom_window.toolButtonBrowseOutput_2.clicked.connect(lambda: showFileDialog(self,self.custom_window.lineEditOutputDirectory_2))  
        

