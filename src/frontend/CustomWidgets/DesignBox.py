from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore
from src.frontend.CustomWidgets.commonFunctions import *
from src.frontend.CustomWidgets.CompilationConfigurationWindow import MyCompilationConfigWindow 
from src.frontend.CustomWidgets.LaunchingConfigurationWindow import MyLaunchingConfigWindow
from src.frontend.CustomWidgets.UIs.DesignBoxUI import Ui_DesignBox
from PyQt5.QtCore import QPoint

class MyDesignBox(QtWidgets.QGroupBox,Ui_DesignBox):
    closed_signal = QtCore.pyqtSignal()
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
        self.myparent=self.parent()
        

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
        grandparent = widget.myparent
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
    
    def showdesign(self):
        self.DesignPath_lineEdit.setDisabled(True)
        self.BrowseDesignPath_button.setDisabled(True)
        for widget in self.compilation_config.findChildren(QWidget):
            if (not (isinstance(widget,QPushButton)) and (type(widget) != QWidget) ):
                widget.setDisabled(True)

        for widget in self.launching_configurations.findChildren(QWidget):
            if(not isinstance(widget,QGroupBox)):
                if ((not (widget.objectName()=="Done_pushButton"))  and (type(widget) != QWidget) and (type(widget) != QScrollBar) and (type(widget) != QScrollArea)):
                    widget.setDisabled(True)

    def center_on_parent(self):       
        screen = QDesktopWidget().screenGeometry()
        center_x = screen.width() // 2  
        center_y = screen.height() // 2
        popup_geometry = self.frameGeometry()
        popup_geometry.moveCenter(QPoint(center_x, center_y))
        self.move(popup_geometry.topLeft())
        
    def closeEvent(self, event):
        self.DesignPath_lineEdit.setDisabled(False)
        self.BrowseDesignPath_button.setDisabled(False)
        for widget in self.compilation_config.findChildren(QWidget):
            if (not (isinstance(widget,QPushButton)) and (type(widget) != QWidget) ):
                widget.setDisabled(False)

        for widget in self.launching_configurations.findChildren(QWidget):
            if(not isinstance(widget,QGroupBox)):
                if ((not (widget.objectName()=="Done_pushButton"))  and (type(widget) != QWidget) and (type(widget) != QScrollBar) and (type(widget) != QScrollArea)):
                    widget.setDisabled(False)
        self.closed_signal.emit()
        event.accept()

        

        
   