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
        # self.JsonData={}
        # self.JsonData[self.Solution_comboBox.currentText()]={}
        self.timer = self.refresh_every_5_sec_for_jobs()
        self.console_timer = self.refresh_every_5_sec()
        self.console_timer.timeout.connect(self.update_console)
        self.combinations=list()
        self.Jobslist=list()
        self.CreateJobs_button.clicked.connect(self.collectData)
        self.undoShortcut = QShortcut(Qt.CTRL + Qt.Key_Z, self)
        self.undoShortcut.activated.connect(self.undo_hide_job)
        self.undoStack = []
        self.buttons_db = {}

        
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
        
    def checkError(self):

        current_index = self.Tasks.currentWidget().stacked_widget.currentIndex() #use it to know which of dir or file is used (0->Dir , 1->File)
        parent_directory = self.Tasks.currentWidget().ParentDir_lineEdit.text()
        
        self.error_free = True  
        
        if current_index == 1:
            if (self.Tasks.currentWidget().FilePath_lineEdit.text()==""):  
                QMessageBox.warning(self, "Empty File Path", f"<b>Please enter build's File Path</b>")
                self.error_free = False
        elif (parent_directory ==""):
                QMessageBox.warning(self, "Empty Directory Path", f"<b>Please enter build's directory</b>")
                self.error_free = False
        
        if(parent_directory != ""):
            bash_files = [file for file in os.listdir(parent_directory) if file.endswith('.bash')]
        
        if(parent_directory != "" and not bash_files):
            QMessageBox.warning(self, "Missing Bash Files", f"<b>There are no bash files in the parent directory in \'Enviroments\' tab</b>")
            self.error_free = False
            
                    
        for running in self.Tasks.currentWidget().Running_data:
                if running.ScriptPath_lineEdit.text()=="":
                    QMessageBox.warning(self, "Empty Running Script", f"<b>Please enter a Running File Path</b>") 

        for design in self.Tasks.currentWidget().Design_data:
                if design.DesignPath_lineEdit.text()=="" :
                    QMessageBox.warning(self, "Empty Design path", f"<b>Please enter a Design Path</b>")
                    self.error_free = False 


    def createJobs(self):
        current_widget = self.Tasks.currentWidget()
        self.runningwindows=[]
        self.checkError()
        
        if(self.error_free):
            if isinstance(current_widget, MyTaskTab) and current_widget.Task_tabWidget.count() < 4:
                self.Job = MyJobs()
                self.Jobslist[self.Tasks.currentIndex()]=self.Job
                
                current_widget.Task_tabWidget.addTab(self.Job,"Jobs")

            self.Jobslist[self.Tasks.currentIndex()].Run_pushButton.clicked.connect(self.GenerateJson)
            self.Jobslist[self.Tasks.currentIndex()].selectall_pushButton.clicked.connect(self.selectallrows)
            self.Jobslist[self.Tasks.currentIndex()].unselectall_pushButton.clicked.connect(self.unselectallrows)

            self.Job.Close_pushButton.clicked.connect(self.close_console)
            

            self.combinations[self.Tasks.currentIndex()]=self.collectData()
            
            self.Job.Jobs_table.setRowCount(len(self.combinations[self.Tasks.currentIndex()]))
            self.Job.Jobs_table.verticalHeader().setVisible(False)
            self.Job.Jobs_table.setRowCount(len(self.combinations[self.Tasks.currentIndex()]))
            self.Job.Jobs_table.verticalHeader().setVisible(False)
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setRowCount(len(self.combinations[self.Tasks.currentIndex()]))
            self.Jobslist[self.Tasks.currentIndex()].Jobs_table.verticalHeader().setVisible(False)
            
            


            for row_index,(running_config, design, build )in enumerate(self.combinations[self.Tasks.currentIndex()]) :
                
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
                
                #self.refresh_job(job_name_str, "New Job Created")
                self.add_all_jobs_status()

                button_size = QSize(40, 14)
                ShowConsole = QPushButton(" 👁️ ")
                ShowConsole.setStyleSheet("color: white;")
                ShowConsole.setFixedSize(button_size)
                self.ShowRun1 = MyRunBox(0, [], "")
                self.runningwindows.append(self.ShowRun1)
                ShowConsole.clicked.connect(lambda _, job_name=job_name_str: self.open_and_update_console(job_name))
                ShowConsole.setToolTip("Show Output")  
                ShowConsole.setStyleSheet("color: rgb(37, 40, 50);")
                
                abort = QPushButton(" ❌ ")
                abort.setStyleSheet("color: white;")
                self.ShowRun2 = MyRunBox(0, [], "")
                abort.setFixedSize(button_size)
                self.runningwindows.append(self.ShowRun2)
                abort.clicked.connect(lambda _, job_name=job_name_str: self.abort_job(job_name))
                abort.setToolTip("Abort")
                abort.setStyleSheet("color: rgb(37, 40, 50);")
                
                
                trash = QPushButton(" 🗑️  ")
                trash.setStyleSheet("color: white;")
                self.ShowRun3 = MyRunBox(0, [], "")
                trash.setFixedSize(button_size)
                self.runningwindows.append(self.ShowRun3)
                trash.clicked.connect(lambda _, job_name= job_name_str: self.delete_job(job_name))
                trash.setToolTip("Delete")  
                trash.setStyleSheet("color: rgb(37, 40, 50);")
                
                
                hide = QPushButton("🚫")
                hide.setStyleSheet("color: white;")
                self.ShowRun4 = MyRunBox(0, [], "")
                hide.setFixedSize(button_size)
                self.runningwindows.append(self.ShowRun4)
                hide.clicked.connect(lambda _, job_name= job_name_str: self.hide_job(job_name))
                hide.setToolTip("Hide")  
                hide.setStyleSheet("color: rgb(37, 40, 50);")
                # Create a horizontal layout
                button_layout = QHBoxLayout()
                button_layout.addWidget(ShowConsole)
                button_layout.addWidget(abort)
                button_layout.addWidget(hide)
                button_layout.addWidget(trash)

                # Set the layout as the cell widget
                cell_widget = QWidget()
                cell_widget.setLayout(button_layout)

                #self.Job.Jobs_table.setCellWidget(row_index, 11, cell_widget)
                self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(row_index, 11 , cell_widget)
                col_index += 1



                     

    def close_console(self, job_name: str):
        self.Jobslist[self.Tasks.currentIndex()].scrollArea_console.setVisible(False)
        self.Jobslist[self.Tasks.currentIndex()].Close_pushButton.setVisible(False)

    def open_and_update_console(self, job_name: str):
        self.open_console(job_name)
        self.Jobslist[self.Tasks.currentIndex()].scrollArea_console.setVisible(True)
        self.Jobslist[self.Tasks.currentIndex()].Close_pushButton.setVisible(True)
        print(job_name)
        self.current_job_name = job_name


    def update_console(self):
        if hasattr(self, 'current_job_name'):
            self.open_console(self.current_job_name)

    def open_console(self, job_name: str) -> None:        
        success, console_output = self.JENKINS_APIs.get_job_console_output(job_name)
        if(self.Jobslist[self.Tasks.currentIndex()]):
            if success:
                self.Jobslist[self.Tasks.currentIndex()].console_text.setPlainText(console_output)
            else:
                self.Jobslist[self.Tasks.currentIndex()].console_text.setPlainText(f"Job {job_name} has not started.")

            scrollbar = self.Jobslist[self.Tasks.currentIndex()].console_text.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            self.Jobslist[self.Tasks.currentIndex()].console_text.repaint()

    def abort_job(self, job_name: str) -> None:
        success, message= self.JENKINS_APIs.stop_job(job_name)

        self.Jobslist[self.Tasks.currentIndex()].scrollArea_console.setVisible(True)
        if success:
            self.Jobslist[self.Tasks.currentIndex()].console_text.setPlainText(f"Job '{job_name}' aborted successfully")
        else:
            self.Jobslist[self.Tasks.currentIndex()].console_text.setPlainText(f"Job {job_name} has not started.")
        self.Jobslist[self.Tasks.currentIndex()].console_text.repaint()



    def hide_job(self, job_name: str) -> None:
        
        for row in range(self.Job.Jobs_table.rowCount()):
            item = self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 2)
            
            if item is not None and item.text() == job_name:
                self.undoStack.append(row)  # Store only the row number since the row is not being deleted.
                self.Jobslist[self.Tasks.currentIndex()].Jobs_table.hideRow(row)
                break  


    
    def undo_hide_job(self):
        if not self.undoStack:
            print("No actions to undo.")
            return

        row = self.undoStack.pop()  # Get the last hidden row's number.
        self.Jobslist[self.Tasks.currentIndex()].Jobs_table.showRow(row)  # Make the row visible again.

        print(f"Row {row} restored.")
        
    def delete_job(self, job_name: str) -> None:
        
        reply = QMessageBox.question(self, 'Confirm Deletion', 
                                 f"Are you sure you want to delete the job '{job_name}' from the Jenkins Server?", 
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            for row in range(self.Job.Jobs_table.rowCount()):
                item = self.Job.Jobs_table.item(row, 2)
                if item is not None and item.text() == job_name:
                    self.Job.Jobs_table.removeRow(row)
                    break
                
        try:
             self.JENKINS_APIs.delete_job(job_name)
             raise Exception("Job not in the server to be deleted")
        except:
             print("Exception occured")

    def refresh_every_5_sec(self) -> QtCore.QTimer:
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_console)
        timer.start(5000)
        return timer

    def add_all_jobs_status(self) -> None:
        original_dict = self.JENKINS_APIs.get_all_status()
        jobs = [{job:status} for job, status in original_dict.items()]
        
        
    def showWarningMessage(self , input):
        warning_dialog = QMessageBox(self)
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle('Empty String')
        warning_dialog.setText(f'Error : {input}')
        warning_dialog.show()
        


    def refresh_job(self, job_name: str, job_status: str) -> None:
        
        self.check_num_of_rows = False
        
        if(self.Jobslist[self.Tasks.currentIndex()]):
            number_of_rows = self.Jobslist[self.Tasks.currentIndex()].Jobs_table.rowCount()
            self.check_num_of_rows = True
            job_row = -1
            
            for row in range(number_of_rows):
                if self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 2).text() == job_name:
                    job_row = row
                    break
            if job_row >= 0:
                label = QLabel(job_status)
                color = BuildState.get_color_by_description(job_status)
                label.setStyleSheet(f"color: {color}; text-align: center; font-weight: bold;")
                label.setAlignment(Qt.AlignCenter) 
                self.Jobslist[self.Tasks.currentIndex()].Jobs_table.setCellWidget(job_row, 10, label)  
                
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
        RunningConfigs = self.Tasks.currentWidget().get_running()
        Builds  = self.Tasks.currentWidget().get_builds()

        for running in RunningConfigs:
            running.collect_running_config()

        self.BinarySearchState=self.Tasks.currentWidget().getBinarySearchValue()
        
        #if(self.BinarySearchState==True):
            
        
        if(self.BinarySearchState==True):
            if(len(RunningConfigs)!=0 and  len(Designs)!=0):
                RunningConfigsFirstIndex=list()
                DesignConfigsFirstIndex=list() 
                RunningConfigsFirstIndex.append(RunningConfigs[0])
                DesignConfigsFirstIndex.append(Designs[0])

                combinations= list(product(RunningConfigsFirstIndex, DesignConfigsFirstIndex, Builds))            
                
            else:
                combinations= list(product(RunningConfigs , Designs, Builds))
        else:
            combinations= list(product(RunningConfigs , Designs, Builds))
        return combinations
        

    
    
    
    def selectallrows(self):
        for row in  range(len(self.combinations[self.Tasks.currentIndex()] )):
            if(self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 0)):
                self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 0).setCheckState(Qt.Checked)

    def unselectallrows(self):
        for row in  range(len(self.combinations[self.Tasks.currentIndex()] )):
            if(self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 0)):
                self.Jobslist[self.Tasks.currentIndex()].Jobs_table.item(row, 0).setCheckState(Qt.Unchecked)


    # def GenerateJson(self):
    #     file_path = "./frontEnd.json"
    #     platform=self.Platfrom_comboBox.currentText()
    #     solution=self.Solution_comboBox.currentText()
    #     taskNu=self.Tasks.currentIndex()
    #     self.JsonData={}
    #     self.JsonData[self.Solution_comboBox.currentText()]={}
        
    #     self.worker_thread = WorkerThread(self, self.JsonData ,)
    #     self.worker_thread.error_signal.connect(self.show_error_message)
        
    #     self.JsonData[solution]["task"+str(taskNu+1)]={}
    #     self.JsonData[solution]["task"+str(taskNu+1)]["id"]=taskNu+1

    #     self.JsonData[solution]["task"+str(taskNu+1)]["binary_search"]= self.BinarySearchState
    #     self.JsonData[solution]["task"+str(taskNu+1)]["jobs"]={}

    #     file_path = "./frontEnd.json"                           
    #     with open(file_path, 'w') as json_file:
        
    #             for currentJobIndex,(running_config, design, build) in enumerate(self.combinations[self.Tasks.currentIndex()] ):

    #                         if(self.Jobslist[taskNu].Jobs_table.item(currentJobIndex,0)):
    #                             if(self.Jobslist[taskNu].Jobs_table.item(currentJobIndex,0).checkState() != 2):
    #                                     continue
    #                             running_dict = running_config.running_configurations
    #                             compilationConfigData = design.compilation_config.compilation_configurationsdict
    #                             ToolConfigData = design.launching_configurations.get_ToolConfig()
    #                             DutConfigData=[]
    #                             buildPath=str(build)
    #                             self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)]={}
    #                             self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(compilationConfigData)
                                
    #                             previous_task_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex,3).text()
                                
    #                             previous_job_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex,4).text()
                                
    #                             prerequistes={  ############# to be changed
    #                                 "prerequisites": {
    #                                 "previous_task_id": int(previous_task_id) if previous_task_id else taskNu+1,
    #                                 "previous_job_id": int(previous_job_id) if previous_job_id else 0
    #                                 },
    #                             }
    #                             self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(prerequistes)
    #                             Duts = design.get_Duts()
    #                             for dut in Duts:
    #                                 DutConfigData.append(dut.collect_data())
                                
    #                             launching_configurations={
    #                                 "launching_configurations": {
    #                                             "$schema": "../schemas/launching_configuration.schema.json",
    #                                             "platform": platform,
    #                                             "solution": solution, 
    #                                             "src_file": buildPath,
    #                                             "dut_configuration":DutConfigData,
    #                                             "tools_configuration":ToolConfigData,
    #                                     }
    #                             }
                                
    #                             self.JsonData[solution][ "task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(launching_configurations)
    #                             self.JsonData[solution][ "task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(running_dict)
            
    #             json.dump(self.JsonData,json_file, indent=2)
    #             json_file.write("\n")
                
                
    #             self.worker_thread.json_data = self.JsonData
                
    #             self.worker_thread.start()


    def GenerateJson(self):
        
        
        file_path = "./frontEnd.json"
        platform = self.Platfrom_comboBox.currentText()
        solution = self.Solution_comboBox.currentText()
        self.DUT_Id = 0
        self.JsonData={}
        self.JsonData[self.Solution_comboBox.currentText()] = {}

        self.worker_thread = WorkerThread(self, self.JsonData , self.BinarySearchState, parent=self)
        self.worker_thread.error_signal.connect(self.show_error_message)
        with open(file_path, 'w') as json_file:
            for taskNu in range(self.Tasks.count()):
                self.JsonData[solution]["task"+str(taskNu+1)] = {}
                self.JsonData[solution]["task"+str(taskNu+1)]["id"] = taskNu+1

                self.JsonData[solution]["task"+str(taskNu+1)]["binary_search"] = self.BinarySearchState
                self.JsonData[solution]["task"+str(taskNu+1)]["jobs"] = {}

                for currentJobIndex, (running_config, design, build) in enumerate(self.combinations[taskNu]):
                    if self.Jobslist[taskNu].Jobs_table.item(currentJobIndex, 0):
                        if self.Jobslist[taskNu].Jobs_table.item(currentJobIndex, 0).checkState() != 2:
                            continue
                        running_dict = running_config.running_configurations
                        compilationConfigData = design.compilation_config.compilation_configurationsdict
                        ToolConfigData = design.launching_configurations.get_ToolConfig()
                        DutConfigData = []
                        buildPath = str(build)
                        previous_task_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex, 3).text()
                        previous_job_id = self.Jobslist[taskNu].Jobs_table.cellWidget(currentJobIndex, 4).text()
                        
                        self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)] = {}

                        prerequistes = {
                            "prerequisites": {
                                "previous_task_id": int(previous_task_id) if previous_task_id else taskNu+1,
                                "previous_job_id": int(previous_job_id) if previous_job_id else 0,
                                
                            }
                            
                        }
                        self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(prerequistes)
                        
                        
                        self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(compilationConfigData)
                        
                        Duts = design.get_Duts()
                        for dut in Duts:
                            DutConfigData.append(dut.collect_data())
                            
                        
                        launching_configurations = {
                            "launching_configurations": {
                                "$schema": "../schemas/launching_configuration.schema.json",
                                "platform": platform,
                                "solution": solution, 
                                "src_file": buildPath,
                                "tools_configuration": ToolConfigData,
                                #"DUT-launch-dpi" : DutConfigData[0]["launch_dpi"]
                            }
                        }
                        
                        print("TOOLS CONFIG : --------")
                        print(ToolConfigData)
                        
                        # if DutConfigData[0]["launch_dpi"] is True:
                        #      launching_configurations["launching_configurations"]["dut_configuration"] = DutConfigData
        
                        self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(launching_configurations)
                        self.JsonData[solution]["task"+str(taskNu+1)]["jobs"][str(currentJobIndex+1)].update(running_dict)
                        
                        
            
            json.dump(self.JsonData, json_file, indent=2)
            json_file.write("\n")
            
            self.worker_thread.json_data = self.JsonData
            self.worker_thread.isbinarysearch = self.BinarySearchState
            self.worker_thread.start()




    def show_error_message(self, error_message):
        QMessageBox.warning(self, "Dependency Failure", f"<b>{error_message}</b>")





class WorkerThread(QThread, QObject):
    error_signal = pyqtSignal(str)

    def __init__(self,main_window, json_data, isbinarysearch, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.json_data = json_data
        self.isbinarysearch = isbinarysearch


    def run(self):
        try:
            self.main_window.JENKINS_APIs.start_jobs_in_batches(self.json_data,self.isbinarysearch, 3)
        except CircularDependencyException as e:
            self.error_signal.emit(str(e))
            
