from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from CompilationConfig import Ui_Form
from commonFunctions import *

class MyCompilationConfigWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyCompilationConfigWindow, self).__init__()
        self.setupUi(self) # This sets up the UI components from the Compilation Config window
        self.pushButtonCreate_2.clicked.connect(self.saveConfiguration)
        self.toolButton.clicked.connect(lambda: showFileDialog(self,self.lineEdit_5))
        self.toolButton_2.clicked.connect(lambda: showDirectoryDialog(self,self.lineEdit_4))
        self.compilation_configurations = {}
        
    def saveConfiguration(self):
        self.compilation_configurations['compile_design'] = self.checkBox_2.isChecked()
        self.compilation_configurations['source_design_path'] = self.lineEdit_5.text()
        self.compilation_configurations['output_directory'] = self.lineEdit_4.text()
        self.compilation_configurations['machine'] = self.comboBox.currentText()
        self.compilation_configurations['force'] = self.checkBox.isChecked()
        self.compilation_configurations['timeout'] = self.lineEdit_3.text()
        print(self.compilation_configurations)
        self.close()