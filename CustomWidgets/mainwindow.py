from itertools import product
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from UIs.MainWindowUI import Ui_MainWindow
from CompilationConfigurationWindow import MyCompilationConfigWindow
from LaunchingConfigurationWindow import MyLaunchingConfigWindow
from TaskTabIntegrated import MyTaskTab
from Jobs import MyJobs
import json

class MyMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)
        self.Tasks.hide()
        self.CreateJobs_button.hide()
        self.CreateTask_button.clicked.connect(self.createTaskTabWidget)
        
        self.compilation_config = MyCompilationConfigWindow()
        self.launching_configurations = MyLaunchingConfigWindow()
        self.CreateJobs_button.clicked.connect(self.createJobs)
        #self.CreateJobs_button.clicked.connect(self.collectData)

    def createTaskTabWidget(self):
        self.Tasks.TaskTab = MyTaskTab()
        if not self.Tasks.isVisible():
            self.Tasks.show()
            self.CreateJobs_button.show()
            self.Tasks.addTab(self.Tasks.TaskTab , f"Task {self.Tasks.count() + 1}")
        else:
            self.Tasks.addTab(self.Tasks.TaskTab , f"Task {self.Tasks.count() + 1}")
    
    def createJobs(self):
        current_widget = self.Tasks.currentWidget()
        if isinstance(current_widget, MyTaskTab) and current_widget.Task_tabWidget.count() < 4:
            self.Job = MyJobs()
            self.Job.Run_pushButton.clicked.connect(self.GenerateJason)
            self.combinations = self.collectData()
            self.Job.Jobs_table.setRowCount(len(self.combinations))
            for row_index, (running_config, design, build) in enumerate(self.combinations):

                checkbox_item = QTableWidgetItem()
                checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                checkbox_item.setCheckState(Qt.Unchecked)
                self.Job.Jobs_table.setItem(row_index, 0, checkbox_item)
                
                self.Job.Jobs_table.setItem(row_index, 1, QTableWidgetItem(str(row_index)))
                running_dict = running_config.custom_window.running_configurations
                col_index = 2

                for (num,(key,value)) in enumerate(running_dict.items()):
                    self.Job.Jobs_table.setItem(row_index, col_index , QTableWidgetItem(str(value)))
                    col_index += 1

                self.Job.Jobs_table.setItem(row_index, col_index , QTableWidgetItem(str(build)))
                col_index += 1

                DesignPath = design.DesignPath_lineEdit.text()
                self.Job.Jobs_table.setItem(row_index, col_index , QTableWidgetItem(str(DesignPath)))
                col_index += 1

            current_widget.Task_tabWidget.addTab(self.Job,"Jobs")
            

    def collectData(self):
        Designs = self.Tasks.TaskTab.get_design()
        RunningConfigs = self.Tasks.TaskTab.get_running()
        Builds  = self.Tasks.TaskTab.get_builds()
        for running in RunningConfigs:
           running.custom_window.collect_running_config()
        combinations = list(product(RunningConfigs , Designs, Builds))
        return combinations

    def GenerateJason(self):
        file_path = "./frontEnd.json"
        platform=self.Platfrom_comboBox.currentText()
        solution=self.Solution_comboBox.currentText()
        taskNu=self.Tasks.currentIndex()
        JasonData={
                       solution:{
                       "task"+str(taskNu+1):{
                        "id": taskNu+1,  ################to be changed
                        "jobs":{
                        }
                       }    
                           
                       } 
                    }
        with open(file_path, 'w') as json_file:
            for currentJobIndex,(running_config, design, build) in enumerate(self.combinations):
                    if(self.Job.Jobs_table.item(currentJobIndex,0).checkState() != 2):
                        continue
                    running_dict = running_config.custom_window.running_configurations
                    compilationConfigData = design.compilation_config.compilation_configurationsdict
                    ToolConfigData = design.launching_configurations.get_ToolConfig()
                    DutConfigData=[]
                    buildPath=str(build)
                    JasonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex)]={}
                    JasonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex)].update(compilationConfigData)
                    
                    prerequistes={  #############to be changed
                        "prerequisites": {
                        "previous_task_id": 0,
                        "previous_job_id": 0
                        },
                    }
                    JasonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex)].update(prerequistes)
                    Duts = design.get_Duts()
                    for dut in Duts:
                       DutConfigData.append(dut.collect_data())
                     
                    launching_configurations={
                        "launching_configurations": {
                                    "$schema": "../schemas/launching_configuration.schema.json",
                                    "platform": platform,
                                    "solution": solution, 
                                    "src_file": buildPath,
                                    "dut_configuration":DutConfigData,
                                    "tools_configuration":ToolConfigData,
                              }
                              }
                    
                    JasonData[solution][ "task"+str(taskNu+1)]["jobs"][str(currentJobIndex)].update(launching_configurations)
                    JasonData[solution][ "task"+str(taskNu+1)]["jobs"][str(currentJobIndex)].update(running_dict)
            json.dump(JasonData,json_file, indent=2)
            json_file.write("\n")
                    
                    

    
        
        
       

                   



        

