# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer   import  KFEThemeManager

from PyQt4.QtGui        import *
from PyQt4.QtCore       import *


class KFEDisplayPic (QLabel):
    FRAMESIZE = QSize(104, 104)
    PIXMAPSIZE = QSize(96, 96)
    
    def __init__(self, parent = None):
        QLabel.__init__(self, parent)
        self.__clickable = True
        self.setFrameStyle(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        path = KFEThemeManager().pathOf("dp_amsn")
        self.setDisplayPic(path)
        self.installEventFilter( DisplayPicEventFilter(self) )
        
        
    def setDisplayPic(self, path):
        self.setPixmap(QPixmap(path).scaled(self.PIXMAPSIZE))
        self.adjustSize()
        
    def setClickable(self, clickable):
        self.__clickable = clickable
        
    def isClickable(self):
        return self.__clickable
        
    def adjustSize(self):
        self.setMinimumSize(self.FRAMESIZE)
        self.setMaximumSize(self.FRAMESIZE)
        
        
            
class DisplayPicEventFilter (QObject):
    def eventFilter(self, displayPic, event):
        if not isinstance(event, QMouseEvent):
            return False
        if not displayPic.isClickable():
            return False
        elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            displayPic.setFrameShadow(QFrame.Raised)
            displayPic.adjustSize()
            displayPic.emit(SIGNAL("clicked()"))
            return True
        elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            displayPic.setFrameShadow(QFrame.Sunken)
            displayPic.adjustSize()
            return True
        else:
            return False
        




