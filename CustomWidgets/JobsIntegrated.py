from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from Jobs import Ui_Jobs


class Jobs(QtWidgets.QWidget,Ui_Jobs):
    def __init__(self):
        super(Jobs, self).__init__()
        self.setupUi(self)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()