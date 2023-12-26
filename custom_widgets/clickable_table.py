from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget


class ClickableTable(QTableWidget):
    def __init__(self, *__args):
        super(ClickableTable, self).__init__(*__args)
        self.installEventFilter(self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            index = self.indexAt(event.pos())
            if index.isValid():
                self.setCurrentIndex(index)
        super().mousePressEvent(event)

    def get_name_without_solution(self):
        # substring from index of first underscore to end of string
        table_name = self.objectName()
        return table_name[table_name.index("_") + 1:]

    def get_solution_name(self):
        # substring from index of first underscore to end of string
        table_name = self.objectName()
        return table_name[:table_name.index("_")]

    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Resize:
            self.autofit()
        return super().eventFilter(object, event)

    def autofit(self):
        self.resizeColumnsToContents()
        # resize column 0 (ID) to fixed size of 70
        self.setColumnWidth(0, 70)
        # sum up the width of all columns
        width_sum = 0
        for i in range(self.columnCount()):
            width_sum += self.columnWidth(i)
        # get difference between the width of the table and the sum of the column widths
        difference = self.width() - width_sum
        if difference > 0:
            import math
            # calculate the increment for each column width, and subtract a small number (3) to prevent adding
            # horizontal scroll bar if possible
            column_increment = math.floor(difference / self.columnCount()) - 3
            # add the difference to each column width
            for i in range(self.columnCount()):
                self.setColumnWidth(i, self.columnWidth(i) + column_increment)
            current_width_sum = width_sum + (column_increment * self.columnCount())
            # subtract the difference from the last column width to prevent adding horizontal scroll bar if possible
            last_column_decrement = 25 - (self.width() - current_width_sum)
            self.setColumnWidth(self.columnCount() - 1,
                                self.columnWidth(self.columnCount() - 1) - last_column_decrement)
