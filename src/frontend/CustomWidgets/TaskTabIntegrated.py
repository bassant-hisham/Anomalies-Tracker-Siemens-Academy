import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from src.frontend.CustomWidgets.UIs.TaskTabUI import Ui_Task_Tab
from src.frontend.CustomWidgets.commonFunctions import *
from src.frontend.CustomWidgets.DesignBox import MyDesignBox
from src.frontend.CustomWidgets.RunningConfiguration import MyRunningConfigurations


class MyTaskTab(QtWidgets.QWidget, Ui_Task_Tab):
    def __init__(self):
        super(MyTaskTab, self).__init__()
        self.setupUi(self)  # This sets up the UI components from the TaskTab section
        
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.Directory_widget)
        self.stacked_widget.addWidget(self.File_widget)
        self.gridLayout_4.addWidget(self.stacked_widget)
        self.gridLayout_4.removeWidget(self.Directory_widget) #.hide()
        self.gridLayout_4.removeWidget(self.File_widget) #.hide()
        
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
        self.RunningDelete_pushButton.clicked.connect(self.deleteRunningWidget)
        self.DesignDelete_pushButton.clicked.connect(self.deleteDesignWidget)
        self.Task_tabWidget.currentChanged.connect(self.DesignTabEntered)


        self.Running_data=list()
        self.Design_data = list()
        self.Builds = list()
    
    def toggle_directory(self):
        self.stacked_widget.setCurrentIndex(0)
            
    def toggle_file(self):
       self.stacked_widget.setCurrentIndex(1)
            
    def add_design(self):
        #self.scrollLayout.addWidget(MyDesignBox(self.scrollLayout.count()+1))
        new_design_box = MyDesignBox(self.scrollLayout.count() + 1)
        self.scrollLayout.addWidget(new_design_box)
        new_design_box.myparent=new_design_box.parent()
        self.Design_data.append(new_design_box)

    def get_design(self):
        return self.Design_data
    
    def get_running(self):
        return self.Running_data
        
    def add_running_config(self):
        new_running_box = MyRunningConfigurations(self.scrollLayoutRunning)
        new_running_box.custom_window.myparent=self.parent()
        self.Running_data.append(new_running_box)  
        
    def get_builds(self):
        current_index = self.stacked_widget.currentIndex() #use it to know which of dir or file is used (0->Dir , 1->File)
        self.Builds = [] 

        if current_index == 1:
            file_path = self.FilePath_lineEdit.text()
            self.Builds.append(file_path)
        else:
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
    
    def getBinarySearchValue(self):
        return self.BinarySearch_radioButton.isChecked()
    
    def deleteRunningWidget(self):
        if(len(self.Running_data)!=0):
            WidgteToBeRemoved=self.Running_data.pop()
            self.scrollLayoutRunning.removeWidget(WidgteToBeRemoved)
            WidgteToBeRemoved.deleteLater()

    def deleteDesignWidget(self):
        if(len(self.Design_data)!=0):
            WidgteToBeRemoved=self.Design_data.pop()
            self.scrollLayout.removeWidget(WidgteToBeRemoved)
            WidgteToBeRemoved.deleteLater()

    def DesignTabEntered(self):
        self.scrollLayout.setEnabled(True)
        for  design in self.Design_data:
                design.setParent(design.myparent)
                design.show()
                self.scrollLayout.addWidget(design)
               
                


 