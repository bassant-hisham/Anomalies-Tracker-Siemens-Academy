from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.UIs.CompilationConfigUI import Ui_CompilationConfig_Form
from src.frontend.CustomWidgets.commonFunctions import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
import os 
class MyCompilationConfigWindow(QtWidgets.QWidget, Ui_CompilationConfig_Form):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        self.compile_design_empty = True
        self.output_directory_empty = True
        super(MyCompilationConfigWindow, self).__init__()
        self.setupUi(self) # This sets up the UI components from the Compilation Config window
        self.Done_button.clicked.connect(self.saveConfiguration)
        self.BrowseSource_button.clicked.connect(lambda: showDirectoryDialog(self,self.Source_lineEdit))
        #self.BrowseOutput_button.clicked.connect(lambda: showDirectoryDialog(self,self.Output_lineEdit))
        self.compilation_configurationsdict={}
        self.compilation_configurationsdict['compile_design'] = False
        self.Timeout_lineEdit.setValidator(QIntValidator())
       
    
    def saveConfiguration(self):
        
        # TODO : SOLVE THE COMPILE_CHECKBOX PROBLEM HERE IN THIS IF CONDITION
        
                
            self.compilation_configurationsdict['compilation_configurations']={}
            source_path = self.Source_lineEdit.text()
            directory_path = self.Output_lineEdit.text()
            self.compile_design_empty = True
            if source_path == "":
                 self.showWarningMessage("Source path cannot be empty")
            else:
                self.compile_design_empty = False
                self.compilation_configurationsdict['compile_design'] = True
                self.compilation_configurationsdict['compilation_configurations']['source_design_path'] = source_path
                self.compilation_configurationsdict['compilation_configurations']['output_directory'] = directory_path
                self.compilation_configurationsdict['compilation_configurations']['machine'] = self.Machine_comboBox.currentText()
                self.compilation_configurationsdict['compilation_configurations']['force'] = self.Force_checkBox.isChecked()
                self.compilation_configurationsdict['compilation_configurations']['timeout'] = self.Timeout_lineEdit.text()
                self.close()
                return self.compilation_configurationsdict
        
                #self.Check_Output_Directory_Exist(directory_path)
    
    
    def Check_Output_Directory_Exist(self , directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Directory {directory_path} created")
            return True
        
        else:
            print(f"Directory {directory_path} already exists")
            return False
    
    
    def showWarningMessage(self , input):
        warning_dialog = QMessageBox(self)
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle('Empty String')
        warning_dialog.setText(f'Error : {input}')
        warning_dialog.show()
       

    
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()

