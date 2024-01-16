from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
from CompilationConfigurationWindow import MyCompilationConfigWindow
from LanchuiningConfigurationWindow import LaunchingConfigurations
from TaskTabIntegrated import MyTaskTab
from JobsIntegrated import Jobs

class MyMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)
        self.Job.hide()
        self.pushButtonCreate_2.hide()
        self.pushButtonCreate.clicked.connect(self.createTaskTabWidget)
        self.compilation_config = MyCompilationConfigWindow()
        self.launching_configurations = LaunchingConfigurations()
        self.pushButtonCreate_2.clicked.connect(self.createJobs)

    def createTaskTabWidget(self):
        self.Job.TaskTab = MyTaskTab()
        if not self.Job.isVisible():
            self.Job.show()
            self.pushButtonCreate_2.show()
            self.Job.addTab(self.Job.TaskTab , f"Task {self.Job.count() + 1}")
        else:
            self.Job.addTab(self.Job.TaskTab , f"Task {self.Job.count() + 1}")
    
    def createJobs(self):
        current_widget = self.Job.currentWidget()
        Design  = self.Job.TaskTab.GetDesign()
        if isinstance(current_widget, MyTaskTab) and current_widget.tabWidget.count() < 4:
            current_widget.tabWidget.addTab(Jobs(),"Jobs")
        # current_widget.custom_window.collect_running_config()