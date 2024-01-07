from lanchuining_conf_ui import Ui_lanchuning_config
from PyQt5 import QtCore, QtGui, QtWidgets
from DutConfg_ui import Ui_DutConf_Form
from CustomComodelsConfig_ui import Ui_CustomComodelsConfig_Form
from AddCustomConfig import AddCustomConfig

class Add_DUTConfClass():
    def __init__(self, ui_lanchuning_config : Ui_lanchuning_config, DutConfs_VLayout : QtWidgets.QVBoxLayout,DutConfCounter: int):
        self.ui_lanchuning_configObject=ui_lanchuning_config
        self.DutConfs_VLayout=DutConfs_VLayout
        self.DutConfgObject=Ui_DutConf_Form()
        self.Ui_CustomComodelsConfig_FormObject=Ui_CustomComodelsConfig_Form()
        self.DutConfCounter= DutConfCounter
        self.CustomConfCounter=1
        self.Add_DUTConf()

    def Add_DUTConf(self) -> None:

        self.new_DutConfig_groupBox = QtWidgets.QWidget(self.ui_lanchuning_configObject.lanch_conf_Hlayout)
        self.DutConfgObject.setupUi(self.new_DutConfig_groupBox)
        self.DutConfs_VLayout.addWidget(self.new_DutConfig_groupBox)
        self.DutConfgObject.DutConfig_groupBox.setTitle("Dut Configuration "+str(self.DutConfCounter))

        self.RegisterSignalsForEachDut()

    def RegisterSignalsForEachDut(self) -> None:

        self.DutConfgObject.CustomComConf_checkbox.stateChanged.connect(self.View_CustomConf)
        self.DutConfgObject.ConfigType_comboBox.currentIndexChanged.connect(self.handleSnapshotsNu)
    
    def RegisterSignalsForEachCustomConfig(self) -> None:
        self.Ui_CustomComodelsConfig_FormObject.CustomComodelsAdd_PushButton.clicked.connect(self.Add_CustomConf)


    def View_CustomConf(self) -> None:

        if  self.DutConfgObject.CustomComConf_checkbox.isChecked()==True:
                self.CustomConfig_groupBox = QtWidgets.QWidget(self.new_DutConfig_groupBox)
                self.Ui_CustomComodelsConfig_FormObject.setupUi(self.CustomConfig_groupBox)

                self.CustomConfs_VLayout=QtWidgets.QVBoxLayout()
                self.CustomConfs_VLayout.addWidget(self.CustomConfig_groupBox)
                self.DutConfgObject.verticalLayout_5.addLayout(self.CustomConfs_VLayout)

                self.RegisterSignalsForEachCustomConfig()

        elif self.DutConfgObject.CustomComConf_checkbox.isChecked()==False:
                self.CustomConfig_groupBox.hide()
    def Add_CustomConf(self):
        self.CustomConfCounter+=1
        self.AddCustomConfigObject=AddCustomConfig(self.Ui_CustomComodelsConfig_FormObject,self.CustomConfCounter)

    def handleSnapshotsNu(self) -> None:

        for i in reversed(range(self.DutConfgObject.ToConfigValue_Hlayout.count())): 
                # temp3=self.DutConfgObject.FromConfigValue_Hlayout.count()
                # temp=self.DutConfgObject.FromConfigValue_Hlayout.itemAt(i) 
                # temp2=self.DutConfgObject.FromConfigValue_Hlayout.itemAt(i).widget()
                if(self.DutConfgObject.ToConfigValue_Hlayout.itemAt(i).widget()!=None):
                    self.DutConfgObject.ToConfigValue_Hlayout.removeWidget(self.DutConfgObject.ToConfigValue_Hlayout.itemAt(i).widget())
                else:
                    self.DutConfgObject.ToConfigValue_Hlayout.removeItem(self.DutConfgObject.ToConfigValue_Hlayout.itemAt(i))


        for i in reversed(range(self.DutConfgObject.FromConfigValue_Hlayout.count())):
                temp3=self.DutConfgObject.FromConfigValue_Hlayout.count()
                #temp=self.DutConfgObject.FromConfigValue_Hlayout.itemAt(i) 
                temp2=self.DutConfgObject.FromConfigValue_Hlayout.itemAt(i).widget()
                if(self.DutConfgObject.FromConfigValue_Hlayout.itemAt(i).widget()!=None):
                    self.DutConfgObject.FromConfigValue_Hlayout.removeWidget(self.DutConfgObject.FromConfigValue_Hlayout.itemAt(i).widget())
                else:
                    self.DutConfgObject.FromConfigValue_Hlayout.removeItem(self.DutConfgObject.FromConfigValue_Hlayout.itemAt(i))

                    
        if (self.DutConfgObject.ConfigType_comboBox.currentIndex()==0):

            spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            spacerItem3 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

            self.Fromlabel=QtWidgets.QLabel("From",self.DutConfgObject.ConfigType_comboBox)
            self.Tolabel=QtWidgets.QLabel("To",self.DutConfgObject.ConfigType_comboBox)
            self.FromConfigValue=QtWidgets.QLineEdit(self.DutConfgObject.ConfigType_comboBox)
            self.ToConfigValue=QtWidgets.QLineEdit(self.DutConfgObject.ConfigType_comboBox)

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(20)
            sizePolicy.setVerticalStretch(0)
            self.Fromlabel.setSizePolicy(sizePolicy)
            self.Tolabel.setSizePolicy(sizePolicy)

            sizePolicy.setHorizontalStretch(55)
            sizePolicy.setVerticalStretch(0)
            self.FromConfigValue.setSizePolicy(sizePolicy)
            self.ToConfigValue.setSizePolicy(sizePolicy)

            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem1)
            self.DutConfgObject.FromConfigValue_Hlayout.addWidget(self.Fromlabel)
            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem2)
            self.DutConfgObject.FromConfigValue_Hlayout.addWidget(self.FromConfigValue)
            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem3)

            self.DutConfgObject.ToConfigValue_Hlayout.addItem(spacerItem1)
            self.DutConfgObject.ToConfigValue_Hlayout.addWidget(self.Tolabel)
            self.DutConfgObject.ToConfigValue_Hlayout.addItem(spacerItem2)
            self.DutConfgObject.ToConfigValue_Hlayout.addWidget(self.ToConfigValue)
            self.DutConfgObject.ToConfigValue_Hlayout.addItem(spacerItem3)

            # self.DutConfgObject.ConfigValue_Vlayout.addLayout(self.DutConfgObject.FromConfigValue_Hlayout)
            # self.DutConfgObject.ConfigValue_Vlayout.addLayout(self.DutConfgObject.ToConfigValue_Hlayout)
            
        elif (self.DutConfgObject.ConfigType_comboBox.currentIndex()==1):
            spacerItem_left = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            spacerItem_mid = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            spacerItem_right = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.ConfigValuelabel=QtWidgets.QLabel("Config Value",self.DutConfgObject.ConfigType_comboBox)
            self.ConfigValueList=QtWidgets.QLineEdit(self.DutConfgObject.ConfigType_comboBox)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(20)
            sizePolicy.setVerticalStretch(0)
            self.ConfigValuelabel.setSizePolicy(sizePolicy)

            sizePolicy.setHorizontalStretch(55)
            sizePolicy.setVerticalStretch(0)
            self.ConfigValueList.setSizePolicy(sizePolicy)

            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem_left)
            self.DutConfgObject.FromConfigValue_Hlayout.addWidget(self.ConfigValuelabel)
            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem_mid)
            self.DutConfgObject.FromConfigValue_Hlayout.addWidget(self.ConfigValueList)
            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem_right)
            #self.DutConfgObject.ConfigValue_Vlayout.addLayout(self.DutConfgObject.FromConfigValue_Hlayout)
            
        else:
            spacerItem_left = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            spacerItem_mid = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            spacerItem_right = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.ConfigValuelabel=QtWidgets.QLabel("Config Value",self.DutConfgObject.ConfigType_comboBox)
            self.ConfigValue=QtWidgets.QLineEdit(self.DutConfgObject.ConfigType_comboBox)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(20)
            sizePolicy.setVerticalStretch(0)
            self.ConfigValuelabel.setSizePolicy(sizePolicy)

            sizePolicy.setHorizontalStretch(55)
            sizePolicy.setVerticalStretch(0)
            self.ConfigValue.setSizePolicy(sizePolicy)

            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem_left)
            self.DutConfgObject.FromConfigValue_Hlayout.addWidget(self.ConfigValuelabel)
            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem_mid)
            self.DutConfgObject.FromConfigValue_Hlayout.addWidget(self.ConfigValue)
            self.DutConfgObject.FromConfigValue_Hlayout.addItem(spacerItem_right)
            #self.DutConfgObject.ConfigValue_Vlayout.addLayout(self.DutConfgObject.FromConfigValue_Hlayout)
