# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaunchingConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_launching_config(object):
    def setupUi(self, launching_config):
        launching_config.setObjectName("launching_config")
        launching_config.resize(844, 803)
        launching_config.setStyleSheet("/* QFrame */\n"
"QWidget {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(37, 40, 50);\n"
"}\n"
"/* Label */\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"font-size:22px;\n"
"font:normal;\n"
"\n"
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
"/* ComboBox */\n"
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
"/* QGroupBox  */\n"
"QGroupBox::title{\n"
"    color: rgb(255, 255, 255);\n"
"    margin-top: 10px;\n"
"    bottom: 20px;\n"
"}\n"
"QGroupBox{\n"
"    margin-top: 40px;\n"
"margin-left:20px;\n"
"    margin-bottom: 40px;\n"
"margin-right:20px;\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    padding-top: 20px;\n"
"}\n"
"/* LineEdit */\n"
"QLineEdit{\n"
"    border: 0px solid rgb(37, 39, 48);\n"
"    height: 30px;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(27, 29, 35);\n"
"    font-size:20px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(64, 71, 88)\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid rgb(91, 101, 124);\n"
"    color: white;\n"
"}\n"
"QLineEdit:disabled {\n"
"    background-color: #808080;\n"
"}\n"
"/* Table */\n"
"QFrame QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QFrame QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
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
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    color: white;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"/* Splitter */\n"
"QSplitter::handle{\n"
"    background-color: gray;\n"
"border-radius:7px;\n"
"font:normal;\n"
"font-size:22px;\n"
"padding-left:8px\n"
"}\n"
"QGroupBox\n"
"{\n"
"font:22px;\n"
"font:bold;\n"
"border-color:white;\n"
"}\n"
"QCheckBox\n"
"{\n"
"    font-size:22px;\n"
"    font:normal; \n"
"}\n"
"QSpinBox\n"
"{\n"
"\n"
"background-color:#1b1d23;\n"
"border-radius:7px;\n"
"font:normal;\n"
"font-size:22px;\n"
"padding-left:8px\n"
"}\n"
"QTextBrowser{\n"
"border:1px solid white;\n"
"\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(launching_config)
        self.gridLayout.setObjectName("gridLayout")
        self.lanch_conf_scrollArea = QtWidgets.QScrollArea(launching_config)
        self.lanch_conf_scrollArea.setStyleSheet("color:white;\n"
"background-color:#2c313b;\n"
"")
        self.lanch_conf_scrollArea.setWidgetResizable(True)
        self.lanch_conf_scrollArea.setObjectName("lanch_conf_scrollArea")
        self.lanch_conf_Hlayout = QtWidgets.QWidget()
        self.lanch_conf_Hlayout.setGeometry(QtCore.QRect(0, -494, 808, 1275))
        self.lanch_conf_Hlayout.setObjectName("lanch_conf_Hlayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lanch_conf_Hlayout)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lanch_conf_VLayout = QtWidgets.QVBoxLayout()
        self.lanch_conf_VLayout.setContentsMargins(-1, 5, -1, -1)
        self.lanch_conf_VLayout.setObjectName("lanch_conf_VLayout")
        self.Title_HLayout = QtWidgets.QHBoxLayout()
        self.Title_HLayout.setContentsMargins(-1, -1, -1, 6)
        self.Title_HLayout.setSpacing(0)
        self.Title_HLayout.setObjectName("Title_HLayout")
        self.Title = QtWidgets.QLabel(self.lanch_conf_Hlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setStyleSheet("background-color:none;\n"
"font-size:26px;\n"
"font:bold;\n"
"border-radius:10px;\n"
"")
        self.Title.setObjectName("Title")
        self.Title_HLayout.addWidget(self.Title)
        spacerItem = QtWidgets.QSpacerItem(420, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Title_HLayout.addItem(spacerItem)
        self.lanch_conf_VLayout.addLayout(self.Title_HLayout)
        self.ToolConfigGroupBox = QtWidgets.QGroupBox(self.lanch_conf_Hlayout)
        self.ToolConfigGroupBox.setStyleSheet("QPushButton {\n"
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
"}")
        self.ToolConfigGroupBox.setObjectName("ToolConfigGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ToolConfigGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LaunchToolCheckBox = QtWidgets.QCheckBox(self.ToolConfigGroupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LaunchToolCheckBox.setFont(font)
        self.LaunchToolCheckBox.setObjectName("LaunchToolCheckBox")
        self.gridLayout_4.addWidget(self.LaunchToolCheckBox, 0, 0, 1, 1)
        self.MasterToolGroupBox = QtWidgets.QGroupBox(self.ToolConfigGroupBox)
        self.MasterToolGroupBox.setStyleSheet("")
        self.MasterToolGroupBox.setObjectName("MasterToolGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MasterToolGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TerminateOnErr_checkBox = QtWidgets.QCheckBox(self.MasterToolGroupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TerminateOnErr_checkBox.setFont(font)
        self.TerminateOnErr_checkBox.setObjectName("TerminateOnErr_checkBox")
        self.gridLayout_2.addWidget(self.TerminateOnErr_checkBox, 2, 0, 1, 1)
        self.AdditionalArg_groupBox = QtWidgets.QGroupBox(self.MasterToolGroupBox)
        self.AdditionalArg_groupBox.setObjectName("AdditionalArg_groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.AdditionalArg_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ToolAdditionalEnvValues = QtWidgets.QTextBrowser(self.AdditionalArg_groupBox)
        self.ToolAdditionalEnvValues.setStyleSheet("border:none;\n"
"")
        self.ToolAdditionalEnvValues.setObjectName("ToolAdditionalEnvValues")
        self.gridLayout_5.addWidget(self.ToolAdditionalEnvValues, 5, 0, 1, 1)
        self.EnvVarName_Hlayout = QtWidgets.QHBoxLayout()
        self.EnvVarName_Hlayout.setObjectName("EnvVarName_Hlayout")
        self.EnvVarName_label = QtWidgets.QLabel(self.AdditionalArg_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnvVarName_label.sizePolicy().hasHeightForWidth())
        self.EnvVarName_label.setSizePolicy(sizePolicy)
        self.EnvVarName_label.setObjectName("EnvVarName_label")
        self.EnvVarName_Hlayout.addWidget(self.EnvVarName_label)
        self.EnvVarName_HSpacer_mid_lineEdit = QtWidgets.QLineEdit(self.AdditionalArg_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnvVarName_HSpacer_mid_lineEdit.sizePolicy().hasHeightForWidth())
        self.EnvVarName_HSpacer_mid_lineEdit.setSizePolicy(sizePolicy)
        self.EnvVarName_HSpacer_mid_lineEdit.setStyleSheet("background-color: #1b1d23;\n"
"")
        self.EnvVarName_HSpacer_mid_lineEdit.setObjectName("EnvVarName_HSpacer_mid_lineEdit")
        self.EnvVarName_Hlayout.addWidget(self.EnvVarName_HSpacer_mid_lineEdit)
        self.gridLayout_5.addLayout(self.EnvVarName_Hlayout, 1, 0, 1, 2)
        self.EnvVarValue_Hlayout = QtWidgets.QHBoxLayout()
        self.EnvVarValue_Hlayout.setObjectName("EnvVarValue_Hlayout")
        self.EnvVarValue_label = QtWidgets.QLabel(self.AdditionalArg_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnvVarValue_label.sizePolicy().hasHeightForWidth())
        self.EnvVarValue_label.setSizePolicy(sizePolicy)
        self.EnvVarValue_label.setObjectName("EnvVarValue_label")
        self.EnvVarValue_Hlayout.addWidget(self.EnvVarValue_label)
        self.EnvVarValue_lineEdit = QtWidgets.QLineEdit(self.AdditionalArg_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnvVarValue_lineEdit.sizePolicy().hasHeightForWidth())
        self.EnvVarValue_lineEdit.setSizePolicy(sizePolicy)
        self.EnvVarValue_lineEdit.setStyleSheet("background-color: #1b1d23;\n"
"")
        self.EnvVarValue_lineEdit.setObjectName("EnvVarValue_lineEdit")
        self.EnvVarValue_Hlayout.addWidget(self.EnvVarValue_lineEdit)
        self.gridLayout_5.addLayout(self.EnvVarValue_Hlayout, 3, 0, 1, 2)
        self.AddEnvLayout = QtWidgets.QHBoxLayout()
        self.AddEnvLayout.setObjectName("AddEnvLayout")
        spacerItem1 = QtWidgets.QSpacerItem(528, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.AddEnvLayout.addItem(spacerItem1)
        self.AddEnv = QtWidgets.QPushButton(self.AdditionalArg_groupBox)
        self.AddEnv.setMinimumSize(QtCore.QSize(111, 54))
        self.AddEnv.setObjectName("AddEnv")
        self.AddEnvLayout.addWidget(self.AddEnv)
        self.gridLayout_5.addLayout(self.AddEnvLayout, 6, 0, 1, 1)
        self.gridLayout_2.addWidget(self.AdditionalArg_groupBox, 5, 0, 3, 2)
        self.ToolLaunch_Hlayout = QtWidgets.QHBoxLayout()
        self.ToolLaunch_Hlayout.setContentsMargins(-1, 5, -1, 5)
        self.ToolLaunch_Hlayout.setObjectName("ToolLaunch_Hlayout")
        self.ToolLaunch_label = QtWidgets.QLabel(self.MasterToolGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolLaunch_label.sizePolicy().hasHeightForWidth())
        self.ToolLaunch_label.setSizePolicy(sizePolicy)
        self.ToolLaunch_label.setStyleSheet("font-size:22px;\n"
"font:normal")
        self.ToolLaunch_label.setObjectName("ToolLaunch_label")
        self.ToolLaunch_Hlayout.addWidget(self.ToolLaunch_label)
        self.ToolLaunch_comboBox = QtWidgets.QComboBox(self.MasterToolGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(56)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.ToolLaunch_comboBox.sizePolicy().hasHeightForWidth())
        self.ToolLaunch_comboBox.setSizePolicy(sizePolicy)
        self.ToolLaunch_comboBox.setAutoFillBackground(False)
        self.ToolLaunch_comboBox.setStyleSheet("background-color:#343b48;\n"
"font:normal;\n"
"font-size:22px;\n"
"border-radius:7px;")
        self.ToolLaunch_comboBox.setObjectName("ToolLaunch_comboBox")
        self.ToolLaunch_comboBox.addItem("")
        self.ToolLaunch_comboBox.addItem("")
        self.ToolLaunch_comboBox.addItem("")
        self.ToolLaunch_Hlayout.addWidget(self.ToolLaunch_comboBox)
        self.gridLayout_2.addLayout(self.ToolLaunch_Hlayout, 1, 0, 1, 2)
        self.ToolName_Hlayout = QtWidgets.QHBoxLayout()
        self.ToolName_Hlayout.setContentsMargins(-1, 5, -1, 5)
        self.ToolName_Hlayout.setObjectName("ToolName_Hlayout")
        self.ToolName_label = QtWidgets.QLabel(self.MasterToolGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolName_label.sizePolicy().hasHeightForWidth())
        self.ToolName_label.setSizePolicy(sizePolicy)
        self.ToolName_label.setStyleSheet("font-size:22px;\n"
"font:normal")
        self.ToolName_label.setObjectName("ToolName_label")
        self.ToolName_Hlayout.addWidget(self.ToolName_label)
        self.ToolName_comboBox = QtWidgets.QComboBox(self.MasterToolGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(56)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.ToolName_comboBox.sizePolicy().hasHeightForWidth())
        self.ToolName_comboBox.setSizePolicy(sizePolicy)
        self.ToolName_comboBox.setAutoFillBackground(False)
        self.ToolName_comboBox.setStyleSheet("background-color:#343b48;\n"
"font:normal;\n"
"font-size:22px;\n"
"border-radius:7px;")
        self.ToolName_comboBox.setObjectName("ToolName_comboBox")
        self.ToolName_comboBox.addItem("")
        self.ToolName_comboBox.addItem("")
        self.ToolName_Hlayout.addWidget(self.ToolName_comboBox)
        self.gridLayout_2.addLayout(self.ToolName_Hlayout, 0, 0, 1, 2)
        self.AdditionalArgGroupBox = QtWidgets.QGroupBox(self.MasterToolGroupBox)
        self.AdditionalArgGroupBox.setObjectName("AdditionalArgGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.AdditionalArgGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ArgName_Hlayout = QtWidgets.QHBoxLayout()
        self.ArgName_Hlayout.setObjectName("ArgName_Hlayout")
        self.ArgName_label = QtWidgets.QLabel(self.AdditionalArgGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArgName_label.sizePolicy().hasHeightForWidth())
        self.ArgName_label.setSizePolicy(sizePolicy)
        self.ArgName_label.setObjectName("ArgName_label")
        self.ArgName_Hlayout.addWidget(self.ArgName_label)
        self.ArgName_HSpacer_mid_lineEdit = QtWidgets.QLineEdit(self.AdditionalArgGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArgName_HSpacer_mid_lineEdit.sizePolicy().hasHeightForWidth())
        self.ArgName_HSpacer_mid_lineEdit.setSizePolicy(sizePolicy)
        self.ArgName_HSpacer_mid_lineEdit.setStyleSheet("background-color: #1b1d23;\n"
"")
        self.ArgName_HSpacer_mid_lineEdit.setObjectName("ArgName_HSpacer_mid_lineEdit")
        self.ArgName_Hlayout.addWidget(self.ArgName_HSpacer_mid_lineEdit)
        self.gridLayout_3.addLayout(self.ArgName_Hlayout, 1, 0, 1, 1)
        self.AddArgLayout = QtWidgets.QHBoxLayout()
        self.AddArgLayout.setObjectName("AddArgLayout")
        spacerItem2 = QtWidgets.QSpacerItem(528, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.AddArgLayout.addItem(spacerItem2)
        self.AddArgButton = QtWidgets.QPushButton(self.AdditionalArgGroupBox)
        self.AddArgButton.setMinimumSize(QtCore.QSize(111, 54))
        self.AddArgButton.setObjectName("AddArgButton")
        self.AddArgLayout.addWidget(self.AddArgButton)
        self.gridLayout_3.addLayout(self.AddArgLayout, 4, 0, 1, 1)
        self.AdditionalArg = QtWidgets.QTextBrowser(self.AdditionalArgGroupBox)
        self.AdditionalArg.setStyleSheet("border:none;\n"
"")
        self.AdditionalArg.setObjectName("AdditionalArg")
        self.gridLayout_3.addWidget(self.AdditionalArg, 3, 0, 1, 1)
        self.ArgValue_Hlayout = QtWidgets.QHBoxLayout()
        self.ArgValue_Hlayout.setObjectName("ArgValue_Hlayout")
        self.ArgValue_label = QtWidgets.QLabel(self.AdditionalArgGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArgValue_label.sizePolicy().hasHeightForWidth())
        self.ArgValue_label.setSizePolicy(sizePolicy)
        self.ArgValue_label.setObjectName("ArgValue_label")
        self.ArgValue_Hlayout.addWidget(self.ArgValue_label)
        self.ArgValue_lineEdit = QtWidgets.QLineEdit(self.AdditionalArgGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArgValue_lineEdit.sizePolicy().hasHeightForWidth())
        self.ArgValue_lineEdit.setSizePolicy(sizePolicy)
        self.ArgValue_lineEdit.setStyleSheet("background-color: #1b1d23;\n"
"")
        self.ArgValue_lineEdit.setObjectName("ArgValue_lineEdit")
        self.ArgValue_Hlayout.addWidget(self.ArgValue_lineEdit)
        self.gridLayout_3.addLayout(self.ArgValue_Hlayout, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.AdditionalArgGroupBox, 4, 0, 1, 2)
        self.TerminateTool_checkBox = QtWidgets.QCheckBox(self.MasterToolGroupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TerminateTool_checkBox.setFont(font)
        self.TerminateTool_checkBox.setObjectName("TerminateTool_checkBox")
        self.gridLayout_2.addWidget(self.TerminateTool_checkBox, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.MasterToolGroupBox, 1, 0, 1, 1)
        self.lanch_conf_VLayout.addWidget(self.ToolConfigGroupBox)
        self.Add_Hlayout = QtWidgets.QHBoxLayout()
        self.Add_Hlayout.setSpacing(1)
        self.Add_Hlayout.setObjectName("Add_Hlayout")
        spacerItem3 = QtWidgets.QSpacerItem(652, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Add_Hlayout.addItem(spacerItem3)
        self.Add_PushButton = QtWidgets.QPushButton(self.lanch_conf_Hlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add_PushButton.sizePolicy().hasHeightForWidth())
        self.Add_PushButton.setSizePolicy(sizePolicy)
        self.Add_PushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Add_PushButton.setStyleSheet("    background-color:#1b1d23;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"")
        self.Add_PushButton.setObjectName("Add_PushButton")
        self.Add_Hlayout.addWidget(self.Add_PushButton)
        self.lanch_conf_VLayout.addLayout(self.Add_Hlayout)
        self.verticalLayout_3.addLayout(self.lanch_conf_VLayout)
        self.lanch_conf_scrollArea.setWidget(self.lanch_conf_Hlayout)
        self.gridLayout.addWidget(self.lanch_conf_scrollArea, 0, 1, 1, 1)

        self.retranslateUi(launching_config)
        QtCore.QMetaObject.connectSlotsByName(launching_config)

    def retranslateUi(self, launching_config):
        _translate = QtCore.QCoreApplication.translate
        launching_config.setWindowTitle(_translate("launching_config", "Form"))
        self.Title.setText(_translate("launching_config", "Launching Configurations :"))
        self.ToolConfigGroupBox.setTitle(_translate("launching_config", "Tools Configuration"))
        self.LaunchToolCheckBox.setText(_translate("launching_config", "Launch Tool"))
        self.MasterToolGroupBox.setTitle(_translate("launching_config", "Master Tool Configuration"))
        self.TerminateOnErr_checkBox.setText(_translate("launching_config", "Terminate Tool"))
        self.AdditionalArg_groupBox.setTitle(_translate("launching_config", "Tools Additional Env Variables"))
        self.EnvVarName_label.setText(_translate("launching_config", "Variable Key"))
        self.EnvVarValue_label.setText(_translate("launching_config", "Variable Value"))
        self.AddEnv.setText(_translate("launching_config", "Add"))
        self.ToolLaunch_label.setText(_translate("launching_config", "Tool Launch Mode"))
        self.ToolLaunch_comboBox.setItemText(0, _translate("launching_config", "Normal"))
        self.ToolLaunch_comboBox.setItemText(1, _translate("launching_config", "GDB_Catch"))
        self.ToolLaunch_comboBox.setItemText(2, _translate("launching_config", "GDB_Run"))
        self.ToolName_label.setText(_translate("launching_config", "Tool Name"))
        self.ToolName_comboBox.setItemText(0, _translate("launching_config", "EPGM"))
        self.ToolName_comboBox.setItemText(1, _translate("launching_config", "Controller"))
        self.AdditionalArgGroupBox.setTitle(_translate("launching_config", "Additional Arguments"))
        self.ArgName_label.setText(_translate("launching_config", "Argument Key"))
        self.AddArgButton.setText(_translate("launching_config", "Add"))
        self.ArgValue_label.setText(_translate("launching_config", "Argument Value"))
        self.TerminateTool_checkBox.setText(_translate("launching_config", "Terminate Tool on Error"))
        self.Add_PushButton.setText(_translate("launching_config", "+"))
