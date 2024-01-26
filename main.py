
import sys
from PyQt5 import QtWidgets
from src.frontend.CustomWidgets.mainwindow import MyMainWindow

from src.backend.Jenkins_APIs import Jenkins


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
