from PyQt5 import QtWidgets
from UIs.RuntimeUI import Ui_MainWindow
from UIs.CrashConfigUI import CrashConfigWindow
from UIs.HangConfigUI import HangConfigWindow  # Import HangConfigWindow
from PyQt5.QtWidgets import *

class CustomRuntimeWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.widget_resize()
        #self.ui.groupBox.resizeEvent = lambda event: self.window_resize()

        self.RunC=self.ui.RunC_2
        self.ErrorL=self.ui.ErrorL_2
        self.ErrorC=self.ui.ErrorC_2
        self.ErrorConf=self.ui.ErrorConf_2
        self.toolButtonBrowseOutput_2=self.ui.toolButtonBrowseDatabase_3 
        self.lineEditOutputDirectory_2 = self.ui.lineEditDatabasePath_2
        self.ErrorConf.hide()

        self.ErrorC.currentTextChanged.connect(self.check_error_conf_visibility)
        self.ErrorConf.clicked.connect(self.show_error_config)  # Modified connection

        self.config_window_crash = CrashConfigWindow(self)
        self.config_window_hang = HangConfigWindow(self)  # Create an instance of HangConfigWindow
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
        elif selected_text == "Hang":  # Check for Hang error type
            self.config_window_hang.show_window()

    # def window_resize(self):
    #     self.ui.groupBox.resize(self.centralWidget().size())

    # def widget_resize(self):
    #     self.ui.groupBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    #     self.window_resize()
    
    def collect_running_config(self):
        self.running_configurations['script_path'] = self.lineEditOutputDirectory_2.text()
        self.running_configurations['run_script'] = self.RunC.isChecked()
        self.running_configurations['error_type'] = self.ErrorC.currentText()
        self.running_configurations['crash_configurations'] = {}

        if self.running_configurations['error_type'] == "Crash":
            self.running_configurations['crash_configurations']['crashed_process'] = self.config_window_crash.tool_combo_box.currentText()
            self.running_configurations['crash_configurations']['attach_gdb'] = self.config_window_crash.checkbox1.isChecked()
        
        if self.running_configurations['error_type'] == "Hang":
            selected_button = self.config_window_hang.button_group.checkedButton()
            if selected_button:
                self.running_configurations['crash_configurations']['crashed_process'] = selected_button.text()
        #print(self.running_configurations)

            
def run_custom_runtime():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CustomRuntimeWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_custom_runtime()
