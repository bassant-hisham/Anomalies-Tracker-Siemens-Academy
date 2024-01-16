from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from UIs.JobsUI import Ui_Jobs


class MyJobs(QtWidgets.QWidget,Ui_Jobs):
    def __init__(self):
        super(MyJobs, self).__init__()
        self.setupUi(self)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()