from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from UIs.CompilationConfigUI import Ui_CompilationConfig_Form
from commonFunctions import *

class MyCompilationConfigWindow(QtWidgets.QWidget, Ui_CompilationConfig_Form):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(MyCompilationConfigWindow, self).__init__()
        self.setupUi(self) # This sets up the UI components from the Compilation Config window
        self.Done_button.clicked.connect(self.saveConfiguration)
        self.BrowseSource_button.clicked.connect(lambda: showFileDialog(self,self.Source_lineEdit))
        self.BrowseOutput_button.clicked.connect(lambda: showDirectoryDialog(self,self.Output_lineEdit))
        self.compilation_configurations = {}
        
    def saveConfiguration(self):
        self.compilation_configurations['compile_design'] = self.CompileDesign_checkBox.isChecked()
        self.compilation_configurations['source_design_path'] = self.Source_lineEdit.text()
        self.compilation_configurations['output_directory'] = self.Output_lineEdit.text()
        self.compilation_configurations['machine'] = self.Machine_comboBox.currentText()
        self.compilation_configurations['force'] = self.Force_checkBox.isChecked()
        self.compilation_configurations['timeout'] = self.Timeout_lineEdit.text()
        self.close()
    
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()
