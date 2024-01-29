from PyQt5.QtWidgets import *
from UIs.RunningConfigUI import Ui_RunningConfiguration
from RunBox import MyRunBox

class MyRunningConfigurations(QWidget, Ui_RunningConfiguration):

    def __init__(self, scrollLayoutRunning: QVBoxLayout):
        super(MyRunningConfigurations, self).__init__()
        self.custom_window = MyRunBox()  # Creating an instance of MyRunBox
        scrollLayoutRunning.addWidget(self.custom_window)
        self.custom_window.ui.groupBox.setTitle("Running Configuration " + str(scrollLayoutRunning.count()))        

