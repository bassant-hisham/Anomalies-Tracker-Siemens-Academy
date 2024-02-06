from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.UIs.DUTBoxUI import Ui_DUTConfiguration
from src.frontend.CustomWidgets.CustomCoModelsConfig import CustomCoModelsConfig
from src.frontend.CustomWidgets.commonFunctions import *
import ast  # Import the ast module for safer evaluation
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp


class MyDUTGroupBox(QtWidgets.QGroupBox, Ui_DUTConfiguration):
    def __init__(self, Dutconfig_Vlayout:QVBoxLayout, Duts:list,id):
        super(MyDUTGroupBox, self).__init__()
        self.setupUi(self)
        self.id=id
        self.setTitle("DUT Configuration " + str(id))
        self.setCheckable(True)
        self.setWindowIcon(QIcon('src/frontend/IconsImages/siemens_logo_icon.png'))
        self.setChecked(True)
        self.toggled.connect(self.toggle_content)
        self.CustomComConf_checkbox_2.stateChanged.connect(self.add_custom_comodel)
        
        # showDirectoryDialog
        self.DesignPath_toolButton_2.clicked.connect(lambda: showDirectoryDialog(self,self.DesignPath_lineEdit_2))
        self.RecordDir_toolButton_2.clicked.connect(lambda: showDirectoryDialog(self,self.RecordDir_lineEdit_2))
        self.ReplyDir_toolButton_2.clicked.connect(lambda: showDirectoryDialog(self,self.ReplyDir_lineEdit_2))
        self.Dut_pushButton.clicked.connect(self.deleteDutWidget)
        self.AddArgButton_2.clicked.connect(self.add_arguments)
        self.AddEnv_2.clicked.connect(self.add_additional_env_variables)
        self.ConfigType_comboBox.currentIndexChanged.connect(self.handleSnapshotsNu)
        self.DeleteArgButton_DPI.clicked.connect(lambda: self.delete_last_variable(self.DPIAdditionalArg_2))
        self.DeleteEnv_DPI.clicked.connect(lambda: self.delete_last_variable(self.DPIAdditionalEnvValues_2))
        self.Configvalue_label.hide()
        self.Configvalue_lineEdit.hide()
        self.ConfigValueList_label.hide()
        self.ConfigValueList_lineEdit.hide()
        self.FromConfigValue_lineEdit.setValidator(QIntValidator())
        self.ToConfigValue_lineEdit.setValidator(QIntValidator())
        self.Configvalue_lineEdit.setValidator(QIntValidator())
        regex = QRegExp('\[\d(,\d)*\]')
        self.ConfigValueList_lineEdit.setValidator(QRegExpValidator(regex))
        self.Dutconfig_Vlayout=Dutconfig_Vlayout
        self.Duts=Duts
        

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
    
    def delete_last_variable(self, textbox):
        text_content = ast.literal_eval(textbox.toPlainText())
        textbox.clear()
        text_content.popitem()
        textbox.append(str(text_content))
        
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

    def deleteDutWidget(self):
        self.Duts.remove(self)
        self.Dutconfig_Vlayout.removeWidget(self)
        self.deleteLater()
        
        for index,widget in enumerate(self.Duts):
            self.Duts[index].id=index+1
            self.Duts[index].setTitle("DUT Configuration " + str(index+1))

    def collect_data(self):
                self.data = {
                        "launch_dpi": self.LanuchDPI_checkBox.isChecked(),
                        "terminate_dpi": self.TermianteDPI_checkBox.isChecked(),                    
                        "terminate_dpi_onerror": self.TerminateDPIOnError_checkBox.isChecked(),
                        "avb_list": self.AVB_ListView_2.selectedIndexes(),
                        #"avb_list": [index.row() for index in self.AVB_ListView_2.selectedIndexes()],    # gpt suggesstion for the problem
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
                    self.data["custom_comodels_config"]=[]
                    customGroupBoxesCount=self.CustomCoModels.ConfigVLayout.count() #nu of groupBoxes
                    for CustomgroupBoxIndex in range(customGroupBoxesCount):
                         Host_name=self.CustomCoModels.ConfigVLayout.itemAt(CustomgroupBoxIndex).widget().HostName_comboBox.currentText()
                         Domain_id=self.CustomCoModels.ConfigVLayout.itemAt(CustomgroupBoxIndex).widget().DomainId_comboBox.currentText()
                         self.data["custom_comodels_config"].append({"host_name":Host_name,"domain_id":Domain_id})
                self.data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"]=[]
                if (self.ConfigType_comboBox.currentText()=="Range"  and self.FromConfigValue_lineEdit.text()!='' and self.ToConfigValue_lineEdit.text()!=''):
                    self.data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"]=[int(self.FromConfigValue_lineEdit.text()),int(self.ToConfigValue_lineEdit.text())]
                elif (self.ConfigType_comboBox.currentText()=="Value" and self.Configvalue_lineEdit.text()!='' ):
                    self.data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"]=int(self.Configvalue_lineEdit.text())
                elif(self.ConfigType_comboBox.currentText()=="List" and self.ConfigValueList_lineEdit.text()!='' ):  
                    self.data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"]=[]
                    for num in self.ConfigValueList_lineEdit.text()[1:len(self.ConfigValueList_lineEdit.text())-1].split(','):
                        self.data["record_replay_configurations"]["record_configurations"]["snapshots_number"]["config_value"].append(int(num)) 
                if(self.DPIAdditionalEnvValues_2.toPlainText()):
                    self. data["dpi_additional_env_variables"]=eval(self.DPIAdditionalEnvValues_2.toPlainText())
                elif(self.DPIAdditionalArg_2.toPlainText()):
                     self.data["dpi_additional_args"]=eval(self.DPIAdditionalArg_2.toPlainText())
            
                return self.data
    
