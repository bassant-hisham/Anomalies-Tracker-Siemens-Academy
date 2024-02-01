from PyQt5 import QtWidgets
from src.frontend.CustomWidgets.UIs.RunningConfigUI import Ui_RunningConfiguration
from src.frontend.CustomWidgets.UIs.CrashConfigUI import CrashConfigWindow
from src.frontend.CustomWidgets.UIs.HangConfigUI import HangConfigWindow  # Import HangConfigWindow
from PyQt5.QtWidgets import *
from src.frontend.CustomWidgets.commonFunctions import *
from PyQt5.QtGui import QIcon

class MyRunBox(QtWidgets.QWidget,Ui_RunningConfiguration):
    def __init__(self,id:int,Running:list,scrollLayoutRunning:QVBoxLayout):
        super(MyRunBox,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('src/frontend/IconsImages/siemens_logo_icon.png'))
        self.BrowseScriptPath_button.hide()
        self.ScriptPath_label.hide()
        self.ScriptPath_lineEdit.hide()
        # #self.widget_resize()
        # #self.ui.groupBox.resizeEvent = lambda event: self.window_resize()
        self.groupBox.setTitle("Running Configuration " + str(id))        
        self.RunC=self.RunC_2
        self.ErrorL=self.ErrorL_2
        self.ErrorC=self.ErrorC_2
        self.ErrorConf=self.ErrorConf_2
        self.toolButtonBrowseOutput_2=self.BrowseScriptPath_button 
        self.lineEditOutputDirectory_2 = self.ScriptPath_lineEdit
        self.ErrorConf.hide()

        self.ErrorC.currentTextChanged.connect(self.check_error_conf_visibility)
        self.ErrorConf.clicked.connect(self.show_error_config)  # Modified connection
        self.toolButtonBrowseOutput_2.clicked.connect(lambda: showFileDialog(self,self.lineEditOutputDirectory_2))  

        self.config_window_crash = CrashConfigWindow()
        self.config_window_hang = HangConfigWindow()  # Create an instance of HangConfigWindow
        self.config_window_crash.closed_signal.connect(self.handle_another_window_closed)
        self.config_window_hang.closed_signal.connect(self.handle_another_window_closed)
        self.RunC_2.clicked.connect(self.showScriptPath)
        self.delete_pushButton.clicked.connect(self.deleteRunningWidget)

        self.running_configurations = {}
        self.isconnected = False
        self.myparent=self.parent()
        self.RunningList=Running
        self.RunningLayout=scrollLayoutRunning

    def check_error_conf_visibility(self, selected_text):
        if selected_text in ["Crash", "Hang"]:
            self.ErrorConf.show()
        else:
            self.ErrorConf.hide()

    def show_error_config(self):
        selected_text = self.ErrorC.currentText()
        self.isconnected = True
        if selected_text == "Crash":
            self.config_window_crash.show_window()
            self.config_window_crash.center_on_parent()
        elif selected_text == "Hang":  # Check for Hang error type
            self.config_window_hang.show_window()
            self.config_window_hang.center_on_parent()
        grandparent = self.get_grandparent(self)
        grandparent.setEnabled(False)
    
    def get_grandparent(self, widget):
        grandparent = widget.myparent
        temp=type(grandparent)
        while grandparent and grandparent.parent():
            grandparent = grandparent.parent()
        return grandparent
    
    def handle_another_window_closed(self):
        grandparent = self.get_grandparent(self)
        grandparent.setEnabled(True)

    def showScriptPath(self):
        if(self.RunC_2.isChecked()==True):
            self.BrowseScriptPath_button.show()
            self.ScriptPath_label.show()
            self.ScriptPath_lineEdit.show()
        else:    
            self.BrowseScriptPath_button.hide()
            self.ScriptPath_label.hide()
            self.ScriptPath_lineEdit.hide()
    
    def collect_running_config(self):
        self.running_configurations['running_configurations']={}
        self.running_configurations['running_configurations']['run_script'] = self.RunC.isChecked()
        self.running_configurations['running_configurations']['error_type'] = self.ErrorC.currentText()
        self.running_configurations['running_configurations']['crash_configurations']={}
        self.running_configurations['running_configurations']['crash_configurations']['attach_gdb'] = ""
        self.running_configurations['running_configurations']['crash_configurations']['crashed_process']=""
        if self.running_configurations['running_configurations']['error_type'] == "Crash":
            self.running_configurations['running_configurations']['crash_configurations']['crashed_process'] = self.config_window_crash.tool_combo_box.currentText()
            self.running_configurations['running_configurations']['crash_configurations']['attach_gdb'] = self.config_window_crash.checkbox1.isChecked()
        
        if self.running_configurations['running_configurations']['error_type'] == "Hang":
            selected_button = self.config_window_hang.button_group.checkedButton()
            if selected_button:
                self.running_configurations['running_configurations']['crash_configurations']['crashed_process'] = selected_button.text()
        self.running_configurations['running_configurations']['script_path'] = self.lineEditOutputDirectory_2.text()        
        

    def show_crash_data(self,running_dict):
        self.config_window_crash.tool_combo_box.setCurrentText(running_dict['running_configurations']['crash_configurations']['crashed_process'] )
        self.config_window_crash.tool_combo_box.setDisabled(True)
        self.config_window_crash.checkbox1.setCheckState(running_dict['running_configurations']['crash_configurations']['attach_gdb'])
        self.config_window_crash.checkbox1.setDisabled(True)
        self.config_window_crash.show_window()
        self.config_window_crash.center_on_parent()
        
    
    def show_hang_data(self,running_dict):
        selected = running_dict['running_configurations']['crash_configurations']['crashed_process']
        for radio_button in self.config_window_hang.button_group.buttons():
            if radio_button.text() == selected:
                radio_button.setChecked(True)
                break
            radio_button.setEnabled(False)
        self.config_window_hang.show_window()
        self.config_window_hang.center_on_parent()
       

        
    def show_data(self,running_dict):
        self.RunC.setCheckState(True)
        self.RunC.setDisabled(True)
        self.ScriptPath_label.show()
        self.ScriptPath_lineEdit.show()
        self.lineEditOutputDirectory_2.setText(running_dict['running_configurations']['script_path'])
        self.lineEditOutputDirectory_2.setReadOnly(True)
        self.ErrorC.setCurrentText(running_dict['running_configurations']['error_type'])
        self.ErrorC.setDisabled(True)
        self.delete_pushButton.setDisabled(True)
        if running_dict['running_configurations']['error_type'] == "Crash":
            #self.config_window_crash.closed_signal.disconnect(self.handle_another_window_closed) 
            self.ErrorConf.clicked.connect(lambda _, rd=running_dict: self.show_crash_data(rd))  
        if running_dict['running_configurations']['error_type'] == "Hang": 
            #self.config_window_hang.closed_signal.disconnect(self.handle_another_window_closed) 
            self.ErrorConf.clicked.connect(lambda _, rd=running_dict: self.show_hang_data(rd))  

    def deleteRunningWidget(self):
        self.RunningList.remove(self)
        self.RunningLayout.removeWidget(self)
        self.deleteLater()
        
        for index,widget in enumerate(self.RunningList):
            self.RunningList[index].id=index+1
            self.RunningList[index].groupBox.setTitle("Running Configuration"+str(index+1))
