from main import *

WINDOW_SIZE = 0;
class TitleBar (MainApp):
    def moveWindow(self,event):
        # IF LEFT CLICK MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()        
    
    def title_bar_custom(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        # Appy shadow to central widget
        self.centralwidget.setGraphicsEffect(self.shadow)

        
        # Button click events to our top bar buttons
        # 
        #Minimize window
        self.hideBtn.clicked.connect(lambda: self.showMinimized())
        #Close window
        self.closeBtn.clicked.connect(lambda: self.close())

         # MOVE WINDOW
        

    # Restore or maximize your window
    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE #The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1 #Update value to show that the window has been maxmized
            self.showMaximized()
            self.horizontalLayout.setContentsMargins(0,0,0,0)
            

        else:
            # If the window is on its default size
            WINDOW_SIZE = 0
            self.showNormal()
           

       