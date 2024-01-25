
import sys
from PyQt5 import QtWidgets
from src.frontend.CustomWidgets.mainwindow import MyMainWindow



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

