# Import generated UI code
from Runtime import Ui_MainWindow  # Replace outputwith your generated file name

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
