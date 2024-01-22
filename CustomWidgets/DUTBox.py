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
        self.ConfigType_comboBox.currentIndexChanged.connect(self.handleSnapshotsNu)
        self.Configvalue_label.hide()
        self.Configvalue_lineEdit.hide()
        self.ConfigValueList_label.hide()
        self.ConfigValueList_lineEdit.hide()
        

    def toggle_content(self):
        if self.isChecked():
            self.setMaximumHeight(16777215)
        else:
            self.setMaximumHeight(120)
            
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
    def handleSnapshotsNu(self) -> None:
        if (self.ConfigType_comboBox.currentIndex()==0):  #range
            self.FromConfigValue_lineEdit.show()
            self.FromConfigValue_label.show()
            self.ToConfigValue_lineEdit.show()
            self.ToConfigValue_label.show()
            self.Configvalue_label.hide()
            self.Configvalue_lineEdit.hide()
            self.ConfigValueList_label.hide()
            self.ConfigValueList_lineEdit.hide()

        elif(self.ConfigType_comboBox.currentIndex()==1): #list
            self.FromConfigValue_lineEdit.hide()
            self.FromConfigValue_label.hide()
            self.ToConfigValue_lineEdit.hide()
            self.ToConfigValue_label.hide()
            self.Configvalue_label.hide()
            self.Configvalue_lineEdit.hide()
            self.ConfigValueList_label.show()
            self.ConfigValueList_lineEdit.show()
        else: #value
            self.FromConfigValue_lineEdit.hide()
            self.FromConfigValue_label.hide()
            self.ToConfigValue_lineEdit.hide()
            self.ToConfigValue_label.hide()
            self.Configvalue_label.show()
            self.Configvalue_lineEdit.show()
            self.ConfigValueList_label.hide()
            self.ConfigValueList_lineEdit.hide()

    def collect_data(self):
                data = {
                        "launch_dpi": self.LanuchDPI_checkBox.isChecked(),
                        "terminate_dpi": self.TermianteDPI_checkBox.isChecked(),                    
                        "terminate_dpi_onerror": self.TerminateDPIOnError_checkBox.isChecked(),
                        "avb_list": self.AVB_ListView_2.selectedIndexes(),
                        "design_path": self.DesignPath_lineEdit_2.text(),
                        "record_replay_configurations":{
                        "record_configurations": {
                        "record_dir": self.RecordDir_lineEdit_2.text(),
                        "snapshots_number":{
                            "config_type":self.ConfigType_comboBox.currentText(),
                        },
                        },
                        "replay_configurations": {
                            "replay_dir": self.ReplyDir_lineEdit_2.text(),  
                            "replay_snapshot_name": self.ReplySnapshotName_lineEdit_2.text(),
                        },                          
                        },
                        "dpi_launch_mode": self.DPILaunchMode_lineEdit_2.text(),
                        "dpi_launch_type": self.DPILaunchType_comboBox_2.currentText(),
                        "dpi_additional_args":{},
                        "dpi_additional_env_variables":{},
                        "use_custom_comodels_config":self.CustomComConf_checkbox_2.isChecked(),
                        

                }

                if (self.CustomComConf_checkbox_2.isChecked() == True):
                    data["custom_comodels_config"]=[]
                    customGroupBoxesCount=self.CustomCoModels.ConfigVLayout.count() #nu of groupBoxes
                    for CustomgroupBoxIndex in range(customGroupBoxesCount):
                         temp=self.CustomCoModels.ConfigVLayout.itemAt(CustomgroupBoxIndex)
                         Host_name=self.CustomCoModels.ConfigVLayout.itemAt(CustomgroupBoxIndex).widget().HostName_comboBox.currentText()
                         Domain_id=self.CustomCoModels.ConfigVLayout.itemAt(CustomgroupBoxIndex).widget().DomainId_comboBox.currentText()
                         data["custom_comodels_config"].append({"host_name":Host_name,"domain_id":Domain_id})
                if (self.ConfigType_comboBox.currentText()=="Range"):
                    data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"]=[int(self.FromConfigValue_lineEdit.text()),int(self.ToConfigValue_lineEdit.text())]
                elif (self.ConfigType_comboBox.currentText()=="Value"):
                    data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"]=int(self.Configvalue_lineEdit.text())
                else:  
                    data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"]=[]
                    for num in self.ConfigValueList_lineEdit.text().split(','):
                        data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"].append(int(num)) 
                if(self.DPIAdditionalEnvValues_2.toPlainText()):
                     data["dpi_additional_env_variables"]=eval(self.DPIAdditionalEnvValues_2.toPlainText())
                elif(self.DPIAdditionalArg_2.toPlainText()):
                     data["dpi_additional_args"]=eval(self.DPIAdditionalArg_2.toPlainText())
            
                return data
    

            

