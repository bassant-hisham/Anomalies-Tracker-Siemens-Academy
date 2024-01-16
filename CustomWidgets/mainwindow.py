from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from MainWindowUI import Ui_MainWindow
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
        Design  = self.Tasks.TaskTab.GetDesign()
        if isinstance(current_widget, MyTaskTab) and current_widget.tabWidget.count() < 4:
            current_widget.tabWidget.addTab(MyJobs(),"Jobs")
        # current_widget.custom_window.collect_running_config()