from src.frontend.CustomWidgets.UIs.ComodelsConfigBoxUI import Ui_ComodelsConfigBox
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class MyComodelsConfigGroupBox(QtWidgets.QGroupBox, Ui_ComodelsConfigBox):
    def __init__(self,id:int,comodelsList:list,comodelsLayout:QVBoxLayout):
        super(MyComodelsConfigGroupBox, self).__init__()
        self.setupUi(self)
        self.id=id
        self.setTitle("Config " + str(self.id))
        self.delete_pushButton.clicked.connect(self.deleteComdelsWidget)
        self.comodelsList=comodelsList
        self.comodelsLayout=comodelsLayout
        
    def deleteComdelsWidget(self):
        self.comodelsList.remove(self)
        self.comodelsLayout.removeWidget(self)
        self.deleteLater()
        
        for index,widget in enumerate(self.comodelsList):
            self.comodelsList[index].id=index+1
            self.comodelsList[index].setTitle("Config " + str(index+1))
