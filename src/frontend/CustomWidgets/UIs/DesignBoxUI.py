# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Siemens diploma\Anomalies-Tracker-Siemens-Academy\src\frontend\UiFiles\NewDesignBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DesignBoxWidget(object):
    def setupUi(self, DesignBoxWidget):
        DesignBoxWidget.setObjectName("DesignBoxWidget")
        DesignBoxWidget.resize(655, 308)
        DesignBoxWidget.setStyleSheet("QWidget{\n"
"    border-radius: 15px;\n"
"    background-color: rgb(37, 40, 50);\n"
"}\n"
"QGroupBox{\n"
"background-color:rgb(37, 40, 50);\n"
"color:white;\n"
"font-size:16px;\n"
"border:1px solid white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"\n"
"}\n"
"QLineEdit{\n"
"    border: 0px solid rgb(37, 39, 48);\n"
"    height: 30px;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(27, 29, 35);\n"
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
"QPushButton{\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton {\n"
"    border: 0px solid rgb(52, 59, 72);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    margin-right:10px;\n"
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
"QGroupBox::title\n"
"{\n"
"font-size:220;\n"
"}\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DesignBoxWidget)
        self.verticalLayout_2.setContentsMargins(9, -1, 6, 10)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DesignBox = QtWidgets.QGroupBox(DesignBoxWidget)
        self.DesignBox.setStyleSheet("QWidget{\n"
"    border-radius: 15px;\n"
"    background-color: rgb(37, 40, 50);\n"
"}\n"
"QCheckBox{\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 11pt;\n"
"}\n"
"QComboBox {\n"
"    background-color: rgb(52, 59, 72);\n"
"    border: 1px solid rgb(49, 54, 65);\n"
"    height: 30px;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"    padding-right: 15px;\n"
"    color: rgb(255, 255, 255);\n"
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
"/* Label */\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 11pt;\n"
"\n"
"}\n"
"QLineEdit{\n"
"    border: 0px solid rgb(37, 39, 48);\n"
"    height: 30px;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(27, 29, 35);\n"
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
"/* QGroupBox  */\n"
"QGroupBox{\n"
"    margin-top: 10px;\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    padding-top: 20px;\n"
"}\n"
"QGroupBox::title{\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 12pt;\n"
"    margin-top: 10px;\n"
"    bottom: 20px;\n"
"    font-style:bold;\n"
"\n"
"}\n"
"/* Button */\n"
"QPushButton {\n"
"    border: 0px solid rgb(52, 59, 72);\n"
"    background-color: rgb(52, 59, 72);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    margin-right:10px;\n"
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
"")
        self.DesignBox.setFlat(True)
        self.DesignBox.setObjectName("DesignBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DesignBox)
        self.verticalLayout.setContentsMargins(-1, 5, 9, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 8)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.delete_pushButton = QtWidgets.QPushButton(self.DesignBox)
        self.delete_pushButton.setStyleSheet("background:none;\n"
"")
        self.delete_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/frontend/IconsImages/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_pushButton.setIcon(icon)
        self.delete_pushButton.setIconSize(QtCore.QSize(35, 25))
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.horizontalLayout.addWidget(self.delete_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        
        
        
        self.DesignPath_horizontalLayout = QtWidgets.QHBoxLayout()
        self.DesignPath_horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.DesignPath_horizontalLayout.setObjectName("DesignPath_horizontalLayout")
        self.DesignPath_label = QtWidgets.QLabel(self.DesignBox)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.DesignPath_label.setFont(font)
        self.DesignPath_label.setLineWidth(0)
        self.DesignPath_label.setObjectName("DesignPath_label")
        self.DesignPath_horizontalLayout.addWidget(self.DesignPath_label)
        self.DesignPath_lineEdit = QtWidgets.QLineEdit(self.DesignBox)
        self.DesignPath_lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.DesignPath_lineEdit.setStyleSheet("")
        self.DesignPath_lineEdit.setObjectName("DesignPath_lineEdit")
        self.DesignPath_horizontalLayout.addWidget(self.DesignPath_lineEdit)
        self.BrowseDesignPath_button = QtWidgets.QToolButton(self.DesignBox)
        self.BrowseDesignPath_button.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/folder_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BrowseDesignPath_button.setIcon(icon1)
        self.BrowseDesignPath_button.setObjectName("BrowseDesignPath_button")
        self.DesignPath_horizontalLayout.addWidget(self.BrowseDesignPath_button)
        self.verticalLayout.addLayout(self.DesignPath_horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(10, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.Configurations_horizontalLayout = QtWidgets.QHBoxLayout()
        self.Configurations_horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Configurations_horizontalLayout.setObjectName("Configurations_horizontalLayout")        
        
        self.Compilation_Config_Layout = QtWidgets.QHBoxLayout()
        self.Compilation_Config_Layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Compilation_Config_Layout.setObjectName("horizontalLayout")
        
        self.CompileDesign_checkBox = QtWidgets.QCheckBox(self.DesignBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.CompileDesign_checkBox.setFont(font)
        self.CompileDesign_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CompileDesign_checkBox.setObjectName("CompileDesign_checkBox")
        self.Compilation_Config_Layout.addWidget(self.CompileDesign_checkBox) 
        
        self.CompilationConfig_button = QtWidgets.QPushButton(self.DesignBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompilationConfig_button.sizePolicy().hasHeightForWidth())
        self.CompilationConfig_button.setSizePolicy(sizePolicy)
        self.CompilationConfig_button.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.CompilationConfig_button.setFont(font)
        self.CompilationConfig_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CompilationConfig_button.setStyleSheet("")
        self.CompilationConfig_button.setObjectName("CompilationConfig_button")
        self.Compilation_Config_Layout.addWidget(self.CompilationConfig_button)
        
        self.verticalLayout.addLayout(self.Compilation_Config_Layout)
        
        self.Dutconfig_Vlayout = QtWidgets.QVBoxLayout()
        self.Dutconfig_Vlayout.setObjectName("Dutconfig_Vlayout")
        
        
        
# Launching Configuration Layout UI element
        
        self.launch_dpi_configuration = QtWidgets.QHBoxLayout()
        self.launch_dpi_configuration.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.launch_dpi_configuration.setObjectName("horizontalLayout")
   
        
# Launching DPI Checkbox UI element

        self.LaunchDpi_checkBox = QtWidgets.QCheckBox(self.DesignBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.LaunchDpi_checkBox.setFont(font)
        self.LaunchDpi_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LaunchDpi_checkBox.setObjectName("LaunchDpi_checkBox")
        self.launch_dpi_configuration.addWidget(self.LaunchDpi_checkBox) 
        
        
# Launching DPI Button UI element

        self.LaunchDpi_button = QtWidgets.QPushButton(self.DesignBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LaunchDpi_button.sizePolicy().hasHeightForWidth())
        self.LaunchDpi_button.setSizePolicy(sizePolicy)
        self.LaunchDpi_button.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.LaunchDpi_button.setFont(font)
        self.LaunchDpi_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LaunchDpi_button.setStyleSheet("")
        self.LaunchDpi_button.setObjectName("LaunchDpi_button")
        self.launch_dpi_configuration.addWidget(self.LaunchDpi_button)
        self.verticalLayout.addLayout(self.launch_dpi_configuration)
        
        

        
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.DesignBox)

        self.retranslateUi(DesignBoxWidget)
        QtCore.QMetaObject.connectSlotsByName(DesignBoxWidget)

    def retranslateUi(self, DesignBoxWidget):
        _translate = QtCore.QCoreApplication.translate
        DesignBoxWidget.setWindowTitle(_translate("DesignBoxWidget", "Form"))
        self.DesignBox.setTitle(_translate("DesignBoxWidget", "Design"))
        self.DesignPath_label.setText(_translate("DesignBoxWidget", "Design Path"))
        self.BrowseDesignPath_button.setText(_translate("DesignBoxWidget", "..."))
        self.CompileDesign_checkBox.setText(_translate("DesignBoxWidget", "Compile Design"))
        self.CompilationConfig_button.setText(_translate("DesignBoxWidget", "Compilation Configuration"))
        self.LaunchDpi_checkBox.setText(_translate("DesignBoxWidget", "Launch DPI"))
        self.LaunchDpi_button.setText(_translate("DesignBoxWidget", "DPI Configuration"))
