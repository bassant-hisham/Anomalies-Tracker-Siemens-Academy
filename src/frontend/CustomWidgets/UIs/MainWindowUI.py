# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 858)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(44, 49, 59);\n"
"    color: white;\n"
"}\n"
"\n"
"#MainWindow, #scrollAreaWidgetContents{\n"
"    background-color: rgb(44, 49, 59);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/* QFrame */\n"
"QFrame {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(37, 40, 50);\n"
"}\n"
"/* Label */\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
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
"    margin-top: 10px;\n"
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
"QTableWidget {\n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"    gridline-color: rgb(49, 54, 65);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"    background-color: rgb(44, 49, 59);\n"
"}\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    color: white;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"/* Tab */\n"
"QTabBar::tab{\n"
"    height:35px;\n"
"}\n"
"QTabWidget::pane {\n"
"     border: 0px solid rgb(39, 44, 54);\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:selected{\n"
"    background-color:rgb(39, 44, 54);\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:!selected{\n"
"    background-color: rgb(30, 35, 45);\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:!selected:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"/* Splitter */\n"
"QSplitter::handle{\n"
"    background-color: gray;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Sol_Plat_gridLayout = QtWidgets.QGridLayout()
        self.Sol_Plat_gridLayout.setObjectName("Sol_Plat_gridLayout")
        self.Sol_Plat_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sol_Plat_frame.sizePolicy().hasHeightForWidth())
        self.Sol_Plat_frame.setSizePolicy(sizePolicy)
        self.Sol_Plat_frame.setMaximumSize(QtCore.QSize(16777215, 134))
        self.Sol_Plat_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Sol_Plat_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Sol_Plat_frame.setObjectName("Sol_Plat_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Sol_Plat_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Sol_Plat_formLayout = QtWidgets.QFormLayout()
        self.Sol_Plat_formLayout.setObjectName("Sol_Plat_formLayout")
        self.Platform_label = QtWidgets.QLabel(self.Sol_Plat_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Platform_label.sizePolicy().hasHeightForWidth())
        self.Platform_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Platform_label.setFont(font)
        self.Platform_label.setLineWidth(0)
        self.Platform_label.setObjectName("Platform_label")
        self.Sol_Plat_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Platform_label)
        self.Platfrom_comboBox = QtWidgets.QComboBox(self.Sol_Plat_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Platfrom_comboBox.setFont(font)
        self.Platfrom_comboBox.setObjectName("Platfrom_comboBox")
        self.Platfrom_comboBox.addItem("")
        self.Platfrom_comboBox.addItem("")
        self.Sol_Plat_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Platfrom_comboBox)
        self.Solution_label = QtWidgets.QLabel(self.Sol_Plat_frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Solution_label.setFont(font)
        self.Solution_label.setObjectName("Solution_label")
        self.Sol_Plat_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Solution_label)
        self.Solution_comboBox = QtWidgets.QComboBox(self.Sol_Plat_frame)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Solution_comboBox.setFont(font)
        self.Solution_comboBox.setStyleSheet("")
        self.Solution_comboBox.setObjectName("Solution_comboBox")
        self.Solution_comboBox.addItem("")
        self.Solution_comboBox.addItem("")
        self.Solution_comboBox.addItem("")
        self.Sol_Plat_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Solution_comboBox)
        self.gridLayout_4.addLayout(self.Sol_Plat_formLayout, 0, 0, 1, 1)
        self.Sol_Plat_gridLayout.addWidget(self.Sol_Plat_frame, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(548, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Sol_Plat_gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.CreateTask_button = QtWidgets.QPushButton(self.centralwidget)
        self.CreateTask_button.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CreateTask_button.setFont(font)
        self.CreateTask_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 188, 180);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 195, 195);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(25, 154, 147);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.CreateTask_button.setObjectName("CreateTask_button")
        self.Sol_Plat_gridLayout.addWidget(self.CreateTask_button, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.Sol_Plat_gridLayout, 0, 0, 1, 1)
        self.Tasks = QtWidgets.QTabWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Tasks.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Tasks.setFont(font)
        self.Tasks.setStyleSheet("\n"
"QTabWidget::pane{\n"
"border-color:none;\n"
"}\n"
"QTabWidget:tab-bar {\n"
"border-color:none;\n"
"}\n"
"QTabBar:tab:selected{\n"
"background-color:#282c37;\n"
"color:white;\n"
"}\n"
"QTabBar:tab:!selected{\n"
"background-color:#1b1d22;\n"
"color:white;\n"
"}\n"
"")
        self.Tasks.setObjectName("Tasks")
        self.gridLayout_2.addWidget(self.Tasks, 1, 0, 1, 1)
        self.CreateJobs_horizontalLayout = QtWidgets.QHBoxLayout()
        self.CreateJobs_horizontalLayout.setObjectName("CreateJobs_horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CreateJobs_horizontalLayout.addItem(spacerItem1)
        self.CreateJobs_button = QtWidgets.QPushButton(self.centralwidget)
        self.CreateJobs_button.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CreateJobs_button.setFont(font)
        self.CreateJobs_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 188, 180);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 195, 195);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(25, 154, 147);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.CreateJobs_button.setObjectName("CreateJobs_button")
        self.CreateJobs_horizontalLayout.addWidget(self.CreateJobs_button)
        self.gridLayout_2.addLayout(self.CreateJobs_horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tasks.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anomalies Tracker Home"))
        self.Platform_label.setText(_translate("MainWindow", "Platform"))
        self.Platfrom_comboBox.setItemText(0, _translate("MainWindow", "Veloce"))
        self.Platfrom_comboBox.setItemText(1, _translate("MainWindow", "VPS"))
        self.Solution_label.setText(_translate("MainWindow", "Solution"))
        self.Solution_comboBox.setItemText(0, _translate("MainWindow", "Ethernet"))
        self.Solution_comboBox.setItemText(1, _translate("MainWindow", "5G"))
        self.Solution_comboBox.setItemText(2, _translate("MainWindow", "OTN"))
        self.CreateTask_button.setText(_translate("MainWindow", "Create Task"))
        self.CreateJobs_button.setText(_translate("MainWindow", "Create Jobs"))
