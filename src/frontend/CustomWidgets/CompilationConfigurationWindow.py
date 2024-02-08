from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.UIs.CompilationConfigUI import Ui_CompilationConfig_Form
from src.frontend.CustomWidgets.commonFunctions import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

class MyCompilationConfigWindow(QtWidgets.QWidget, Ui_CompilationConfig_Form):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        
        self.compile_design_empty = True
        self.output_directory_empty = True
        super(MyCompilationConfigWindow, self).__init__()
        self.setupUi(self) # This sets up the UI components from the Compilation Config window
        self.Done_button.clicked.connect(self.saveConfiguration)
        self.BrowseSource_button.clicked.connect(lambda: showDirectoryDialog(self,self.Source_lineEdit))
        self.BrowseOutput_button.clicked.connect(lambda: showDirectoryDialog(self,self.Output_lineEdit))
        self.compilation_configurationsdict={}
        self.Timeout_lineEdit.setValidator(QIntValidator())
        
    def saveConfiguration(self):
        self.compilation_configurationsdict['compilation_configurations']={}
        self.compilation_configurationsdict['compilation_configurations']['compile_design'] = self.CompileDesign_checkBox.isChecked()
        
        
        source_path = self.Source_lineEdit.text()
        directory_path = self.Output_lineEdit.text()
        self.compile_design_empty = True
        self.output_directory_empty = True
        if source_path == "":
            self.showWarningMessage("Source path cannot be empty")
        else:
            self.compile_design_empty = False
            self.compilation_configurationsdict['compilation_configurations']['source_design_path'] = source_path
        
        if ((directory_path == "") and not self.compile_design_empty) :
             self.showWarningMessage("Directory path cannot be empty")
        else:
            self.output_directory_empty = False
            self.compilation_configurationsdict['compilation_configurations']['output_directory'] = directory_path
            
        self.compilation_configurationsdict['compilation_configurations']['machine'] = self.Machine_comboBox.currentText()
        self.compilation_configurationsdict['compilation_configurations']['force'] = self.Force_checkBox.isChecked()
        self.compilation_configurationsdict['compilation_configurations']['timeout'] = self.Timeout_lineEdit.text()
        if(not self.compile_design_empty and not self.output_directory_empty):
            self.close()
        return self.compilation_configurationsdict
    
    def showWarningMessage(self , input):
        warning_dialog = QMessageBox(self)
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle('Empty String')
        warning_dialog.setText(f'Error : {input}')
        warning_dialog.show()
       

    
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()

    # def show_data(self,compilation_configurationsdict:dict):
    #     self.CompileDesign_checkBox.setChecked(compilation_configurationsdict['compilation_configurations']['compile_design'])
    #     self.Source_lineEdit.setText(compilation_configurationsdict['compilation_configurations']['source_design_path'] )
    #     self.Output_lineEdit.setText(compilation_configurationsdict['compilation_configurations']['output_directory'] )
    #     self.Machine_comboBox.setCurrentText(compilation_configurationsdict['compilation_configurations']['machine'] )
    #     self.Force_checkBox.setChecked(compilation_configurationsdict['compilation_configurations']['force'] )
    #     self.Timeout_lineEdit.setText(compilation_configurationsdict['compilation_configurations']['timeout'])

