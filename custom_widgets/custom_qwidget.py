"""!
It contains CustomQWidget class.
"""
from PyQt5.QtWidgets import QWidget


class CustomQWidget(QWidget):
    """!
    CustomQWidget class used to provide the regular functionalities of the QWidget, but overrides the behaviour of
    closing.
    """

    def __init__(self, window):
        """!
        @brief Constructor which creates an instance of the CustomQWidget.
        @param window: the window implementing the CustomWidget.
        @return: Instance of the CustomQWidget.
        """
        super(CustomQWidget, self).__init__()
        self.window = window

    def closeEvent(self, event):
        """!
        @brief Function overriding which clears the state of the connections and accepts the closing event.
        @param event: the closing event to be accepted.
        """
        self.window.clear()
        event.accept()
