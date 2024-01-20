from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QRadioButton, QPushButton, QWidget,QButtonGroup,QDesktopWidget
from PyQt5.QtCore import Qt,QPoint
from PyQt5 import QtWidgets, QtCore

class HangConfigWindow(QMainWindow):
    closed_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HangConfig')

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
                border: 0px solid rgb(52, 59, 72);
                background-color: rgb(33, 188, 180);
                color:rgb(255, 255, 255);
                border-radius: 50px;
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
        self.setMinimumSize(300, 200)

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