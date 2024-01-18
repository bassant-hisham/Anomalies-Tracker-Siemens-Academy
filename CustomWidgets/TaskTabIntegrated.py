import os
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
        self.AddDesignB.clicked.connect(self.add_design)
        self.AddRunningConfgB.clicked.connect(self.add_running_config)
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.scrollLayoutRunning = QVBoxLayout(self.scrollAreaRunningConfig)
        self.scrollAreaWidgetContents_3.setLayout(self.scrollLayout)
        self.scrollAreaRunningConfig.setLayout(self.scrollLayoutRunning)
        self.AddDirectoryB.clicked.connect(self.toggle_directory)
        self.AddFileB.clicked.connect(self.toggle_file)
        self.BrowseEvnParentDirectoryB.clicked.connect(lambda: showDirectoryDialog(self,self.lineEditDatabasePath_2))
        self.BrowseEvnFilePathB.clicked.connect(lambda: showFileDialog(self,self.lineEditDatabasePath_5))
        self.Running_data=[]
        self.Design_data = []
        self.Builds = []
    
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

    def get_design(self):
        return self.Design_data
    def get_running(self):
        return self.Running_data
        
    def add_running_config(self):
        new_running_box = MyRunningConfigurations(self.scrollLayoutRunning)
        self.Running_data.append(new_running_box)  
    def envData(self):
        file_path = self.lineEditDatabasePath_5.text()
        parent_dir = self.lineEditDatabasePath_2.text()
        StartRange = 0
        EndRange = 0
        if self.radioButton_2.isChecked():
            StartRange = self.lineEditDatabasePath_3.text()
            EndRange = self.lineEditDatabasePath_4.text()

        elif self.radioButton_3.isChecked():
            StartRange = self.lineEditDatabasePath_7.text()
            EndRange = self.lineEditDatabasePath_6.text()

        if self.radioButton.isChecked():
            bash_files = [f for f in os.listdir(parent_dir) if f.endswith(".bash")]
            for file_name in bash_files:
                self.Builds.append(file_name)
        else :
            start_value = int(StartRange) 
            end_value = int(EndRange) 
            for i in range(start_value, end_value + 1):
                file_name = f"vved{i}.bash"
                if os.path.exists(os.path.join(parent_dir, file_name)):
                    self.Builds.append(file_name)
        print (self.Builds)
