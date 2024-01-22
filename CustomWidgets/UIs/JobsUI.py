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
        Jobs.resize(796, 606)
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
        self.Jobs_scrollArea = QtWidgets.QWidget()
        self.Jobs_scrollArea.setGeometry(QtCore.QRect(0, 0, 776, 586))
        self.Jobs_scrollArea.setStyleSheet("QWidget::pane{\n"
"border-color:none;\n"
"\n"
"background-color:rgb(37, 40, 50);\n"
"}\n"
"\n"
"")
        self.Jobs_scrollArea.setObjectName("Jobs_scrollArea")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Jobs_scrollArea)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Jobs_table = QtWidgets.QTableWidget(self.Jobs_scrollArea)
        self.Jobs_table.setStyleSheet("QTableWidget::item {\n"
"background-color:rgb(37, 40, 50);\n"
"color:white;\n"
"}")
        self.Jobs_table.setObjectName("Jobs_table")
        self.Jobs_table.setColumnCount(28)
        self.Jobs_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.Jobs_table.setHorizontalHeaderItem(27, item)
        self.gridLayout_2.addWidget(self.Jobs_table, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(580, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Run_pushButton = QtWidgets.QPushButton(self.Jobs_scrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Run_pushButton.sizePolicy().hasHeightForWidth())
        self.Run_pushButton.setSizePolicy(sizePolicy)
        self.Run_pushButton.setMinimumSize(QtCore.QSize(100, 35))
        self.Run_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: red;\n"
"    color:White;\n"
"    margin-right:5px;\n"
"    border-radius: 10px;\n"
"    border: 0px solid rgb(52, 59, 72);\n"
"    font-size:16px;\n"
"    font-weight:bold;\n"
"\n"
"}\n"
"")
        self.Run_pushButton.setObjectName("Run_pushButton")
        self.horizontalLayout.addWidget(self.Run_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.Jobs_scrollArea)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Jobs)
        QtCore.QMetaObject.connectSlotsByName(Jobs)

    def retranslateUi(self, Jobs):
        _translate = QtCore.QCoreApplication.translate
        Jobs.setWindowTitle(_translate("Jobs", "Form"))
        item = self.Jobs_table.horizontalHeaderItem(0)
        item.setText(_translate("Jobs", "Include"))
        item = self.Jobs_table.horizontalHeaderItem(1)
        item.setText(_translate("Jobs", "ID"))
        item = self.Jobs_table.horizontalHeaderItem(2)
        item.setText(_translate("Jobs", "Script Path"))
        item = self.Jobs_table.horizontalHeaderItem(3)
        item.setText(_translate("Jobs", "Run Script"))
        item = self.Jobs_table.horizontalHeaderItem(4)
        item.setText(_translate("Jobs", "Error Type"))
        item = self.Jobs_table.horizontalHeaderItem(5)
        item.setText(_translate("Jobs", "Crashed Process"))
        item = self.Jobs_table.horizontalHeaderItem(6)
        item.setText(_translate("Jobs", "Attach GDB"))
        item = self.Jobs_table.horizontalHeaderItem(7)
        item.setText(_translate("Jobs", "Build"))
        item = self.Jobs_table.horizontalHeaderItem(8)
        item.setText(_translate("Jobs", "Design Path"))
        item = self.Jobs_table.horizontalHeaderItem(9)
        item.setText(_translate("Jobs", "Environment Path"))
        item = self.Jobs_table.horizontalHeaderItem(10)
        item.setText(_translate("Jobs", "Compile Design"))
        item = self.Jobs_table.horizontalHeaderItem(11)
        item.setText(_translate("Jobs", "Source Design Path"))
        item = self.Jobs_table.horizontalHeaderItem(12)
        item.setText(_translate("Jobs", "Output Directory"))
        item = self.Jobs_table.horizontalHeaderItem(13)
        item.setText(_translate("Jobs", "Force"))
        item = self.Jobs_table.horizontalHeaderItem(14)
        item.setText(_translate("Jobs", "Timeout"))
        item = self.Jobs_table.horizontalHeaderItem(15)
        item.setText(_translate("Jobs", "Launch DPI"))
        item = self.Jobs_table.horizontalHeaderItem(16)
        item.setText(_translate("Jobs", "Terminate DPI"))
        item = self.Jobs_table.horizontalHeaderItem(17)
        item.setText(_translate("Jobs", "Terminate DPI on Error"))
        item = self.Jobs_table.horizontalHeaderItem(18)
        item.setText(_translate("Jobs", "Design Path (Launch)"))
        item = self.Jobs_table.horizontalHeaderItem(19)
        item.setText(_translate("Jobs", "Design Path"))
        item = self.Jobs_table.horizontalHeaderItem(20)
        item.setText(_translate("Jobs", "Record Directory"))
        item = self.Jobs_table.horizontalHeaderItem(21)
        item.setText(_translate("Jobs", "Configuration Value"))
        item = self.Jobs_table.horizontalHeaderItem(22)
        item.setText(_translate("Jobs", "Replay Directory"))
        item = self.Jobs_table.horizontalHeaderItem(23)
        item.setText(_translate("Jobs", "Reply Directory"))
        item = self.Jobs_table.horizontalHeaderItem(24)
        item.setText(_translate("Jobs", "DPI Launch Mode"))
        item = self.Jobs_table.horizontalHeaderItem(25)
        item.setText(_translate("Jobs", "DPI Launch Type"))
        item = self.Jobs_table.horizontalHeaderItem(26)
        item.setText(_translate("Jobs", "Use Custom Comodel Config"))
        item = self.Jobs_table.horizontalHeaderItem(27)
        item.setText(_translate("Jobs", "Custom Comodel Config"))
        self.Run_pushButton.setText(_translate("Jobs", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Jobs = QtWidgets.QWidget()
    ui = Ui_Jobs()
    ui.setupUi(Jobs)
    Jobs.show()
    sys.exit(app.exec_())
