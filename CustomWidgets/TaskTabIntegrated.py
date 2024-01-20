import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from UIs.TaskTabUI import Ui_Task_Tab
from commonFunctions import *
from DesignBox import MyDesignBox
from RunningConfiguration import MyRunningConfigurations


class MyTaskTab(QtWidgets.QWidget, Ui_Task_Tab):
    def __init__(self):
        super(MyTaskTab, self).__init__()
        self.setupUi(self)  # This sets up the UI components from the TaskTab section
        self.Directory_widget.hide()
        self.File_widget.hide()
        self.AddDesign_button.clicked.connect(self.add_design)
        self.AddRunningConfig_button.clicked.connect(self.add_running_config)
        self.scrollLayout = QVBoxLayout(self.Designs_scrollAreaWidget)
        self.scrollLayoutRunning = QVBoxLayout(self.RunningConfig_scroll)
        self.Designs_scrollAreaWidget.setLayout(self.scrollLayout)
        self.RunningConfig_scroll.setLayout(self.scrollLayoutRunning)
        self.AddDirectory_button.clicked.connect(self.toggle_directory)
        self.AddFile_button.clicked.connect(self.toggle_file)
        self.BrowseParentDir_button.clicked.connect(lambda: showDirectoryDialog(self,self.ParentDir_lineEdit))
        self.BrowseFilePath_button.clicked.connect(lambda: showFileDialog(self,self.FilePath_lineEdit))
        self.Running_data=[]
        self.Design_data = []
        self.Builds = []
    
    def toggle_directory(self):
        self.Directory_widget.show()
        if self.File_widget.isVisible():
            self.File_widget.hide()
            
    def toggle_file(self):
        self.File_widget.show()
        if self.Directory_widget.isVisible():
            self.Directory_widget.hide()
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
    def get_builds(self):
        file_path = self.FilePath_lineEdit.text()
        parent_dir = self.ParentDir_lineEdit.text()
        StartRange = 0
        EndRange = 0
        if self.Range_radioButton.isChecked():
            StartRange = self.RangeFrom_lineEdit.text()
            EndRange = self.RangeTo_lineEdit.text()

        elif self.BinarySearch_radioButton.isChecked():
            StartRange = self.BinarySearchFrom_lineEdit.text()
            EndRange = self.BinarySearchTo_lineEdit.text()

        if self.All_radioButton.isChecked():
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
        return self.Builds
