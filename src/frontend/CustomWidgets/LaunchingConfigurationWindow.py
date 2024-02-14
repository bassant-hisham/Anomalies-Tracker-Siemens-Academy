from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.UIs.LaunchingConfigUI import Ui_launching_config
from src.frontend.CustomWidgets.commonFunctions import *
from src.frontend.CustomWidgets.DUTBox import MyDUTGroupBox
import ast  # Import the ast module for safer evaluation
from PyQt5.QtGui import QIcon
import os
from PyQt5.QtWidgets import QApplication

class MyLaunchingConfigWindow(QtWidgets.QWidget, Ui_launching_config):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(MyLaunchingConfigWindow, self).__init__()
        self.setupUi(self) # This sets up the UI components from the Launching Config window
        self.ToolConfigGroupBox.setCheckable(True)
        self.ToolConfigGroupBox.setChecked(False)
        self.toggle_content()
        self.setWindowIcon(QIcon('src/frontend/IconsImages/siemens_logo_icon.png'))
        self.ToolConfigGroupBox.toggled.connect(self.toggle_content)
        self.Add_PushButton.clicked.connect(self.add_dut_config)
        self.Add_PushButton.setToolTip("Add Dut Configuration")
        #self.Add_PushButton.setStyleSheet("QToolTip { color: black; }")
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
        
        self.VE_ENABLE_BUFFERS_STATISTICS_empty = True
        self.ENABLE_BACKUP_LOG_empty = True
        self.VE_ENABLE_BUFFERS_STATISTICS_slave_empty = True
        self.ENABLE_BACKUP_LOG_empty_slave = True
        self.argument_key_empty = True
        self.argument_key_slave_empty = True
        
        
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
        self.argument_key_empty = True
        self.argument_value_empty = True
        text_content = self.AdditionalArg.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.AdditionalArg.clear()   
        
          
        argument_key = self.ArgName_HSpacer_mid_lineEdit.text()
        if(argument_key == ""):
             self.argument_key_empty = True
        else:
            self.argument_key_empty = False
            
            
        argument_value = self.ArgValue_lineEdit.text()
        
        if(argument_value == ""):
            self.argument_value_empty = True
        else:
            self.argument_value_empty = False
            
        
        if(self.argument_key_empty and not self.argument_value_empty):
            self.showWarningMessage("Cannot put value without key in Additional Arguments")
        else:
            self.arguments[argument_key] =argument_value
            self.ToolConfig["master_tool_configuration"]["additional_args"][argument_key] = argument_value
            self.AdditionalArg.append(str(self.arguments))
       
            
    def add_additional_env_variables(self):
        self.VE_ENABLE_BUFFERS_STATISTICS_empty = True
        self.ENABLE_BACKUP_LOG_empty = True
        
        text_content = self.ToolAdditionalEnvValues.toPlainText()
        
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.ToolAdditionalEnvValues.clear()     
            
        VE_ENABLE_BUFFERS_STATISTICS = self.EnvVarName_HSpacer_mid_lineEdit.text()
        if(VE_ENABLE_BUFFERS_STATISTICS == ""):
            self.VE_ENABLE_BUFFERS_STATISTICS_empty = True
        else:
            self.VE_ENABLE_BUFFERS_STATISTICS_empty = False
            
            
        ENABLE_BACKUP_LOG = self.EnvVarValue_lineEdit.text()
        if(ENABLE_BACKUP_LOG == ""):
            self.ENABLE_BACKUP_LOG_empty = True
        else:
            self.ENABLE_BACKUP_LOG_empty = False
            
        
        if((self.VE_ENABLE_BUFFERS_STATISTICS_empty and not self.ENABLE_BACKUP_LOG_empty)) or ((not self.VE_ENABLE_BUFFERS_STATISTICS_empty and self.ENABLE_BACKUP_LOG_empty)):
            self.showWarningMessage("Complete the environment variables")
        else:
            self.ToolConfig["master_tool_configuration"]["tool_additional_env_variables"][VE_ENABLE_BUFFERS_STATISTICS] = ENABLE_BACKUP_LOG
            self.arguments[VE_ENABLE_BUFFERS_STATISTICS] =ENABLE_BACKUP_LOG
            self.ToolAdditionalEnvValues.append(str(self.arguments))
        
            
            
            
    def add_additional_env_variables_slave(self):
        self.VE_ENABLE_BUFFERS_STATISTICS_slave_empty = True
        self.ENABLE_BACKUP_LOG_empty_slave = True
        
        text_content = self.ToolAdditionalEnvValues_2.toPlainText()
        
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.ToolAdditionalEnvValues_2.clear()     
        VE_ENABLE_BUFFERS_STATISTICS = self.EnvVarName_HSpacer_mid_lineEdit_2.text()
        

        if(VE_ENABLE_BUFFERS_STATISTICS == ""):
            self.VE_ENABLE_BUFFERS_STATISTICS_slave_empty = True
        else:
            self.VE_ENABLE_BUFFERS_STATISTICS_slave_empty = False
            
        ENABLE_BACKUP_LOG = self.EnvVarValue_lineEdit_2.text()
        
        if(ENABLE_BACKUP_LOG == ""):
            self.ENABLE_BACKUP_LOG_empty_slave = True
        else:
            self.ENABLE_BACKUP_LOG_empty_slave = False
        
       
        
        if((self.VE_ENABLE_BUFFERS_STATISTICS_slave_empty and not self.ENABLE_BACKUP_LOG_empty_slave)) or ((not self.VE_ENABLE_BUFFERS_STATISTICS_slave_empty and self.ENABLE_BACKUP_LOG_empty_slave)):

            self.showWarningMessage("Complete the slave tool environment Variables")
        
        else:
            self.ToolConfig["slave_tool_configuration"]["tool_additional_env_variables"][VE_ENABLE_BUFFERS_STATISTICS] = ENABLE_BACKUP_LOG
            self.arguments[VE_ENABLE_BUFFERS_STATISTICS] =ENABLE_BACKUP_LOG
            self.ToolAdditionalEnvValues_2.append(str(self.arguments))
        
        

    def add_additional_arguments_slave(self):
        self.argument_value_slave_empty= True
        self.argument_key_slave_empty = True
        text_content = self.AdditionalArg_2.toPlainText()
        if not text_content:
            self.arguments = {}
        else:
            self.arguments = ast.literal_eval(text_content)
            self.AdditionalArg_2.clear()     
        argument_key = self.ArgName_HSpacer_mid_lineEdit_2.text()
        
        if(argument_key == ""):
            self.argument_key_slave_empty= True
        else:
            self.argument_key_slave_empty = False
            
        
            
        argument_value = self.ArgValue_lineEdit_2.text()
        
        if(argument_value == ""):
            self.argument_value_slave_empty = True
        else:
            self.argument_value_slave_empty = False
                
        if(self.argument_key_slave_empty and not self.argument_value_slave_empty):
            self.showWarningMessage("Cannot put key without value in slave tool additional arguments")
        else:
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
    
    
    def showWarningMessage(self , input):
        warning_dialog = QMessageBox(self)
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle('Empty String')
        warning_dialog.setText(f'Error : {input}')
        warning_dialog.show()
        
    def closeEvent(self, event):
        num = 0
        dut_index, dut = next(enumerate(self.Duts), (None, None))
        error_msg = f""       
        self.config_tool_error = False
      
        for index,dut in enumerate(self.Duts):
            
            error_msg += "---------------------------------------------\n"
            error_msg += f"Enter the following for Dut {index} :" + "\n"
            error_msg += "---------------------------------------------\n"
            if(dut.DesignPath_lineEdit_2.text() == "" or not os.path.exists(dut.DesignPath_lineEdit_2.text()) or not os.path.isdir(dut.DesignPath_lineEdit_2.text())):
                error_msg += f"{str(num).rjust(2)}: Valid Design File Path \n"
                num += 1
            # temp=dut.AVB_ListView_2.selectedIndexes()
            # if (len(dut.AVB_ListView_2.selectedIndexes())==0):
            #     error_msg+=f"{str(num).rjust(2)}: Choose values for the AVB List \n"
            #     num += 1
            if(dut.RecordDir_lineEdit_2.text() == "" or not os.path.isdir(dut.RecordDir_lineEdit_2.text()) or not os.path.exists(dut.DesignPath_lineEdit_2.text())):
                error_msg+=f"{str(num).rjust(2)}: Valid Record Directory path \n" 
                num += 1
            if(dut.ReplyDir_lineEdit_2.text()=="" or not os.path.isdir(dut.ReplyDir_lineEdit_2.text()) or not os.path.exists(dut.DesignPath_lineEdit_2.text())):
                error_msg+=f"{str(num).rjust(2)}: Valid Reply Directory path \n"
                num += 1
            if(dut.ReplySnapshotName_lineEdit_2.text()==""):
                error_msg+=f"{str(num).rjust(2)}: Snapshot Name \n" 
                num += 1
            if(dut.DPILaunchMode_lineEdit_2.text()==""):
                error_msg+=f"{str(num).rjust(2)}: Launch Mode \n"
                num += 1
            
            
        
        if(num == 0 and self.config_tool_error == False):
            error_msg = ""
                
        
                
        if(error_msg== ""):
            num = 1       
            self.closed_signal.emit()
            event.accept()
        else:
           event.ignore()
           warning_dialog = QMessageBox(self)
           warning_dialog.setWindowTitle("Empty input Fields")
           warning_dialog.setIcon(QMessageBox.Warning)
           warning_dialog.show()
           warning_dialog.setText(error_msg)  
