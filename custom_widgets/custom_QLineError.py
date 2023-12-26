from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit

from GUI.Views.design_creator_gui.mainwindow.errors_handler.errors_objects.generic_error_object import \
    GenericError


class CustomQLineError(QLineEdit):
    clicked = pyqtSignal()
    text: str = None
    error_object: GenericError = None

    def __init__(self, error_object: GenericError, text: str):
        super().__init__()
        self.setText(text)
        self.setReadOnly(True)
        self.error_object = error_object
        # disable selection of text
        self.selectionChanged.connect(lambda: self.setSelection(0, 0))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def event(self, event):
        if event.type() == QtGui.QMouseEvent.MouseButtonPress and event.button() == QtCore.Qt.LeftButton:
            self.error_object.navigation_behaviour()
        return super().event(event)
