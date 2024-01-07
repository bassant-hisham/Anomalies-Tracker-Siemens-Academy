# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowOEEtqr.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 588)
        icon = QIcon()
        icon.addFile(u":/icons/icons/design_creator_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(44, 49, 59);\n"
"	color: white;\n"
"}\n"
"/* MessageBox */\n"
"QMessageBox {\n"
"    background-color: rgb(44, 49, 59);\n"
"}\n"
"QMessageBox QFrame {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QMessageBox QLabel {\n"
"    color: white;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QMessageBox QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    background-color: rgb(33, 188, 180);\n"
"    color: rgb(223, 223, 223);\n"
"    min-width: 80px;\n"
"	min-height: 35px;\n"
"    border-radius: 15px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"QMessageBox QPushButton:hover {\n"
"    background-color: rgb(84, 195, 195);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QMessageBox QPushButton:pressed {\n"
"    background-color: rgb(25, 154, 147);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"#MainWindow, #scrollAreaWidgetContents{\n"
"	background-color: rgb(44, 49, 59);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(MainWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setSizeIncrement(QSize(0, 200))
        self.centralWidget.setBaseSize(QSize(0, 200))
        self.centralWidget.setStyleSheet(u"/* QFrame */\n"
"QFrame {\n"
"	border-radius: 15px;\n"
"	background-color: rgb(37, 40, 50);\n"
"}\n"
"/* Label */\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* ToolButton */\n"
"QToolButton {\n"
"	border: 0px;\n"
"	width: 28px;\n"
"	height: 28px;\n"
"	background-color: transparent;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QToolButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"/* Button */\n"
"QPushButton {\n"
"	border: 0px solid rgb(52, 59, 72);\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	margin-right:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 5px solid transparent;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 7px solid transparent;\n"
"}\n"
"QPushButton:disabled {\n"
""
                        "	background-color: rgb(102, 109, 122);\n"
"	color: rgb(168, 168, 168);\n"
"}\n"
"/* ComboBox */\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	height: 14px;\n"
"	margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QFrame QScrollBar:vertical {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	width: 14px;\n"
"	margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(85, 170, 255);\n"
"	min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	subcontrol-position: left;\n"
"	subcon"
                        "trol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"	background: none;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(85, 170, 255);\n"
"	min-height: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
                        "\n"
"	background: none;\n"
"}\n"
"QComboBox {\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 1px solid rgb(49, 54, 65);\n"
"	height: 30px;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:rgb(27, 29, 35);\n"
"	border: 0px;\n"
"	color: #fff;\n"
"    selection-background-color: rgb(22, 51, 79);\n"
"    outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(22, 51, 79);\n"
"}\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"	image: url(\":/icons/icons/cil-chevron-bottom.png\");\n"
"	width:15px;\n"
"	height:15px;\n"
"	margin-right:15px;\n"
"}\n"
"QComboBox:on {\n"
"	border: 0px solid rgb(61, 70, 86);\n"
"	background-color: rgb(57, 65, 80)\n"
"}\n"
"QComboBox QListView {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding: 10px;\n"
"}\n"
"QComboBox:disabled {\n"
"	b"
                        "ackground-color: #808080;\n"
"}\n"
"/* QGroupBox  */\n"
"QGroupBox::title{\n"
"	color: rgb(255, 255, 255);\n"
"	margin-top: 10px;\n"
"	bottom: 20px;\n"
"}\n"
"QGroupBox{\n"
"	margin-top: 10px;\n"
"	background-color: transparent;\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"	padding-top: 20px;\n"
"}\n"
"/* LineEdit */\n"
"QLineEdit{\n"
"	border: 0px solid rgb(37, 39, 48);\n"
"	height: 30px;\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88)\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 3px solid rgb(91, 101, 124);\n"
"	color: white;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: #808080;\n"
"}\n"
"/* Table */\n"
"QFrame QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QFrame QScrollBar:vertical {\n"
"	border: none;\n"
"    background:"
                        " rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
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
" QScrollBar::handle:vertica"
                        "l {\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
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
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"	gridline-color: rgb(49, 54, 65);\n"
"}\n"
"QTableWidget::item:selec"
                        "ted{\n"
"	background-color: rgb(85, 170, 255);\n"
"	background-color: rgb(44, 49, 59);\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	color: white;\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"/* Tab */\n"
"QTabBar::tab{\n"
"	height:35px;\n"
"}\n"
"QTabWidget::pane {\n"
" 	border: 0px solid rgb(39, 44, 54);\n"
" 	color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:selected{\n"
"	background-color:rgb(39, 44, 54);\n"
" 	color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:!selected{\n"
"	background-color: rgb(30, 35, 45);\n"
" 	color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:!selected:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
" 	color: rgb(255, 255, 255);\n"
"}\n"
"/* Splitter */\n"
"QSplitter::handle{\n"
"	background-color: gray;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.config_frame = QFrame(self.centralWidget)
        self.config_frame.setObjectName(u"config_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.config_frame.sizePolicy().hasHeightForWidth())
        self.config_frame.setSizePolicy(sizePolicy1)
        self.config_frame.setMaximumSize(QSize(660, 134))
        self.config_frame.setBaseSize(QSize(100, 100))
        self.config_frame.setStyleSheet(u"height:200px\n"
"")
        self.config_frame.setFrameShape(QFrame.StyledPanel)
        self.config_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.config_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.config_frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"font-size:18px;\n"
"font:Sans-serif;")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.config_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(72)
        sizePolicy3.setVerticalStretch(100)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setStyleSheet(u"border-radius:7px;\n"
"")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_platform = QHBoxLayout()
        self.horizontalLayout_platform.setObjectName(u"horizontalLayout_platform")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_platform.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.config_frame)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(70)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setStyleSheet(u"font-size:18px;\n"
"font:Sans-serif;")

        self.horizontalLayout_platform.addWidget(self.label)

        self.comboBox_2 = QComboBox(self.config_frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(250)
        sizePolicy5.setVerticalStretch(200)
        sizePolicy5.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy5)
        self.comboBox_2.setStyleSheet(u"font-size:14px;\n"
"font:Sans-serif;\n"
"border-radius:7px;")

        self.horizontalLayout_platform.addWidget(self.comboBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_platform.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_platform)

        self.horizontalLayout_Solution = QHBoxLayout()
        self.horizontalLayout_Solution.setObjectName(u"horizontalLayout_Solution")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_Solution.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.config_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setStyleSheet(u"font-size:18px;\n"
"font:Sans-serif;")

        self.horizontalLayout_Solution.addWidget(self.label_2)

        self.comboBox = QComboBox(self.config_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(250)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy6)
        self.comboBox.setStyleSheet(u"font-size:14px;\n"
"font:Sans-serif;\n"
"border-radius:7px;")

        self.horizontalLayout_Solution.addWidget(self.comboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_Solution.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_Solution)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.checkBox = QCheckBox(self.config_frame)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(20)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy7)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setStyleSheet(u"font-size:18px;\n"
"font:Sans-serif;\n"
"background:none;")
        self.checkBox.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.checkBox_2 = QCheckBox(self.config_frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy2)
        self.checkBox_2.setStyleSheet(u"font-size:18px;\n"
"font:Sans-serif;\n"
"background:none;")

        self.horizontalLayout_5.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(2, 34)

        self.verticalLayout_3.addWidget(self.config_frame)


        self.verticalLayout_2.addWidget(self.centralWidget)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Design Creator", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Source File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plat Form", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"platForm1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"platForm2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"platForm3", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Solution ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Solution1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Solution2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Solution3", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"   Launch DPI", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"   Terminate DPI", None))
    # retranslateUi

        def main():
                if QApplication.instance():
                        app = QApplication.instance()
                else:
                        app = QApplication(sys.argv)
                model = Model()
                model.loadModel()
                window = SigVerifWindow(model)
                window.show()
                app.exec()

                if __name__ == '__main__':
                     main()