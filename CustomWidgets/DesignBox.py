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
    
    def get_design_path(self):
        return self.DesignPath_lineEdit.text()
    
    def get_compilation_dict(self):
        return self.compilation_config.saveConfiguration()
    
    def get_ToolConfig_dict(self):
        return self.launching_configurations.get_ToolConfig()
    
    def get_Dut_dict(self):
        dutsdict={}
        for index,dut in enumerate(self.launching_configurations.get_Duts()):
            dutsdict[index]=dut.collect_data()
        return dutsdict
    
    def showdesign(self):
        self.DesignPath_lineEdit.setDisabled(True)
        self.BrowseDesignPath_button.setDisabled(True)
        self.setCheckable
        for widget in self.compilation_config.findChildren(QWidget):
            if (not (isinstance(widget,QPushButton)) and (type(widget) != QWidget) ):
                widget.setDisabled(True)

        for widget in self.launching_configurations.findChildren(QWidget):
            if(not isinstance(widget,QGroupBox)):
                if ((not (widget.objectName()=="Done_pushButton"))  and (type(widget) != QWidget) and (type(widget) != QScrollBar) and (type(widget) != QScrollArea)):
                    widget.setDisabled(True)


    def showdata(self,compilation_dict,tool_dict,dut_dict,design_path):
        
        self.DesignPath_lineEdit.setText(design_path)
        self.launching_configurations.show_data(tool_dict)

        for index in range(len(dut_dict.items())):
            self.launching_configurations.add_dut_config()
            self.launching_configurations.Duts[index].show_data(dut_dict[index])

        self.compilation_config.show_data(compilation_dict)
        self.showdesign()




        
   