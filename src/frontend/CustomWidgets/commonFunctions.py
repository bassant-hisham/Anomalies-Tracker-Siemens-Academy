from PyQt5.QtWidgets import *

def showFileDialog(self,line_edit):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self, "Choose File path", "", "All Files (*);;Text Files (*.txt)", options=options)

            if fileName:
                line_edit.setText(fileName)
                
def showDirectoryDialog(self,line_edit):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # Open directory dialog
        result = QFileDialog.getExistingDirectory(self, "Choose Directory", options=options)

        if result:
            line_edit.setText(result)