from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox, QLineEdit

from GUI.custom_widgets.clickable_table import ClickableTable


# delegate for centered items in combobox
class CenterDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(CenterDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class Filter(QObject):
    def __init__(self, widget):
        super().__init__(widget)
        self.widget = widget
        self.widget.installEventFilter(self)

    clicked = QtCore.pyqtSignal()

    def eventFilter(self, obj, event):
        if obj == self.widget:
            if event.type() == QtCore.QEvent.MouseButtonRelease and self.widget.isEnabled():
                self.clicked.emit()
                return True
        return False

    @classmethod
    def get_click_signal(cls, widget):
        return cls(widget).clicked


class UnselectableLineEdit(QLineEdit):
    """!
    @brief: This class is used to create a custom QLineEdit, which unselects itself when clicked
    """

    def __init__(self, parent=None):
        """!
        @brief: This method is used to initialize the custom QLineEdit
        @param parent: The parent widget
        """
        super(UnselectableLineEdit, self).__init__(parent)
        self.setReadOnly(True)

    def mousePressEvent(self, event):
        """!
        @brief: This method is used to handle the mousePressEvent to deselect the lineEdit when clicked
        @param event: The mousePressEvent
        """
        self.deselect()

    def mouseDoubleClickEvent(self, event):
        """!
        @brief: This method is used to handle the mouseDoubleClickEvent to deselect the lineEdit when double clicked
        @param event: The mouseDoubleClickEvent
        """
        self.deselect()

    def mouseReleaseEvent(self, event):
        """!
        @brief: This method is used to handle the mouseReleaseEvent to deselect the lineEdit released
        @param event: The mouseReleaseEvent
        """
        self.deselect()


class CustomQCombobox(QComboBox):
    """!
    @brief: This class is used to create a custom QCombobox
    """

    def __init__(self, list_of_items, parent=None):
        """!
        @brief: This method is used to initialize the custom QCombobox
        @param list_of_items: The list of items to be added to the combobox
        """
        super(CustomQCombobox, self).__init__(parent)
        self.addItems(list_of_items)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.setFont(font)
        self.setEditable(True)
        # set line edit to instance of UnselectableLineEdit
        self.setLineEdit(UnselectableLineEdit(self))
        self.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        Filter.get_click_signal(self).connect(self.toggle_popup)
        Filter.get_click_signal(self.lineEdit()).connect(self.toggle_popup)
        self.setItemDelegate(CenterDelegate(self))

    def toggle_popup(self):
        # check if popup is open
        if self.view().isVisible():
            self.hidePopup()
            # lose focus, THIS MAY? CAUSE ERRORS
            self.clearFocus()
        else:
            self.showPopup()

    def wheelEvent(self, event):
        # Disable the mouse scroll event
        event.ignore()

    def setCurrentText(self, text: str) -> None:
        """!
        @brief: This method is used to set the current text of the combobox
        @param text: The text to be set
        """

        index = self.findText(text)
        self.setCurrentIndex(index)
        self.currentIndexChanged.emit(index)

    @classmethod
    def insert_QComboBox_cell(cls, table: ClickableTable, row_index: int, col_index: int
                              , combo_list: list, disable_flag: bool = False, value: str = None) -> None:
        """!
        @brief: This method is used to insert a QComboBox cell in a table
        @param table: The table in which the cell will be inserted
        @param row_index: The row index of the cell
        @param col_index: The column index of the cell
        @param combo_list: The list of items to be added to the combobox
        @param disable_flag: Flag to disable the combobox
        @param value: The value to be set in the combobox
        """

        from GUI.Views.design_creator_gui.mainwindow.tables_data_controllers.data_change_controllers.change_controller import \
            ChangeController

        combo_box = CustomQCombobox(combo_list)
        if not disable_flag:
            combo_box.currentIndexChanged.connect(lambda: ChangeController.handle_change(table, col_index, row_index))
        if value is not None:
            combo_box.setCurrentText(value)
        if disable_flag:
            combo_box.setEnabled(False)
        table.setCellWidget(row_index, col_index, combo_box)
