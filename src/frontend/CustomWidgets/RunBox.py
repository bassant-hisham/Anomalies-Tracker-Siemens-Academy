from PyQt5 import QtWidgets
from src.frontend.CustomWidgets.UIs.RunningConfigUI import Ui_RunningConfiguration
from src.frontend.CustomWidgets.UIs.CrashConfigUI import CrashConfigWindow
from src.frontend.CustomWidgets.UIs.HangConfigUI import HangConfigWindow  # Import HangConfigWindow
from PyQt5.QtWidgets import *

class MyRunBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RunningConfiguration()
        self.ui.setupUi(self)

        self.ui.BrowseScriptPath_button.hide()
        self.ui.ScriptPath_label.hide()
        self.ui.ScriptPath_lineEdit.hide()
        #self.widget_resize()
        #self.ui.groupBox.resizeEvent = lambda event: self.window_resize()

        self.RunC=self.ui.RunC_2
        self.ErrorL=self.ui.ErrorL_2
        self.ErrorC=self.ui.ErrorC_2
        self.ErrorConf=self.ui.ErrorConf_2
        self.toolButtonBrowseOutput_2=self.ui.BrowseScriptPath_button 
        self.lineEditOutputDirectory_2 = self.ui.ScriptPath_lineEdit
        self.ErrorConf.hide()

        self.ErrorC.currentTextChanged.connect(self.check_error_conf_visibility)
        self.ErrorConf.clicked.connect(self.show_error_config)  # Modified connection

        self.config_window_crash = CrashConfigWindow()
        self.config_window_hang = HangConfigWindow()  # Create an instance of HangConfigWindow
        self.config_window_crash.closed_signal.connect(self.handle_another_window_closed)
        self.config_window_hang.closed_signal.connect(self.handle_another_window_closed)
        self.ui.RunC_2.clicked.connect(self.showScriptPath)
        self.running_configurations = {}
        self.isconnected = False
        self.myparent=self.parent()

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
        if(self.ui.RunC_2.isChecked()==True):
            self.ui.BrowseScriptPath_button.show()
            self.ui.ScriptPath_label.show()
            self.ui.ScriptPath_lineEdit.show()
        else:
            self.ui.BrowseScriptPath_button.hide()
            self.ui.ScriptPath_label.hide()
            self.ui.ScriptPath_lineEdit.hide()
    
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
        self.ui.ScriptPath_label.show()
        self.ui.ScriptPath_lineEdit.show()
        self.lineEditOutputDirectory_2.setText(running_dict['running_configurations']['script_path'])
        self.lineEditOutputDirectory_2.setReadOnly(True)
        self.ErrorC.setCurrentText(running_dict['running_configurations']['error_type'])
        self.ErrorC.setDisabled(True)
        if running_dict['running_configurations']['error_type'] == "Crash":
            #self.config_window_crash.closed_signal.disconnect(self.handle_another_window_closed) 
            self.ErrorConf.clicked.connect(lambda _, rd=running_dict: self.show_crash_data(rd))  
        if running_dict['running_configurations']['error_type'] == "Hang": 
            #self.config_window_hang.closed_signal.disconnect(self.handle_another_window_closed) 
            self.ErrorConf.clicked.connect(lambda _, rd=running_dict: self.show_hang_data(rd))  

        
        
                       
def run_custom_runtime():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyRunBox()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_custom_runtime()
