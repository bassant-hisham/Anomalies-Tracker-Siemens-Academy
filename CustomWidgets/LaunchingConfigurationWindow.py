from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from UIs.LaunchingConfigUI import Ui_launching_config
from commonFunctions import *
from DUTBox import MyDUTGroupBox

class MyLaunchingConfigWindow(QtWidgets.QWidget, Ui_launching_config):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(MyLaunchingConfigWindow, self).__init__()
        self.setupUi(self) # This sets up the UI components from the Launching Config window
        self.ToolConfigGroupBox.setCheckable(True)
        self.ToolConfigGroupBox.setChecked(False)
        self.toggle_content()
        self.ToolConfigGroupBox.toggled.connect(self.toggle_content)
        self.Add_PushButton.clicked.connect(self.add_dut_config)
        self.Duts = []

    def toggle_content(self):
        if self.ToolConfigGroupBox.isChecked():
            self.ToolConfigGroupBox.setMaximumHeight(16777215)
        else:
            self.ToolConfigGroupBox.setMaximumHeight(120)
            
    def add_dut_config(self):
        #self.scrollLayout.addWidget(MyDesignBox(self.scrollLayout.count()+1))
        new_dut_box = MyDUTGroupBox(self.lanch_conf_VLayout.count() - 2)
        self.lanch_conf_VLayout.addWidget(new_dut_box)
        # self.Design_data.append(new_design_box)
        self.Duts.append(new_dut_box)
    def get_Duts(self):
        return self.Duts
    
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()
