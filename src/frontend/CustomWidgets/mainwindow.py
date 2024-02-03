from itertools import product
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
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
from PyQt5 import QtGui
import threading
from src.backend.Jenkins_APIs import Jenkins
import config
from PyQt5.QtGui import QIcon
from config import BuildState
from PyQt5.QtCore import Qt, QThread, QObject, pyqtSignal
from src.common.exception import CircularDependencyException
from PyQt5.QtCore import QSize
class MyMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.JENKINS_APIs = Jenkins()
        self.setupUi(self)
        self.Tasks.hide()
        self.CreateJobs_button.hide()
        self.CreateTask_button.clicked.connect(self.createTaskTabWidget)
        self.setWindowIcon(QIcon('src/frontend/IconsImages/siemens_logo_icon.png'))
        self.compilation_config = MyCompilationConfigWindow()
        self.launching_configurations = MyLaunchingConfigWindow()
        
        self.design=MyDesignBox("",[],"")
        self.CreateJobs_button.clicked.connect(self.createJobs)
        self.new_window = QMainWindow()
        self.design_widget_layout=QVBoxLayout()
        self.JsonData={}
        self.JsonData[self.Solution_comboBox.currentText()]={}
        self.timer = self.refresh_every_5_sec_for_jobs()
        self.console_timer = self.refresh_every_5_sec()
        self.console_timer.timeout.connect(self.update_console)
        self.combinations=list()
        self.Jobslist=list()

        self.worker_thread = WorkerThread(self, self.JsonData ,)
        self.worker_thread.error_signal.connect(self.show_error_message)
        
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
        # if(self.design.DesignPath_lineEdit.text() == ""):
        #     self.showWarningMessage("Design Path cannot be empty for Job Creation")
        
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
        self.Jobslist[self.Tasks.currentIndex()].unselectall_pushButton.clicked.connect(self.unselectallrows)

        self.Job.Close_pushButton.clicked.connect(self.close_console)
        

        self.combinations[self.Tasks.currentIndex()] = self.collectData()
        
        self.Job.Jobs_table.setRowCount(len(self.combinations[self.Tasks.currentIndex()]))
        self.Job.Jobs_table.verticalHeader().setVisible(False)
        self.Job.Jobs_table.setRowCount(len(self.combinations[self.Tasks.currentIndex()]))
        self.Job.Jobs_table.verticalHeader().setVisible(False)
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
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, 3, lineEdit_PrerequisiteTask)

            # Create a QLineEdit and set it as the cell widget
            text_box = QLineEdit(self.Job)
            text_box.setStyleSheet("QLineEdit { color: white; }")
            validator = QIntValidator()
            text_box.setValidator(validator)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, 3, text_box)
            
            lineEdit_PrerequisiteJob = QTableWidgetItem()
            lineEdit_PrerequisiteJob.setFlags(lineEdit_PrerequisiteJob.flags() & ~Qt.ItemIsEditable)  # Make the cell not editable
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, 4, lineEdit_PrerequisiteJob)

            # Create a QLineEdit and set it as the cell widget
            text_box = QLineEdit(self.Job)
            text_box.setStyleSheet("QLineEdit { color: white; }")
            validator = QIntValidator()
            text_box.setValidator(validator)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, 4, text_box)
            
            running_dict = running_config.running_configurations
            col_index = 5
            scriptPath = running_dict['running_configurations']['script_path']

            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, col_index , QTableWidgetItem(str(build)))
            col_index += 1

            
            item = QTableWidgetItem(str(os.path.basename(scriptPath)))
            item.setToolTip(scriptPath)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, col_index, item)
            col_index += 1

            DesignPath = design.DesignPath_lineEdit.text()
            item = QTableWidgetItem(str(os.path.basename(DesignPath)))
            item.setToolTip(DesignPath)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setItem(row_index, col_index, item)
            col_index += 1

            ShowRunningConfigB = QPushButton("Show")
            ShowRunningConfigB.setStyleSheet("color: white;")
            self.ShowRun = MyRunBox(0,[],"")
            self.runningwindows.append(self.ShowRun)
            ShowRunningConfigB.clicked.connect(lambda _, ShowRun=self.ShowRun,r=running_config,rd=running_dict: self.show_running(ShowRun,r,rd))
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, col_index, ShowRunningConfigB)
            col_index += 1
        
            ShowDesignConfigB = QPushButton("Show")
            ShowDesignConfigB.setStyleSheet("color: white;")
            ShowDesignConfigB.clicked.connect(lambda _, d=design,: self.show_design(d))
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, col_index, ShowDesignConfigB)
            col_index += 1           

            solution=self.Solution_comboBox.currentText()
            taskNu=self.Tasks.currentIndex()
            job_name_str = f"{solution}-Task{taskNu+1}-Job{row_index+1}"

            self.Job.Jobs_table.setItem(row_index, 2 , QTableWidgetItem(job_name_str))
            col_index += 1 
            self.add_all_jobs_status()

            button_size = QSize(40, 14)
            ShowConsole = QPushButton(" 👁️ ")
            ShowConsole.setStyleSheet("color: white;")
            ShowConsole.setFixedSize(button_size)
            self.ShowRun1 = MyRunBox(0, [], "")
            self.runningwindows.append(self.ShowRun1)
            ShowConsole.clicked.connect(lambda _, job_name=job_name_str: self.open_and_update_console(job_name))

            abort = QPushButton(" ❌ ")
            abort.setStyleSheet("color: white;")
            self.ShowRun2 = MyRunBox(0, [], "")
            abort.setFixedSize(button_size)
            self.runningwindows.append(self.ShowRun2)
            abort.clicked.connect(lambda _, job_name=job_name_str: self.abort_job(job_name))

            trash = QPushButton(" 🗑️  ")
            trash.setStyleSheet("color: white;")
            self.ShowRun3 = MyRunBox(0, [], "")
            trash.setFixedSize(button_size)
            self.runningwindows.append(self.ShowRun3)
            trash.clicked.connect(lambda _, job_name="job_name": self.delete_job(job_name))

            # Create a horizontal layout
            button_layout = QHBoxLayout()
            button_layout.addWidget(ShowConsole)
            button_layout.addWidget(abort)
            button_layout.addWidget(trash)

            # Set the layout as the cell widget
            cell_widget = QWidget()
            cell_widget.setLayout(button_layout)

            self.Job.Jobs_table.setCellWidget(row_index, 11, cell_widget)
            col_index += 1



                     

    def close_console(self, job_name: str):
        self.Job.scrollArea_console.setVisible(False)
        self.Job.Close_pushButton.setVisible(False)

    def open_and_update_console(self, job_name: str):
        self.open_console(job_name)
        self.Job.scrollArea_console.setVisible(True)
        self.Job.Close_pushButton.setVisible(True)

        self.current_job_name = job_name


    def update_console(self):
        if hasattr(self, 'current_job_name'):
            self.open_console(self.current_job_name)

    def open_console(self, job_name: str) -> None:        
        success, console_output = self.JENKINS_APIs.get_job_console_output(job_name)
        if success:
            self.Job.console_text.setPlainText(console_output)
        else:
            self.Job.console_text.setPlainText(f"Job {job_name} has not started.")

        scrollbar = self.Job.console_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        self.Job.console_text.repaint()

    def abort_job(self, job_name: str) -> None:
        success, message= self.JENKINS_APIs.stop_job(job_name)

        self.Job.scrollArea_console.setVisible(True)
        if success:
            self.Job.console_text.setPlainText(f"Job '{job_name}' aborted successfully")
        else:
            self.Job.console_text.setPlainText(f"Job {job_name} has not started.")
        self.Job.console_text.repaint()



    def delete_job(self, job_name: str) -> None:
        self.Job.scrollArea_console.setVisible(True)
        self.Job.console_text.setPlainText(f"Console for {job_name} will go here.")
        self.Job.console_text.repaint()


    def refresh_every_5_sec(self) -> QtCore.QTimer:
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_console)
        timer.start(5000)
        return timer

    def add_all_jobs_status(self) -> None:
        original_dict = self.JENKINS_APIs.get_all_status()
        jobs = [{job:status} for job, status in original_dict.items()]
        
    #    for job_index in range(len(jobs)):
    #         self.add_job(jobs[job_index])
    def showWarningMessage(self , input):
        warning_dialog = QMessageBox(self)
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle('Empty String')
        warning_dialog.setText(f'Error : {input}')
        warning_dialog.show()
        


    def refresh_job(self, job_name: str, job_status: str) -> None:
        number_of_rows = self.Job.Jobs_table.rowCount()
        job_row = -1
        for row in range(number_of_rows):
            if self.Job.Jobs_table.item(row, 2).text() == job_name:
                job_row = row
                break
        if job_row >= 0:
            status_item = QTableWidgetItem("")
            label = QLabel(job_status)
            
            # match case but needs python 3.10 upwards
             
            if job_status == "SUCCESS":
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet("color: green; text-align: center; font-weight: bold;") 
                self.Job.Jobs_table.setCellWidget(job_row, 10, label)  
            elif job_status == "FAILURE":
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet("color: red; text-align: center; font-weight: bold;")
                self.Job.Jobs_table.setCellWidget(job_row, 10, label) 
            elif job_status == BuildState.JOB_CREATED.description:
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet(f"color: {BuildState.JOB_CREATED.color}; text-align: center; font-weight: bold;")
                self.Job.Jobs_table.setCellWidget(job_row, 10, label)
            elif job_status == BuildState.JOB_CRASHED.description:
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet(f"color: {BuildState.JOB_CRASHED.color}; text-align: center; font-weight: bold;")
                self.Job.Jobs_table.setCellWidget(job_row, 10, label)
            elif job_status == BuildState.JOB_IN_BATCH.description:
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet(f"color: {BuildState.JOB_IN_BATCH.color}; text-align: center; font-weight: bold;")
                self.Job.Jobs_table.setCellWidget(job_row, 10, label)
            elif job_status == BuildState.JOB_STARTED.description:
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet(f"color: {BuildState.JOB_STARTED.color}; text-align: center; font-weight: bold;")
                self.Job.Jobs_table.setCellWidget(job_row, 10, label)
            elif job_status[:len(BuildState.CHILD_JOB_FAILED.description)] == BuildState.CHILD_JOB_FAILED.description:
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet("color: red; text-align: center; font-weight: bold;")
                self.Job.Jobs_table.setCellWidget(job_row, 10, label)
            else:
                self.Job.Jobs_table.setItem(job_row, 10, status_item)
                label.setStyleSheet("color: grey; text-align: center; font-weight: bold;")
                self.Job.Jobs_table.setCellWidget(job_row, 10, label)
                
    def refresh_all_jobs(self) -> None:
        original_dict = self.JENKINS_APIs.get_all_status()
        jobs = [{job:status} for job, status in original_dict.items()]

        for job_index in range(len(jobs)):
            job_name = list(jobs[job_index].items())[0][0]
            job_status = list(jobs[job_index].items())[0][1]
            self.refresh_job(job_name, job_status)

    def refresh_every_5_sec_for_jobs(self) -> QtCore.QTimer:
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.refresh_all_jobs)
        timer.start(5000)
        return timer
    
    def collectData(self):

        Designs = self.Tasks.currentWidget().get_design()
        #print(self.Tasks.cuurentwidget().
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

    def unselectallrows(self):
        for row in  range(len(self.combinations[self.Tasks.currentIndex()] )):
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 0).setCheckState(Qt.Unchecked)


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
                    
                    previous_task_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex,3).text()
                    previous_job_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex,4).text()
                    
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
            
            
            self.worker_thread.json_data = self.JsonData
            self.worker_thread.start()


    def show_error_message(self, error_message):
        QMessageBox.warning(self, "Dependency Failure", f"<b>{error_message}</b>")





class WorkerThread(QThread, QObject):
    error_signal = pyqtSignal(str)

    def __init__(self,main_window, json_data):
        super().__init__()
        self.main_window = main_window
        self.json_data = json_data


    def run(self):
        try:
            self.main_window.JENKINS_APIs.start_jobs_in_batches(self.json_data, 3)
        except CircularDependencyException as e:
            self.error_signal.emit(str(e))