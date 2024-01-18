from itertools import product
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from UIs.MainWindowUI import Ui_MainWindow
from CompilationConfigurationWindow import MyCompilationConfigWindow
from LaunchingConfigurationWindow import MyLaunchingConfigWindow
from TaskTabIntegrated import MyTaskTab
from Jobs import MyJobs

class MyMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)
        self.Tasks.hide()
        self.pushButtonCreate_2.hide()
        self.pushButtonCreate.clicked.connect(self.createTaskTabWidget)
        self.compilation_config = MyCompilationConfigWindow()
        self.launching_configurations = MyLaunchingConfigWindow()
        self.pushButtonCreate_2.clicked.connect(self.createJobs)
        #self.pushButtonCreate_2.clicked.connect(self.collectData)

    def createTaskTabWidget(self):
        self.Tasks.TaskTab = MyTaskTab()
        if not self.Tasks.isVisible():
            self.Tasks.show()
            self.pushButtonCreate_2.show()
            self.Tasks.addTab(self.Tasks.TaskTab , f"Task {self.Tasks.count() + 1}")
        else:
            self.Tasks.addTab(self.Tasks.TaskTab , f"Task {self.Tasks.count() + 1}")
    
    def createJobs(self):
        current_widget = self.Tasks.currentWidget()
        if isinstance(current_widget, MyTaskTab) and current_widget.tabWidget.count() < 4:
            Job = MyJobs()
            combinations = self.collectData()
            Job.tableWidget.setRowCount(len(combinations))
            for row_index, (running_config, design, build) in enumerate(combinations):
                Job.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(row_index)))
                running_dict = running_config.custom_window.running_configurations
                col_index = 2
                for (num,(key,value)) in enumerate(running_dict.items()):
                    Job.tableWidget.setItem(row_index, col_index , QTableWidgetItem(str(value)))
                    col_index += 1
                Job.tableWidget.setItem(row_index, col_index , QTableWidgetItem(str(build)))
                col_index += 1

            current_widget.tabWidget.addTab(Job,"Jobs")
            

    def collectData(self):
        Designs = self.Tasks.TaskTab.get_design()
        RunningConfigs = self.Tasks.TaskTab.get_running()
        Builds  = self.Tasks.TaskTab.get_builds()
        for running in RunningConfigs:
           running.custom_window.collect_running_config()
        for designs in Designs:
            Duts = designs.get_Duts()
            for dut in Duts:
                dut.collect_data()
        combinations = list(product(RunningConfigs , Designs, Builds))
        return combinations
    
        
        
       

                   



        

