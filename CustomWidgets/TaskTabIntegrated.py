from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from UIs.TaskTabUI import Ui_Task_Tab
from commonFunctions import *
from DesignBox import MyDesignBox
from AddRuntime import MyRunningConfigurations


class MyTaskTab(QtWidgets.QWidget, Ui_Task_Tab):
    def __init__(self):
        super(MyTaskTab, self).__init__()
        self.setupUi(self)  # This sets up the UI components from the TaskTab section
        self.widget.hide()
        self.widget_2.hide()
        self.pushButton.clicked.connect(self.add_design)
        self.pushButton_4.clicked.connect(self.add_running_config)
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.scrollLayoutRunning = QVBoxLayout(self.scrollAreaRunningConfig)
        self.scrollAreaWidgetContents_3.setLayout(self.scrollLayout)
        self.scrollAreaRunningConfig.setLayout(self.scrollLayoutRunning)
        self.pushButton_2.clicked.connect(self.toggle_directory)
        self.pushButton_3.clicked.connect(self.toggle_file)
        self.toolButtonBrowseDatabase_3.clicked.connect(lambda: showDirectoryDialog(self,self.lineEditDatabasePath_2))
        self.toolButtonBrowseDatabase_4.clicked.connect(lambda: showFileDialog(self,self.lineEditDatabasePath_5))
        self.Running_data=[]
        self.Design_data = []
    
    def toggle_directory(self):
        self.widget.show()
        if self.widget_2.isVisible():
            self.widget_2.hide()
            
    def toggle_file(self):
        self.widget_2.show()
        if self.widget.isVisible():
            self.widget.hide()
    def add_design(self):
        #self.scrollLayout.addWidget(MyDesignBox(self.scrollLayout.count()+1))
        new_design_box = MyDesignBox(self.scrollLayout.count() + 1)
        self.scrollLayout.addWidget(new_design_box)
        self.Design_data.append(new_design_box)

    def GetDesign(self):
        return self.Design_data
        
    def add_running_config(self):
        new_running_box = MyRunningConfigurations(self.scrollLayoutRunning)
        self.Running_data.append(new_running_box)     