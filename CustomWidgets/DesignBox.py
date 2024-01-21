from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from commonFunctions import *
from CompilationConfigurationWindow import MyCompilationConfigWindow 
from LaunchingConfigurationWindow import MyLaunchingConfigWindow
from UIs.DesignBoxUI import Ui_DesignBox

class MyDesignBox(QtWidgets.QGroupBox,Ui_DesignBox):
    def __init__(self,id):
        super(MyDesignBox, self).__init__()
        self.setupUi(self)  # This sets up the UI components from the Design box
        self.setTitle("Design " + str(id))
        self.compilation_config = MyCompilationConfigWindow()
        self.launching_configurations=MyLaunchingConfigWindow()
        self.CompilationConfig_button.clicked.connect(self.open_compilation_config)
        self.BrowseDesignPath_button.clicked.connect(lambda: showFileDialog(self,self.DesignPath_lineEdit))
        self.LaunchingConfig_button.clicked.connect(self.open_launching_config)
        self.setCheckable(True)
        self.setChecked(True)
        self.toggled.connect(self.toggle_content)

    def toggle_content(self):
        if self.isChecked():
            self.setMaximumHeight(16777215)
        else:
            self.setMaximumHeight(40)
            
    def open_compilation_config(self):
        self.compilation_config.show()
        self.compilation_config.closed_signal.connect(self.handle_another_window_closed)
        grandparent = self.get_grandparent(self)
        grandparent.setEnabled(False)
    
    def get_grandparent(self, widget):
        grandparent = widget.parent()
        while grandparent and grandparent.parent():
            grandparent = grandparent.parent()
        return grandparent
    
    def open_launching_config(self):
        self.launching_configurations.show()
        self.launching_configurations.closed_signal.connect(self.handle_another_window_closed)
        grandparent = self.get_grandparent(self)
        grandparent.setEnabled(False)
    
    def handle_another_window_closed(self):
        grandparent = self.get_grandparent(self)
        grandparent.setEnabled(True)
           
    def get_Duts(self):
        return self.launching_configurations.get_Duts()
    def get_ToolConfig(self):
        return self.launching_configurations.get_ToolConfig()
   