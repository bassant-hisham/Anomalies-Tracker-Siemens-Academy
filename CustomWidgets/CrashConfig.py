from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QCheckBox, QPushButton, QWidget, QComboBox, QLabel, QHBoxLayout

class CrashConfigWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Crash Configuration')

        layout = QVBoxLayout()

        # Create a QHBoxLayout for the label and combo box
        tool_layout = QHBoxLayout()
        tool_label = QLabel("Tool Name")
        self.tool_combo_box = QComboBox(self)
        self.tool_combo_box.addItems(["EPGM", "DPI", "Controller"])
        tool_layout.addWidget(tool_label)
        tool_layout.addWidget(self.tool_combo_box)
        layout.addLayout(tool_layout)

        # Create Checkboxes
        self.checkbox1 = QCheckBox('Attach GDB', self)
        # ... (other checkboxes)

       # Apply styles
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

        layout.addWidget(self.checkbox1)
       
        # Close button
        close_button = QPushButton('Done', self)
        close_button.clicked.connect(self.close)

        layout.addWidget(close_button)

        # Central widget setup
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_window(self):
        self.show()
