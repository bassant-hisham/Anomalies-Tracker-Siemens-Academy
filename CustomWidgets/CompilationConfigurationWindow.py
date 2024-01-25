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
        self.compilation_configurationsdict={}
        
    def saveConfiguration(self):
        self.compilation_configurationsdict['compilation_configurations']={}
        self.compilation_configurationsdict['compilation_configurations']['compile_design'] = self.CompileDesign_checkBox.isChecked()
        self.compilation_configurationsdict['compilation_configurations']['source_design_path'] = self.Source_lineEdit.text()
        self.compilation_configurationsdict['compilation_configurations']['output_directory'] = self.Output_lineEdit.text()
        self.compilation_configurationsdict['compilation_configurations']['machine'] = self.Machine_comboBox.currentText()
        self.compilation_configurationsdict['compilation_configurations']['force'] = self.Force_checkBox.isChecked()
        self.compilation_configurationsdict['compilation_configurations']['timeout'] = self.Timeout_lineEdit.text()
        self.close()
        return self.compilation_configurationsdict
    
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()

    def show_data(self,compilation_configurationsdict:dict):
        self.CompileDesign_checkBox.setChecked(compilation_configurationsdict['compilation_configurations']['compile_design'])
        self.Source_lineEdit.setText(compilation_configurationsdict['compilation_configurations']['source_design_path'] )
        self.Output_lineEdit.setText(compilation_configurationsdict['compilation_configurations']['output_directory'] )
        self.Machine_comboBox.setCurrentText(compilation_configurationsdict['compilation_configurations']['machine'] )
        self.Force_checkBox.setChecked(compilation_configurationsdict['compilation_configurations']['force'] )
        self.Timeout_lineEdit.setText(compilation_configurationsdict['compilation_configurations']['timeout'])

