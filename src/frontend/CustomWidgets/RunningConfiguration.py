from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.UIs.RunningConfigUI import Ui_RunningConfiguration
from src.frontend.CustomWidgets.RunBox import MyRunBox

class MyRunningConfigurations(QWidget, Ui_RunningConfiguration):

    def __init__(self, scrollLayoutRunning: QVBoxLayout):
        super(MyRunningConfigurations, self).__init__()
        self.custom_window = MyRunBox()  # Creating an instance of MyRunBox
        scrollLayoutRunning.addWidget(self.custom_window)
        
