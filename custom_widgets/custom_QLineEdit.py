from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtWidgets import QLineEdit

from GUI.custom_widgets.clickable_table import ClickableTable


class CustomQLineEdit(QLineEdit):
    """!
    @brief: This class is used to create a custom QLineEdit
    """

    state = None
    doubleClicked = pyqtSignal()
    empty_flag = False

    def __init__(self, text, state):
        """!
        @brief: This method is used to initialize the custom QLineEdit
        @param text: The text to be displayed
        @param state: The state of the line edit
        """

        super().__init__()
        self.setFont(QFont("Times", 9, QFont.DemiBold))
        self.setText(text)
        self.set_state(state)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def set_state(self, state: bool, warning_flag=False) -> None:
        """!
        @brief: This method is used to set the state of the line edit
        @param state: The state to be set
        @param warning_flag: Flag to set the line edit to warning state
        """

        if state and not self.empty_flag:
            self.setStyleSheet(
                "QLineEdit {selection-background-color: rgb(33, 188, 180); border: 1px solid grey; border-radius: 10px;}")
            self.state = True
        if not state:
            self.setStyleSheet(
                "QLineEdit {selection-background-color: rgb(241, 89, 90); border: 1px solid rgb(241, 89, 90); border-radius: 10px;}")
            self.state = False

        if warning_flag and not self.state:
            self.state = "warning"
            self.setStyleSheet(
                "QLineEdit {selection-background-color: rgb(251, 133, 0); border: 1px solid rgb(251, 133, 0); border-radius: 10px;}")

    def refresh_empty_flag(self) -> bool:
        """!
        @brief: This method is used to refresh the empty flag
        @return: The empty flag
        """

        if self.text() == "":
            self.empty_flag = True
            self.set_state(False)
            return True
        self.empty_flag = False
        self.set_state(True)
        return False

    def mousePressEvent(self, QMouseEvent):
        QMouseEvent.ignore()

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        """!
        @brief: This method is used to handle the focus in event
        @param e: The focus event
        """

        super().focusInEvent(e)
        QTimer.singleShot(0, self.selectAll)
        # to focus, obj.setFocus() is used

    def event(self, event):

        if event.type() == QtGui.QMouseEvent.MouseButtonDblClick:
            self.doubleClicked.emit()
        return super().event(event)

    def setText(self, text: str) -> None:
        """!
        @brief: This method is used to set the text of the line edit
        @param a0: The text to be set
        """

        super().setText(text)
        self.textChanged.emit(text)

    @classmethod
    def insert_QLineEdit_cell(cls, table: ClickableTable, row_index: int, col_index: int,
                              value: str, validator: QRegExpValidator = None,
                              disable_flag: bool = False) -> None:
        """!
        @brief: This method is used to insert a line edit cell in a table
        @param table: The table in which the cell is to be inserted
        @param row_index: The row index of the cell
        @param col_index: The column index of the cell
        @param value: The value to be set in the cell
        @param validator: The validator to be set in the cell
        @param disable_flag: Flag to disable the cell
        """
        line_edit = cls.get_line_edit_instance(table, row_index, col_index, value, validator, disable_flag)
        if not disable_flag:
            from GUI.Views.design_creator_gui.mainwindow.tables_data_controllers.data_change_controllers.change_controller import \
                ChangeController
            line_edit.textChanged.connect(
                lambda: ChangeController.handle_change(table, col_index, row_index))
        if validator is not None:
            line_edit.setValidator(validator)
        if disable_flag:
            line_edit.setEnabled(False)
        table.setCellWidget(row_index, col_index, line_edit)

    @classmethod
    def get_line_edit_instance(cls, table: ClickableTable, row_index: int, col_index: int,
                               value: str, validator: QRegExpValidator = None,
                               disable_flag: bool = False):
        return CustomQLineEdit(value, True)
