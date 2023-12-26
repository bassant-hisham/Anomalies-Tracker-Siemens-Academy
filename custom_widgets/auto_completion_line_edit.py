import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


class AutoCompletionLineEdit(QLineEdit):
    """!
    @brief Class responsible for creating a line edit with auto completion. It is used in the design creator to allow
    the user to select the output directory and the database path. The auto completion is based on the environment
    variables. The user can type $ and then the name of the variable and the line edit will suggest the value of the
    variable. For example, if the user types $HOME then presses enter, the line edit will suggest
    the path to the user's home directory.
    """
    def __init__(self, parent=None, auto_completion_dict=None):
        super().__init__(parent)
        self.auto_completion_dict = {} if auto_completion_dict is None else auto_completion_dict

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            text = self.text()
            if text.startswith('$'):
                searching_text = text[1:]
                matches = [var for var in self.auto_completion_dict if var.startswith(searching_text)]
                if len(matches) == 1:
                    replacement = self.auto_completion_dict[matches[0]]
                    self.setText(replacement)
            return
        super().keyPressEvent(event)
