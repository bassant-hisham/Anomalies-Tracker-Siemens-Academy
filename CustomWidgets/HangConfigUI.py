from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QRadioButton, QPushButton, QWidget,QButtonGroup
from PyQt5.QtCore import Qt

class HangConfigWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Hang Configuration')

        layout = QVBoxLayout()

        # Create Checkboxes
        self.radiobutton1 = QRadioButton('EPGM', self)
        self.radiobutton2 = QRadioButton('Controller', self)
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radiobutton1)
        self.button_group.addButton(self.radiobutton2)
        # Apply styles
        self.setStyleSheet(
            """
            QMainWindow {
                border-radius: 15px;
                background-color: rgb(37, 40, 50);
            }
            QRadioButton {
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
            """
        )

        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)

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
