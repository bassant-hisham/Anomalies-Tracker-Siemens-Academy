from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QCheckBox, QPushButton, QWidget, QComboBox, QLabel, QHBoxLayout,QDesktopWidget
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint

class CrashConfigWindow(QMainWindow):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CrashConfig')

        layout = QVBoxLayout()

        # Create a QHBoxLayout for the label and combo box
        tool_layout = QHBoxLayout()
        tool_label = QLabel("Tool Name")
        self.tool_combo_box = QComboBox(self)
        self.tool_combo_box.addItems(["EPGM", "DPI", "Controller"])
        tool_layout.addWidget(tool_label)
        tool_layout.addWidget(self.tool_combo_box)
        self.verticalSpacer=QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(self.verticalSpacer)
        layout.addLayout(tool_layout)
        layout.addItem(self.verticalSpacer)


        # self.parent = parent

        # Create Checkboxes
        self.checkbox1 = QCheckBox('Attach GDB', self)
        # ... (other checkboxes)

       # Apply styles
       
        layout.addWidget(self.checkbox1)
        layout.addItem(self.verticalSpacer)

       
        # Close button
        self.close_button = QPushButton('Done', self)
        self.close_button.clicked.connect(self.close)
        self.closebtnLayout=QtWidgets.QHBoxLayout()
        self.HorizontalSpacer=QtWidgets.QSpacerItem(55, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.closebtnLayout.addItem(self.HorizontalSpacer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        self.close_button.setSizePolicy(sizePolicy)
        self.closebtnLayout.addWidget(self.close_button)
        self.closebtnLayout.addItem(self.HorizontalSpacer)
        layout.addLayout(self.closebtnLayout)

        # Central widget setup
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setMinimumSize(300, 200)
        self.setStyleSheet(
            """
        QMainWindow {
            border-radius: 15px;
            background-color: rgb(37, 40, 50);
        }
        QCheckBox {
            color: rgb(255, 255, 255);
            font-size: 11pt;
        }
        QPushButton {
	    background-color: rgb(33, 188, 180);
        color:rgb(255, 255, 255);
        border-radius: 10px;
        font:18px;
        font-weight:bold;
        }

        QPushButton:hover {
            background-color: rgb(84, 195, 195);
        }

        QPushButton:pressed {
            background-color: rgb(25, 154, 147);
        }

        QPushButton:disabled {
            background-color: rgb(180, 180, 180);
            color: rgb(100, 100, 100);
        }
        QComboBox {
            background-color: rgb(52, 59, 72);
            border: 1px solid rgb(49, 54, 65);
            height: 30px;
            border-radius: 10px;
            padding-left: 10px;
            padding-right: 15px;
            color: rgb(255, 255, 255);
        }
        QComboBox QAbstractItemView {
            background-color:rgb(27, 29, 35);
            border: 0px;
            color: #fff;
            selection-background-color: rgb(22, 51, 79);
            outline: none;
        }
        QComboBox QAbstractItemView::item:selected {
            background-color: rgb(22, 51, 79);
        }
        QComboBox:on {
            border: 0px solid rgb(61, 70, 86);
            background-color: rgb(57, 65, 80)
        }
        QComboBox QListView {
            background-color: rgb(27, 29, 35);
            border-radius: 10px;
            color: #FFF;
            padding: 10px;
        }
        QComboBox:disabled {
            background-color: #808080;
        }
        /* Label */
        QLabel{
            color: rgb(255, 255, 255);
            font-size: 11pt;

        }
        QLineEdit{
            border: 0px solid rgb(37, 39, 48);
            height: 30px;
            border-radius: 15px;
            color: white;
            padding-left: 20px;
            padding-right: 20px;
            background-color: rgb(27, 29, 35);
        }
        QLineEdit:hover{
            border: 2px solid rgb(64, 71, 88)
        }
        QLineEdit:focus{
            border: 3px solid rgb(91, 101, 124);
            color: white;
        }
        QLineEdit:disabled {
            background-color: #808080;
        }
                    """
        )

    def center_on_parent(self):       
        screen = QDesktopWidget().screenGeometry()
        center_x = screen.width() // 2  
        center_y = screen.height() // 2
        popup_geometry = self.frameGeometry()
        popup_geometry.moveCenter(QPoint(center_x, center_y))
        self.move(popup_geometry.topLeft())

    def show_window(self):
        self.show()
        
    def closeEvent(self, event):
        self.closed_signal.emit()
        event.accept()
