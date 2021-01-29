from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import platform
from PyQt5.uic import loadUiType
from PyQt5 import QtCore as QtCore
import datetime
import os
from title_bar import *



# Connect Ui With Main
ui,_  = loadUiType('ui_main.ui')
class MainApp (QMainWindow , ui):
    def __init__(self):
        super().__init__()
        QMainWindow().__init__(self)
        self.setupUi(self)
        self.__initUi()

    def __initUi (self):
        self.title_bar()
        
        
    def title_bar (self):

        titil = TitleBar.title_bar_custom(self)
        #Restore/Maximize window
        self.restor.clicked.connect(lambda: TitleBar.restore_or_maximize_window(self))
        # SET TITLE BAR
        self.titl.mouseMoveEvent =lambda event :TitleBar.moveWindow(self,event)
    def mousePressEvent(self, event):self.clickPosition = event.globalPos()    

        
    
        



def main ():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
    