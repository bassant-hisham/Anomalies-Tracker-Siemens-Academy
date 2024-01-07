from PyQt5 import QtCore, QtGui, QtWidgets
from CustomComodelsConfig_ui import Ui_CustomComodelsConfig_Form

class AddCustomConfig:
    def __init__(self,Ui_CustomComodelsConfig_FormObject : Ui_CustomComodelsConfig_Form,CustomConfCounter:int):
        self.CustomConfCounter=CustomConfCounter
        self.Ui_CustomComodelsConfig_FormObject=Ui_CustomComodelsConfig_FormObject
        self.Add_CustomConf()

    def Add_CustomConf(self) -> None:
        new_CustomConfig_groupBox=self.DuplicateCustomConfGroupBox()
        self.Ui_CustomComodelsConfig_FormObject.gridLayout.addWidget(new_CustomConfig_groupBox)

    def DuplicateCustomConfGroupBox(self) -> QtWidgets.QGroupBox:

        CustomConfig_InnergroupBox = QtWidgets.QGroupBox(self.Ui_CustomComodelsConfig_FormObject.CustomComodConf_groupBox)

        CustomConfig_InnergroupBox.setObjectName("CustomConfig_InnergroupBox")
        verticalLayout = QtWidgets.QVBoxLayout(CustomConfig_InnergroupBox)
        verticalLayout.setObjectName("verticalLayout")
        HostName_Hlayout = QtWidgets.QHBoxLayout()
        HostName_Hlayout.setContentsMargins(-1, 5, -1, 5)
        HostName_Hlayout.setObjectName("HostName_Hlayout")
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        HostName_Hlayout.addItem(spacerItem1)
        HostName_HSpacer_label = QtWidgets.QLabel(CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HostName_HSpacer_label.sizePolicy().hasHeightForWidth())
        HostName_HSpacer_label.setSizePolicy(sizePolicy)
        HostName_HSpacer_label.setStyleSheet("font-size:22px;\n"
"font:normal")
        HostName_HSpacer_label.setObjectName("HostName_HSpacer_label")
        HostName_Hlayout.addWidget(HostName_HSpacer_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        HostName_Hlayout.addItem(spacerItem2)
        HostName_comboBox = QtWidgets.QComboBox(CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HostName_comboBox.sizePolicy().hasHeightForWidth())
        HostName_comboBox.setSizePolicy(sizePolicy)
        HostName_comboBox.setStyleSheet("background-color:#343b48;\n"
"font:normal;\n"
"font-size:22px;\n"
"border-radius:7px;")
        HostName_comboBox.setObjectName("HostName_comboBox")
        HostName_comboBox.addItem("")
        HostName_comboBox.addItem("")
        HostName_comboBox.addItem("")
        HostName_comboBox.addItem("")
        HostName_Hlayout.addWidget(HostName_comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        HostName_Hlayout.addItem(spacerItem3)
        verticalLayout.addLayout(HostName_Hlayout)
        DomainId_Hlayout = QtWidgets.QHBoxLayout()
        DomainId_Hlayout.setContentsMargins(-1, 5, -1, 5)
        DomainId_Hlayout.setObjectName("DomainId_Hlayout")
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        DomainId_Hlayout.addItem(spacerItem4)
        DomainId_HSpacer_label = QtWidgets.QLabel(CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DomainId_HSpacer_label.sizePolicy().hasHeightForWidth())
        DomainId_HSpacer_label.setSizePolicy(sizePolicy)
        DomainId_HSpacer_label.setStyleSheet("font-size:22px;\n"
"font:normal")
        DomainId_HSpacer_label.setObjectName("DomainId_HSpacer_label")
        DomainId_Hlayout.addWidget(DomainId_HSpacer_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        DomainId_Hlayout.addItem(spacerItem5)
        DomainId_comboBox = QtWidgets.QComboBox(CustomConfig_InnergroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DomainId_comboBox.sizePolicy().hasHeightForWidth())
        DomainId_comboBox.setSizePolicy(sizePolicy)
        DomainId_comboBox.setStyleSheet("background-color:#343b48;\n"
"font:normal;\n"
"font-size:22px;\n"
"border-radius:7px;")
        DomainId_comboBox.setObjectName("DomainId_comboBox")
        DomainId_comboBox.addItem("")
        DomainId_comboBox.addItem("")
        DomainId_comboBox.addItem("")
        DomainId_comboBox.addItem("")
        DomainId_Hlayout.addWidget(DomainId_comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        DomainId_Hlayout.addItem(spacerItem6)
        verticalLayout.addLayout(DomainId_Hlayout)

        _translate = QtCore.QCoreApplication.translate
        CustomConfig_InnergroupBox.setTitle(_translate("CustomComodelsConfig_Form", "Config "+ str(self.CustomConfCounter)))
        HostName_HSpacer_label.setText(_translate("CustomComodelsConfig_Form", "Host Name"))
        HostName_comboBox.setItemText(0, _translate("CustomComodelsConfig_Form", "Auto"))
        HostName_comboBox.setItemText(1, _translate("CustomComodelsConfig_Form", "egc-med-bell"))
        HostName_comboBox.setItemText(2, _translate("CustomComodelsConfig_Form", "egc-med-baird"))
        HostName_comboBox.setItemText(3, _translate("CustomComodelsConfig_Form", "egc-med-nozark"))
        DomainId_HSpacer_label.setText(_translate("CustomComodelsConfig_Form", "Domain Id"))
        DomainId_comboBox.setItemText(0, _translate("CustomComodelsConfig_Form", "0"))
        DomainId_comboBox.setItemText(1, _translate("CustomComodelsConfig_Form", "1"))
        DomainId_comboBox.setItemText(2, _translate("CustomComodelsConfig_Form", "2"))
        DomainId_comboBox.setItemText(3, _translate("CustomComodelsConfig_Form", "3"))

       

   
       


        return CustomConfig_InnergroupBox
