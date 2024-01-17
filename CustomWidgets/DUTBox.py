from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from UIs.DUTBoxUI import Ui_DUTConfiguration
from CustomCoModelsConfig import CustomCoModelsConfig
from commonFunctions import *
import ast  # Import the ast module for safer evaluation

class MyDUTGroupBox(QtWidgets.QGroupBox, Ui_DUTConfiguration):
    def __init__(self,id):
        super(MyDUTGroupBox, self).__init__()
        self.setupUi(self)
        self.setTitle("DUT Configuration " + str(id))
        self.setCheckable(True)
        self.setChecked(True)
        self.toggled.connect(self.toggle_content)
        self.CustomComConf_checkbox_2.stateChanged.connect(self.add_custom_comodel)
        self.DesignPath_toolButton_2.clicked.connect(lambda: showFileDialog(self,self.DesignPath_lineEdit_2))
        self.RecordDir_toolButton_2.clicked.connect(lambda: showDirectoryDialog(self,self.RecordDir_lineEdit_2))
        self.ReplyDir_toolButton_2.clicked.connect(lambda: showDirectoryDialog(self,self.ReplyDir_lineEdit_2))
        self.AddArgButton_2.clicked.connect(self.add_arguments)
        self.AddEnv_2.clicked.connect(self.add_additional_env_variables)
        

    def toggle_content(self):
        if self.isChecked():
            self.setMaximumHeight(16777215)
        else:
            self.setMaximumHeight(70)
            
    def add_custom_comodel(self):
        if self.CustomComConf_checkbox_2.isChecked():
            self.CustomCoModels = CustomCoModelsConfig()
            self.gridLayout_8.addWidget(self.CustomCoModels)
        else:
            self.gridLayout_8.removeWidget(self.CustomCoModels)
            self.CustomCoModels.deleteLater()
    
    def add_arguments(self):
        text_content = self.DPIAdditionalArg_2.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.DPIAdditionalArg_2.clear()
        self.arguments[self.ArgName_HSpacer_mid_lineEdit_2.text()] = self.ArgValue_lineEdit_2.text()
        self.DPIAdditionalArg_2.append(str(self.arguments))
    
    def add_additional_env_variables(self):
        text_content = self.DPIAdditionalEnvValues_2.toPlainText()
        if not text_content:
            self.additionalEnv = {}
        else:
            self.additionalEnv = ast.literal_eval(text_content)
            self.DPIAdditionalEnvValues_2.clear()
        self.additionalEnv[self.EnvVarName_HSpacer_mid_lineEdit_2.text()] = self.EnvVarValue_lineEdit_2.text()
        self.DPIAdditionalEnvValues_2.append(str(self.additionalEnv))

            
