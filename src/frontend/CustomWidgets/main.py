#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5 import QtWidgets
from src.frontend.CustomWidgets.mainwindow import MyMainWindow


# In[ ]:


#MAIN
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

