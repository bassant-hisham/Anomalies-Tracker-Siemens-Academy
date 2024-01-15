from PyQt5 import QtWidgets
from Runtime import Ui_MainWindow
from CrashConfig import CrashConfigWindow
from HangConfig import HangConfigWindow  # Import HangConfigWindow

class CustomRuntimeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.widget)
        self.widget_resize()
        self.ui.widget.resizeEvent = lambda event: self.window_resize()

        self.RunC, self.ErrorL, self.ErrorC, self.ErrorConf, self.toolButtonBrowseOutput_2 ,self.lineEditOutputDirectory_2 = self.ui.get_ui_elements()
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

    def window_resize(self):
        self.ui.widget.resize(self.centralWidget().size())

    def widget_resize(self):
        self.ui.widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.window_resize()
    
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
        print(self.running_configurations)

            
def run_custom_runtime():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CustomRuntimeWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_custom_runtime()
