from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.UIs.LaunchingConfigUI import Ui_launching_config
from src.frontend.CustomWidgets.commonFunctions import *
from src.frontend.CustomWidgets.DUTBox import MyDUTGroupBox
import ast  # Import the ast module for safer evaluation


class MyLaunchingConfigWindow(QtWidgets.QWidget, Ui_launching_config):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(MyLaunchingConfigWindow, self).__init__()
        self.setupUi(self) # This sets up the UI components from the Launching Config window
        self.ToolConfigGroupBox.setCheckable(True)
        self.ToolConfigGroupBox.setChecked(False)
        self.toggle_content()

        self.ToolConfigGroupBox.toggled.connect(self.toggle_content)
        self.Add_PushButton.clicked.connect(self.add_dut_config)
        self.AddArgButton.clicked.connect(self.add_additional_arguments)
        self.AddEnv.clicked.connect(self.add_additional_env_variables)
        self.AddArgButton_2.clicked.connect(self.add_additional_arguments_slave)
        self.AddEnv_2.clicked.connect(self.add_additional_env_variables_slave)
        self.Delete_pushButton.clicked.connect(self.deleteLastDutWidget)
        self.Done_pushButton.clicked.connect(self.close)
        self.DeleteArgButton_master.clicked.connect(lambda: self.delete_last_variable(self.AdditionalArg))
        self.DeleteEnvButton_master.clicked.connect(lambda: self.delete_last_variable(self.ToolAdditionalEnvValues))
        self.DeleteArgButton_slave.clicked.connect(lambda: self.delete_last_variable(self.AdditionalArg_2))
        self.DeleteEnvButton_slave.clicked.connect(lambda: self.delete_last_variable(self.ToolAdditionalEnvValues_2))
        
        self.ToolConfig = {}
        self.ToolConfig["launch_tool"]=False
        self.ToolConfig['master_tool_configuration'] = {}
        self.ToolConfig["master_tool_configuration"]["tool_name"]=""
        self.ToolConfig["master_tool_configuration"]["tool_launch_mode"]="" 
        self.ToolConfig["master_tool_configuration"]["additional_args"] = {}
        self.ToolConfig["master_tool_configuration"]["tool_additional_env_variables"] = {}

        self.ToolConfig["slave_tool_configuration"]={}
        self.ToolConfig["slave_tool_configuration"]['launch_behavior'] =""
        self.ToolConfig["slave_tool_configuration"]["tool_launch_mode"]=""
        self.ToolConfig["slave_tool_configuration"]["additional_args"]={} 
        self.ToolConfig["slave_tool_configuration"]["additional_args"] = {}
        self.ToolConfig["slave_tool_configuration"]["tool_additional_env_variables"] = {}
        self.Duts = []

    def toggle_content(self):
        if self.ToolConfigGroupBox.isChecked():
            self.ToolConfigGroupBox.setMaximumHeight(16777215)
        else:
            self.ToolConfigGroupBox.setMaximumHeight(120)

    def add_arguments(self):
        text_content = self.DPIAdditionalArg_2.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.DPIAdditionalArg_2.clear()
        self.arguments[self.ArgName_HSpacer_mid_lineEdit_2.text()] = self.ArgValue_lineEdit_2.text()
        self.DPIAdditionalArg_2.append(str(self.arguments))
    
    # def get_arguments(self):
    #     text_content = self.DPIAdditionalArg_2.toPlainText()
    #     if not text_content:
    #         self.arguments = {}
    #     else:
    #         self.arguments = ast.literal_eval(text_content)
    #         self.DPIAdditionalArg_2.clear()
    #     self.arguments[self.ArgName_HSpacer_mid_lineEdit_2.text()] = self.ArgValue_lineEdit_2.text()
    #     self.DPIAdditionalArg_2.append(str(self.arguments))
        
    def add_additional_arguments(self):
        text_content = self.AdditionalArg.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.AdditionalArg.clear()     
        argument_key = self.ArgName_HSpacer_mid_lineEdit.text()
        argument_value = self.ArgValue_lineEdit.text()
        self.arguments[argument_key] =argument_value
        self.ToolConfig["master_tool_configuration"]["additional_args"][argument_key] = argument_value
        self.AdditionalArg.append(str(self.arguments))

            
    def add_additional_env_variables(self):
        text_content = self.ToolAdditionalEnvValues.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.ToolAdditionalEnvValues.clear()     
        VE_ENABLE_BUFFERS_STATISTICS = self.EnvVarName_HSpacer_mid_lineEdit.text()
        ENABLE_BACKUP_LOG = self.EnvVarValue_lineEdit.text()
        self.ToolConfig["master_tool_configuration"]["tool_additional_env_variables"][VE_ENABLE_BUFFERS_STATISTICS] = ENABLE_BACKUP_LOG
        self.arguments[VE_ENABLE_BUFFERS_STATISTICS] =ENABLE_BACKUP_LOG
        self.ToolAdditionalEnvValues.append(str(self.arguments))
    
    def add_additional_env_variables_slave(self):
        text_content = self.ToolAdditionalEnvValues_2.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.ToolAdditionalEnvValues_2.clear()     
        VE_ENABLE_BUFFERS_STATISTICS = self.EnvVarName_HSpacer_mid_lineEdit_2.text()
        ENABLE_BACKUP_LOG = self.EnvVarValue_lineEdit_2.text()
        self.ToolConfig["slave_tool_configuration"]["tool_additional_env_variables"][VE_ENABLE_BUFFERS_STATISTICS] = ENABLE_BACKUP_LOG
        self.arguments[VE_ENABLE_BUFFERS_STATISTICS] =ENABLE_BACKUP_LOG
        self.ToolAdditionalEnvValues_2.append(str(self.arguments))

    def add_additional_arguments_slave(self):
        text_content = self.AdditionalArg_2.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.AdditionalArg_2.clear()     
        argument_key = self.ArgName_HSpacer_mid_lineEdit_2.text()
        argument_value = self.ArgValue_lineEdit_2.text()
        self.arguments[argument_key] =argument_value
        self.ToolConfig["slave_tool_configuration"]["additional_args"][argument_key] = argument_value
        self.AdditionalArg_2.append(str(self.arguments))


    def add_dut_config(self):
        new_dut_box = MyDUTGroupBox(self.Dutconfig_Vlayout,self.Duts,self.Dutconfig_Vlayout.count()+1)
        self.Dutconfig_Vlayout.addWidget(new_dut_box)
        self.Duts.append(new_dut_box)

    def get_Duts(self):
        return self.Duts

    def deleteLastDutWidget(self):
        if(len(self.Duts)!=0):
            WidgteToBeRemoved=self.Duts.pop()
            self.Dutconfig_Vlayout.removeWidget(WidgteToBeRemoved)
            WidgteToBeRemoved.deleteLater()
        
    def get_ToolConfig(self):
        self.ToolConfig["launch_tool"] = self.LaunchToolCheckBox.isChecked()
        self.ToolConfig["master_tool_configuration"]["tool_name"] = self.ToolName_comboBox.currentText()
        self.ToolConfig["master_tool_configuration"]["tool_launch_mode"] = self.ToolLaunch_comboBox.currentText()
        #self.ToolConfig["master_tool_configuration"]["additional_args"]["argument_key"] = self.ArgName_HSpacer_mid_lineEdit.text()
        #self.ToolConfig["master_tool_configuration"]["additional_args"]["argument_value"] = self.ArgValue_lineEdit.text()
        #self.ToolConfig["master_tool_configuration"]["tool_additional_env_variables"]["VE_ENABLE_BUFFERS_STATISTICS"] = self.EnvVarName_HSpacer_mid_lineEdit.text()
        #self.ToolConfig["master_tool_configuration"]["tool_additional_env_variables"]["ENABLE_BACKUP_LOG"] = self.EnvVarValue_lineEdit.text()
        self.ToolConfig["master_tool_configuration"]["terminate_tool"] = self.TerminateOnErr_checkBox.isChecked()
        self.ToolConfig["master_tool_configuration"]["terminate_tool_onerror"] = self.TerminateTool_checkBox.isChecked()

        self.ToolConfig["slave_tool_configuration"]["launch_behavior"] = self.ToolName_comboBox_2.currentText()
        self.ToolConfig["slave_tool_configuration"]["tool_launch_mode"] = self.ToolLaunch_comboBox_2.currentText()
        self.ToolConfig["slave_tool_configuration"]["terminate_tool"] = self.TerminateOnErr_checkBox_2.isChecked()
        self.ToolConfig["slave_tool_configuration"]["terminate_tool_onerror"] = self.TerminateTool_checkBox_2.isChecked()
        return self.ToolConfig
        
    def delete_last_variable(self, textbox):
        text_content = ast.literal_eval(textbox.toPlainText())
        textbox.clear()
        text_content.popitem()
        textbox.append(str(text_content))
        
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()
