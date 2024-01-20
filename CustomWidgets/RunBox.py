from PyQt5 import QtWidgets
from UIs.RunningConfigUI import Ui_RunningConfiguration
from UIs.CrashConfigUI import CrashConfigWindow
from UIs.HangConfigUI import HangConfigWindow  # Import HangConfigWindow
from PyQt5.QtWidgets import *

class MyRunBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RunningConfiguration()
        self.ui.setupUi(self)
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
        self.running_configurations = {}

    def check_error_conf_visibility(self, selected_text):
        if selected_text in ["Crash", "Hang"]:
            self.ErrorConf.show()
        else:
            self.ErrorConf.hide()

    def show_error_config(self):
        selected_text = self.ErrorC.currentText()
        if selected_text == "Crash":
            self.config_window_crash.show_window()
            self.config_window_crash.center_on_parent()
        elif selected_text == "Hang":  # Check for Hang error type
            self.config_window_hang.show_window()
            self.config_window_hang.center_on_parent()
        grandparent = self.get_grandparent(self)
        grandparent.setEnabled(False)
    
    def get_grandparent(self, widget):
        grandparent = widget.parent()
        while grandparent and grandparent.parent():
            grandparent = grandparent.parent()
        return grandparent
    
    def handle_another_window_closed(self):
        grandparent = self.get_grandparent(self)
        grandparent.setEnabled(True)
    
    def collect_running_config(self):
        self.running_configurations['script_path'] = self.lineEditOutputDirectory_2.text()
        self.running_configurations['run_script'] = self.RunC.isChecked()
        self.running_configurations['error_type'] = self.ErrorC.currentText()
        self.running_configurations['crashed_process'] = ""
        self.running_configurations['attach_gdb'] = ""
        if self.running_configurations['error_type'] == "Crash":
            self.running_configurations['crashed_process'] = self.config_window_crash.tool_combo_box.currentText()
            self.running_configurations['attach_gdb'] = self.config_window_crash.checkbox1.isChecked()
        
        if self.running_configurations['error_type'] == "Hang":
            selected_button = self.config_window_hang.button_group.checkedButton()
            if selected_button:
                self.running_configurations['crashed_process'] = selected_button.text()
                
        #print(self.running_configurations)

                
def run_custom_runtime():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyRunBox()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_custom_runtime()