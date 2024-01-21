from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from UIs.LaunchingConfigUI import Ui_launching_config
from commonFunctions import *
from DUTBox import MyDUTGroupBox

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

        self.ToolConfig = {}
        self.ToolConfig['master_tool_configuration'] = {}
        self.ToolConfig["master_tool_configuration"]["additional_args"] = {}
        self.ToolConfig["master_tool_configuration"]["tool_additional_env_variables"] = {}
        self.Duts = []

    def toggle_content(self):
        if self.ToolConfigGroupBox.isChecked():
            self.ToolConfigGroupBox.setMaximumHeight(16777215)
        else:
            self.ToolConfigGroupBox.setMaximumHeight(120)

    def add_additional_arguments(self):
        argument_key = self.ArgName_HSpacer_mid_lineEdit.text()
        argument_value = self.ArgValue_lineEdit.text()
        self.ToolConfig["master_tool_configuration"]["additional_args"][argument_key] = argument_value
    
    def add_additional_env_variables(self):
        VE_ENABLE_BUFFERS_STATISTICS = self.EnvVarName_HSpacer_mid_lineEdit.text()
        ENABLE_BACKUP_LOG = self.EnvVarValue_lineEdit.text()
        self.ToolConfig["master_tool_configuration"]["tool_additional_env_variables"][VE_ENABLE_BUFFERS_STATISTICS] = ENABLE_BACKUP_LOG
    





    def add_dut_config(self):
        #self.scrollLayout.addWidget(MyDesignBox(self.scrollLayout.count()+1))
        new_dut_box = MyDUTGroupBox(self.lanch_conf_VLayout.count() - 2)
        self.lanch_conf_VLayout.addWidget(new_dut_box)
        # self.Design_data.append(new_design_box)
        self.Duts.append(new_dut_box)
    def get_Duts(self):
        return self.Duts
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
        return self.ToolConfig
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()
