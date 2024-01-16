from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from commonFunctions import *
from CompilationConfigurationWindow import MyCompilationConfigWindow 
from LaunchingConfigurationWindow import MyLaunchingConfigWindow
from DesignBoxUI import Ui_GroupBox

class MyDesignBox(QtWidgets.QGroupBox,Ui_GroupBox):
    def __init__(self,id):
        super(MyDesignBox, self).__init__()
        self.setupUi(self)  # This sets up the UI components from the Design box
        self.setTitle("Design " + str(id))
        self.compilation_config = MyCompilationConfigWindow()
        self.launching_configurations=MyLaunchingConfigWindow()
        self.pushButtonAdd_3.clicked.connect(self.open_compilation_config)
        self.toolButtonBrowseDatabase_3.clicked.connect(lambda: showFileDialog(self,self.lineEditDatabasePath_2))
        self.pushButtonAdd_4.clicked.connect(self.open_launching_config)
        self.setCheckable(True)
        self.setChecked(True)
        self.toggled.connect(self.toggle_content)

    def toggle_content(self):
        if self.isChecked():
            self.setMaximumHeight(16777215)
        else:
            self.setMaximumHeight(20)
            
    def open_compilation_config(self):
        self.compilation_config.show()
    
    def open_launching_config(self):
        self.launching_configurations.show()
        
    def GetLists(self):
        return self.launching_configurations.lanchuning_conf_editsObject.GetList()
   