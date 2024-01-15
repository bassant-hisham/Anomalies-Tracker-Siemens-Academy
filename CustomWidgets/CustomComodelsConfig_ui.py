# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Siemens diploma\Final project\task2\task2Final\CustomComodelsConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CustomComodelsConfig_Form(object):
    def setupUi(self, CustomComodelsConfig_Form):
        CustomComodelsConfig_Form.setObjectName("CustomComodelsConfig_Form")
        CustomComodelsConfig_Form.resize(524, 418)
        CustomComodelsConfig_Form.setStyleSheet("/* QFrame */\n"
"QWidget {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(37, 40, 50);\n"
"}\n"
"/* Label */\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"font-size:22px;\n"
"font:normal;\n"
"}\n"
"QComboBox {\n"
"    background-color: rgb(52, 59, 72);\n"
"    border: 1px solid rgb(49, 54, 65);\n"
"    height: 30px;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"    padding-right: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font-size:22px;\n"
"    font:normal; \n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:rgb(27, 29, 35);\n"
"    border: 0px;\n"
"    color: #fff;\n"
"    selection-background-color: rgb(22, 51, 79);\n"
"    outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(22, 51, 79);\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: url(\":/icons/icons/cil-chevron-bottom.png\");\n"
"    width:15px;\n"
"    height:15px;\n"
"    margin-right:15px;\n"
"}\n"
"QComboBox:on {\n"
"    border: 0px solid rgb(61, 70, 86);\n"
"    background-color: rgb(57, 65, 80)\n"
"}\n"
"QComboBox QListView {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding: 10px;\n"
"}\n"
"QComboBox:disabled {\n"
"    background-color: #808080;\n"
"}\n"
"/* ToolButton */\n"
"QToolButton {\n"
"    border: 0px;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"/* Button */\n"
"QPushButton {\n"
"    border: 0px solid rgb(52, 59, 72);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    background-color:#1b1d23;\n"
"    color: rgb(255, 255, 255);\n"
"    margin:10px;\n"
"    padding:5px;\n"
"font:bold 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 5px solid transparent;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 7px solid transparent;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(102, 109, 122);\n"
"    color: rgb(168, 168, 168);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    color: white;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QGroupBox::title{\n"
"    color: rgb(255, 255, 255);\n"
"    margin-top: 10px;\n"
"    bottom: 20px;\n"
"}\n"
"QGroupBox{\n"
"    margin-top: 10px;\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    padding-top: 20px;\n"
"font:22px;\n"
"font:bold;\n"
"border-color:white;\n"
"}\n"
"\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CustomComodelsConfig_Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CustomComodConf_groupBox = QtWidgets.QGroupBox(CustomComodelsConfig_Form)
        self.CustomComodConf_groupBox.setObjectName("CustomComodConf_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.CustomComodConf_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.CustomComodelsAdd_Hlayout = QtWidgets.QHBoxLayout()
        self.CustomComodelsAdd_Hlayout.setContentsMargins(-1, 0, -1, 0)
        self.CustomComodelsAdd_Hlayout.setSpacing(0)
        self.CustomComodelsAdd_Hlayout.setObjectName("CustomComodelsAdd_Hlayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CustomComodelsAdd_Hlayout.addItem(spacerItem)
        self.CustomComodelsAdd_PushButton = QtWidgets.QPushButton(self.CustomComodConf_groupBox)
        self.CustomComodelsAdd_PushButton.setStyleSheet("    background-color:#1b1d23;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"")
        self.CustomComodelsAdd_PushButton.setObjectName("CustomComodelsAdd_PushButton")
        self.CustomComodelsAdd_Hlayout.addWidget(self.CustomComodelsAdd_PushButton)
        self.gridLayout.addLayout(self.CustomComodelsAdd_Hlayout, 0, 0, 1, 1)
        self.CustomConfig_InnergroupBox = QtWidgets.QGroupBox(self.CustomComodConf_groupBox)
        self.CustomConfig_InnergroupBox.setObjectName("CustomConfig_InnergroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CustomConfig_InnergroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HostName_Hlayout = QtWidgets.QHBoxLayout()
        self.HostName_Hlayout.setContentsMargins(-1, 5, -1, 5)
        self.HostName_Hlayout.setObjectName("HostName_Hlayout")
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HostName_Hlayout.addItem(spacerItem1)
        self.HostName_HSpacer_label = QtWidgets.QLabel(self.CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HostName_HSpacer_label.sizePolicy().hasHeightForWidth())
        self.HostName_HSpacer_label.setSizePolicy(sizePolicy)
        self.HostName_HSpacer_label.setStyleSheet("font-size:22px;\n"
"font:normal")
        self.HostName_HSpacer_label.setObjectName("HostName_HSpacer_label")
        self.HostName_Hlayout.addWidget(self.HostName_HSpacer_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HostName_Hlayout.addItem(spacerItem2)
        self.HostName_comboBox = QtWidgets.QComboBox(self.CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HostName_comboBox.sizePolicy().hasHeightForWidth())
        self.HostName_comboBox.setSizePolicy(sizePolicy)
        self.HostName_comboBox.setStyleSheet("background-color:#343b48;\n"
"font:normal;\n"
"font-size:22px;\n"
"border-radius:7px;")
        self.HostName_comboBox.setObjectName("HostName_comboBox")
        self.HostName_comboBox.addItem("")
        self.HostName_comboBox.addItem("")
        self.HostName_comboBox.addItem("")
        self.HostName_comboBox.addItem("")
        self.HostName_Hlayout.addWidget(self.HostName_comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HostName_Hlayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.HostName_Hlayout)
        self.DomainId_Hlayout = QtWidgets.QHBoxLayout()
        self.DomainId_Hlayout.setContentsMargins(-1, 5, -1, 5)
        self.DomainId_Hlayout.setObjectName("DomainId_Hlayout")
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DomainId_Hlayout.addItem(spacerItem4)
        self.DomainId_HSpacer_label = QtWidgets.QLabel(self.CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DomainId_HSpacer_label.sizePolicy().hasHeightForWidth())
        self.DomainId_HSpacer_label.setSizePolicy(sizePolicy)
        self.DomainId_HSpacer_label.setStyleSheet("font-size:22px;\n"
"font:normal")
        self.DomainId_HSpacer_label.setObjectName("DomainId_HSpacer_label")
        self.DomainId_Hlayout.addWidget(self.DomainId_HSpacer_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DomainId_Hlayout.addItem(spacerItem5)
        self.DomainId_comboBox = QtWidgets.QComboBox(self.CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DomainId_comboBox.sizePolicy().hasHeightForWidth())
        self.DomainId_comboBox.setSizePolicy(sizePolicy)
        self.DomainId_comboBox.setStyleSheet("background-color:#343b48;\n"
"font:normal;\n"
"font-size:22px;\n"
"border-radius:7px;")
        self.DomainId_comboBox.setObjectName("DomainId_comboBox")
        self.DomainId_comboBox.addItem("")
        self.DomainId_comboBox.addItem("")
        self.DomainId_comboBox.addItem("")
        self.DomainId_comboBox.addItem("")
        self.DomainId_Hlayout.addWidget(self.DomainId_comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DomainId_Hlayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.DomainId_Hlayout)
        self.gridLayout.addWidget(self.CustomConfig_InnergroupBox, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.CustomComodConf_groupBox)

        self.retranslateUi(CustomComodelsConfig_Form)
        QtCore.QMetaObject.connectSlotsByName(CustomComodelsConfig_Form)

    def retranslateUi(self, CustomComodelsConfig_Form):
        _translate = QtCore.QCoreApplication.translate
        CustomComodelsConfig_Form.setWindowTitle(_translate("CustomComodelsConfig_Form", "Form"))
        self.CustomComodConf_groupBox.setTitle(_translate("CustomComodelsConfig_Form", "Custom Comodels config"))
        self.CustomComodelsAdd_PushButton.setText(_translate("CustomComodelsConfig_Form", "+"))
        self.CustomConfig_InnergroupBox.setTitle(_translate("CustomComodelsConfig_Form", "Config 1"))
        self.HostName_HSpacer_label.setText(_translate("CustomComodelsConfig_Form", "Host Name"))
        self.HostName_comboBox.setItemText(0, _translate("CustomComodelsConfig_Form", "Auto"))
        self.HostName_comboBox.setItemText(1, _translate("CustomComodelsConfig_Form", "egc-med-bell"))
        self.HostName_comboBox.setItemText(2, _translate("CustomComodelsConfig_Form", "egc-med-baird"))
        self.HostName_comboBox.setItemText(3, _translate("CustomComodelsConfig_Form", "egc-med-nozark"))
        self.DomainId_HSpacer_label.setText(_translate("CustomComodelsConfig_Form", "Domain Id"))
        self.DomainId_comboBox.setItemText(0, _translate("CustomComodelsConfig_Form", "0"))
        self.DomainId_comboBox.setItemText(1, _translate("CustomComodelsConfig_Form", "1"))
        self.DomainId_comboBox.setItemText(2, _translate("CustomComodelsConfig_Form", "2"))
        self.DomainId_comboBox.setItemText(3, _translate("CustomComodelsConfig_Form", "3"))