from itertools import product
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from src.frontend.CustomWidgets.UIs.MainWindowUI import Ui_MainWindow
from src.frontend.CustomWidgets.CompilationConfigurationWindow import MyCompilationConfigWindow
from src.frontend.CustomWidgets.LaunchingConfigurationWindow import MyLaunchingConfigWindow
from src.frontend.CustomWidgets.TaskTabIntegrated import MyTaskTab
from src.frontend.CustomWidgets.Jobs import MyJobs
from src.frontend.CustomWidgets.RunBox import MyRunBox
import json
from src.frontend.CustomWidgets.DesignBox import MyDesignBox
import copy
from PyQt5.QtGui import QIntValidator
import threading
from src.backend.Jenkins_APIs import Jenkins

class MyMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.JENKINS_APIs = Jenkins()
        self.setupUi(self)
        self.Tasks.hide()
        self.CreateJobs_button.hide()
        self.CreateTask_button.clicked.connect(self.createTaskTabWidget)

        self.compilation_config = MyCompilationConfigWindow()
        self.launching_configurations = MyLaunchingConfigWindow()
        
        self.design=MyDesignBox("",[],"")
        self.CreateJobs_button.clicked.connect(self.createJobs)
        self.new_window = QMainWindow()
        self.design_widget_layout=QVBoxLayout()
        self.JsonData={}
        self.JsonData[self.Solution_comboBox.currentText()]={}
        self.combinations=list()
        self.Jobslist=list()

        
        
        #self.CreateJobs_button.clicked.connect(self.collectData)

    def createTaskTabWidget(self):
        self.Tasks.TaskTab = MyTaskTab()
        self.combinations.append([])
        self.Jobslist.append([])
        if not self.Tasks.isVisible():
            self.Tasks.show()
            self.CreateJobs_button.show()
            self.Tasks.addTab(self.Tasks.TaskTab , f"Task {self.Tasks.count() + 1}")
        else:
            self.Tasks.addTab(self.Tasks.TaskTab , f"Task {self.Tasks.count() + 1}")
    
    def show_running(self,ShowRun,running, running_dict):
        ShowRun.groupBox.setTitle("Running Configuration ")
        ShowRun.show_data(running_dict)
        ShowRun.myparent=running.myparent
        ShowRun.show()

    def show_design(self,design):

        self.design=design
        self.design.setParent(None)
        self.design.showdesign()
        self.design.show()
        self.design.center_on_parent()
        

    def createJobs(self):
        current_widget = self.Tasks.currentWidget()
        self.runningwindows=[]
        
        if isinstance(current_widget, MyTaskTab) and current_widget.Task_tabWidget.count() < 4:
            self.Job = MyJobs()
            self.Jobslist[self.Tasks.currentIndex()]=self.Job
            current_widget.Task_tabWidget.addTab(self.Job,"Jobs")
        # else:
        #     # Remove the existing MyJobs instance
        #     current_widget.Task_tabWidget.removeTab(3) 
        #     # Create a new instance of MyJobs
        #     self.Job = MyJobs()
        #     current_widget.Task_tabWidget.insertTab(3, self.Job, "Jobs")

        self.Jobslist[self.Tasks.currentIndex()].Run_pushButton.clicked.connect(self.GenerateJson)
        self.Jobslist[self.Tasks.currentIndex()].selectall_pushButton.clicked.connect(self.selectallrows)

        self.combinations[self.Tasks.currentIndex()] = self.collectData()
        self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setRowCount(len(self.combinations[self.Tasks.currentIndex()]))
        self.Jobslist[self.Tasks.currentIndex()].Jobs_table.verticalHeader().setVisible(False)

        for row_index, (running_config, design, build) in enumerate(self.combinations[self.Tasks.currentIndex()] ):

            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox_item.setCheckState(Qt.Unchecked)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, 0, checkbox_item)
            
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, 1, QTableWidgetItem(str(row_index+1)))
            
            
            lineEdit_PrerequisiteTask = QTableWidgetItem()
            lineEdit_PrerequisiteTask.setFlags(lineEdit_PrerequisiteTask.flags() & ~Qt.ItemIsEditable)  # Make the cell not editable
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, 2, lineEdit_PrerequisiteTask)

            # Create a QLineEdit and set it as the cell widget
            text_box = QLineEdit(self.Job)
            text_box.setStyleSheet("QLineEdit { color: white; }")
            validator = QIntValidator()
            text_box.setValidator(validator)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, 2, text_box)
            
            lineEdit_PrerequisiteJob = QTableWidgetItem()
            lineEdit_PrerequisiteJob.setFlags(lineEdit_PrerequisiteJob.flags() & ~Qt.ItemIsEditable)  # Make the cell not editable
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, 3, lineEdit_PrerequisiteJob)

            # Create a QLineEdit and set it as the cell widget
            text_box = QLineEdit(self.Job)
            text_box.setStyleSheet("QLineEdit { color: white; }")
            validator = QIntValidator()
            text_box.setValidator(validator)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, 3, text_box)
            
            running_dict = running_config.running_configurations
            col_index = 4
            scriptPath = running_dict['running_configurations']['script_path']
        
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, col_index, QTableWidgetItem(str(scriptPath)))
            col_index += 1

            ShowRunningConfigB = QPushButton("Show")
            ShowRunningConfigB.setStyleSheet("color: white;")
            self.ShowRun = MyRunBox(0,[],"")
            self.runningwindows.append(self.ShowRun)
            ShowRunningConfigB.clicked.connect(lambda _, ShowRun=self.ShowRun,r=running_config,rd=running_dict: self.show_running(ShowRun,r,rd))
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, col_index, ShowRunningConfigB)
            col_index += 1

            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, col_index , QTableWidgetItem(str(build)))
            col_index += 1

            DesignPath = design.DesignPath_lineEdit.text()
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, col_index , QTableWidgetItem(str(DesignPath)))
            col_index += 1

            ShowDesignConfigB = QPushButton("Show")
            ShowDesignConfigB.setStyleSheet("color: white;")
            ShowDesignConfigB.clicked.connect(lambda _, d=design,: self.show_design(d))
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, col_index, ShowDesignConfigB)
            col_index += 1           

            ShowConsole = QPushButton("Show")
            ShowConsole.setStyleSheet("color: white;")
            self.ShowRun = MyRunBox(0,[],"")
            self.runningwindows.append(self.ShowRun)
            ShowConsole.clicked.connect(lambda _, job_name="job_name": self.open_console(job_name))
            self.Job.Jobs_table.setCellWidget(row_index, 11, ShowConsole)
            col_index += 1

    def open_console(self, job_name: str) -> None:
        self.Job.scrollArea_console.setVisible(True)
        self.Job.console_text.setPlainText(f"Console for {job_name} will go here.")
        self.Job.console_text.repaint()

    def collectData(self):

        Designs = self.Tasks.currentWidget().get_design()
        RunningConfigs = self.Tasks.currentWidget().get_running()
        Builds  = self.Tasks.currentWidget().get_builds()

        for running in RunningConfigs:
            running.collect_running_config()

        self.BinarySearhState=self.Tasks.currentWidget().getBinarySearchValue()

        if(self.BinarySearhState==True):
            if(len(RunningConfigs)!=0 and  len(Designs)!=0):
                RunningConfigsFirstIndex=list()
                DesignConfigsFirstIndex=list() # 3shan product msh btakhod gher list f m7tgha a7ot awel element fy el list el fo2a fy list 
                RunningConfigsFirstIndex.append(RunningConfigs[0])
                DesignConfigsFirstIndex.append(Designs[0])

                combinations = list(product(RunningConfigsFirstIndex, DesignConfigsFirstIndex, Builds))
            else:
                combinations = list(product(RunningConfigs , Designs, Builds))
        else:
            combinations = list(product(RunningConfigs , Designs, Builds))
        return combinations
    
    
    def selectallrows(self):
        for row in  range(len(self.combinations[self.Tasks.currentIndex()] )):
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 0).setCheckState(Qt.Checked)


    def GenerateJson(self):
        file_path = "./frontEnd.json"
        platform=self.Platfrom_comboBox.currentText()
        solution=self.Solution_comboBox.currentText()
        taskNu=self.Tasks.currentIndex()
        
        self.JsonData[solution]["task"+str(taskNu+1)]={}
        self.JsonData[solution]["task"+str(taskNu+1)]["id"]=taskNu+1

        self.JsonData[solution]["task"+str(taskNu+1)]["binary_search"]=self.BinarySearhState
        self.JsonData[solution]["task"+str(taskNu+1)]["jobs"]={}

                       
        with open(file_path, 'w') as json_file:
            
            for currentJobIndex,(running_config, design, build) in enumerate(self.combinations[self.Tasks.currentIndex()] ):
                    if(self.Jobslist[taskNu].Jobs_table.item(currentJobIndex,0).checkState() != 2):
                        continue
                    running_dict = running_config.running_configurations
                    compilationConfigData = design.compilation_config.compilation_configurationsdict
                    ToolConfigData = design.launching_configurations.get_ToolConfig()
                    DutConfigData=[]
                    buildPath=str(build)
                    self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)]={}
                    self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(compilationConfigData)
                    
                    previous_task_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex,2).text()
                    previous_job_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex,3).text()
                    
                    prerequistes={  #############to be changed
                        "prerequisites": {
                        "previous_task_id": int(previous_task_id) if previous_task_id else taskNu+1,
                        "previous_job_id": int(previous_job_id) if previous_job_id else 0
                        },
                    }
                    self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(prerequistes)
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
                    
                    self.JsonData[solution][ "task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(launching_configurations)
                    self.JsonData[solution][ "task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(running_dict)
            json.dump(self.JsonData,json_file, indent=2)
            json_file.write("\n")
            
            


            thread_output = threading.Thread(target=self.JENKINS_APIs.start_jobs_in_batches,
                                                        args=(self.JsonData,3))
            thread_output.start()
        
        
       

                   



        

