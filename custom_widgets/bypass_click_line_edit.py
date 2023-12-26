from PyQt5.QtGui import QRegExpValidator

from GUI.custom_widgets.clickable_table import ClickableTable
from GUI.custom_widgets.custom_QLineEdit import CustomQLineEdit


class BypassClickLineEdit(CustomQLineEdit):

    def __init__(self, text, state, col_index):
        super().__init__(text=text, state=state)
        self.col_index = col_index

    def mousePressEvent(self, event):
        # Ignore press event, so that signal gets propagated to parent widget, which is the table
        event.ignore()

    @classmethod
    def get_line_edit_instance(cls, table: ClickableTable, row_index: int, col_index: int,
                               value: str, validator: QRegExpValidator = None,
                               disable_flag: bool = False):
        return BypassClickLineEdit(value, True, col_index)
