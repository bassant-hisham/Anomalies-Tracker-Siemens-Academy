# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Jobs.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Jobs(object):
    def setupUi(self, Jobs):
        Jobs.setObjectName("Jobs")
        Jobs.resize(796, 527)
        Jobs.setStyleSheet("QWidget{\n"
"background-color:rgb(37, 40, 50);\n"
"    color: white;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QFrame QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Jobs)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Jobs)
        self.scrollArea.setStyleSheet("color:rgb(37, 40, 50);\n"
"QTableWidget::item{\n"
"background-color:rgb(37, 40, 50);\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 772, 503))
        self.scrollAreaWidgetContents_3.setStyleSheet("QWidget::pane{\n"
"border-color:none;\n"
"\n"
"background-color:rgb(37, 40, 50);\n"
"}\n"
"\n"
"")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.tableWidget.setStyleSheet("QTableWidget::item {\n"
"background-color:rgb(37, 40, 50);\n"
"color:white;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(29)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Jobs)
        QtCore.QMetaObject.connectSlotsByName(Jobs)

    def retranslateUi(self, Jobs):
        _translate = QtCore.QCoreApplication.translate
        Jobs.setWindowTitle(_translate("Jobs", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Jobs", "Include"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Jobs", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Jobs", "Script Path"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Jobs", "Run Script"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Jobs", "Error Type"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Jobs", "Attach GDB"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Jobs", "EPGM"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Jobs", "DPI"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Jobs", "Controller"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Jobs", "Environment Path"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Jobs", "Design Path"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Jobs", "Compile Design"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Jobs", "Source Design Path"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Jobs", "Output Directory"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Jobs", "Force"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Jobs", "Timeout"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Jobs", "Launch DPI"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Jobs", "Terminate DPI"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Jobs", "Terminate DPI on Error"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Jobs", "Design Path (Launch)"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("Jobs", "Design Path"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("Jobs", "Record Directory"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("Jobs", "Configuration Value"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("Jobs", "Replay Directory"))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("Jobs", "Reply Directory"))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("Jobs", "DPI Launch Mode"))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("Jobs", "DPI Launch Type"))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("Jobs", "Use Custom Comodel Config"))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("Jobs", "Custom Comodel Config"))