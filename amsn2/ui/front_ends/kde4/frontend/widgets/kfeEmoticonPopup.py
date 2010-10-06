# -*- coding: utf-8 -*-
from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog, KFEThemeManager
from amsn2.core.smiley_manager  import aMSNSmileyManager
from amsn2.core.theme_manager   import aMSNThemeManager

from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *

import math


class KFEEmoticonPopup (QDockWidget):
    fadeTime = 200
    remainingFadeTime = fadeTime
    emoticonSelected = pyqtSignal("QString")
    def __init__(self, parent=None):
        QDockWidget.__init__(self, parent, Qt.Popup)
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.fadeTimer = QTimer(self)
        self.fadeTimer.setSingleShot(False)
        themeManager = KFEThemeManager()
        # FIXME: Smiley manager's implementation will likely change heavily
        smileyDict = aMSNSmileyManager(None).default_smileys_shortcuts
        smileyButtonList = []
    
        for i in smileyDict.keys():
            icon = KIcon(QIcon(themeManager.pathOf(smileyDict[i])))
            button = SmileyButton(icon, smileyDict[i],  i)
            button.setFlat(True)
            w, h = button.size().width(), button.size().height()
            button.resize(min(w, h), min(w, h))
            button.selected.connect(self.onEmoticonSelected)
            smileyButtonList.append(button)
            
        #calculate dimensions:
        # constraints: x*y = len(smileyDict) = r AND  x/y = 1.6
        # which gives: y = sqrt(p/r) AND x = sqrt(r*p)
        p = len(smileyButtonList)
        self.y = math.ceil(math.sqrt(1.6 * p)) #numero di colonne
        self.x = p / self.y #numero di righe
        
        grid = QGridLayout()
        grid.setSpacing(0)
        counter = 0
        for i in range(self.x):
            for j in range(self.y):
                if counter >= p:
                    continue
                grid.addWidget(smileyButtonList[counter], i,  j)
                counter += 1

        centralWidget = QWidget()
        centralWidget.setLayout(grid)
        
        self.setWidget(QWidget())
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.setTitleBarWidget(centralWidget)
        
        self.timer.timeout.connect(self.fadeHide)
        self.fadeTimer.timeout.connect(self.fadeHide)
        
    def enterEvent(self, event):
        if self.timer.isActive():
            self.timer.stop()
        
    def leaveEvent(self, event):
        self.timer.start(750)
        
    def onEmoticonSelected(self, shortcut):
        self.hide()
        self.emoticonSelected.emit(shortcut)
        
    def show(self):
        pos = QCursor.pos()
        x = pos.x()
        y = pos.y()
        
        screenGeometry = KApplication.kApplication().desktop().screenGeometry()
        maxX = screenGeometry.width()
        maxY = screenGeometry.height()
        
        mySize = self.sizeHint()
        deltaX = mySize.width()
        deltaY = mySize.height()
        
        if (x + deltaX) > maxX:
            x = maxX - deltaX
        if (y + deltaY) > maxY:
            y = maxY - deltaY
        
        self.move(QPoint(x, y))
        QWidget.show(self)
    
    def fadeHide(self):
        opacity = self.windowOpacity()
        opacity -= 0.1
        
        if opacity > 0.2:
            self.setWindowOpacity(self.windowOpacity() - 0.1)
            if not self.fadeTimer.isActive():
                self.fadeTimer.start(self.fadeTime / 9)
        else:
            self.hide()
            self.setWindowOpacity(1)
            self.fadeTimer.stop()




class SmileyButton (KPushButton):
    selected = pyqtSignal("QString")
    def __init__(self, icon, tooltip, shortcut,  parent=None):
        KPushButton.__init__(self, icon, QString(), )
        self.setToolTip("<b>%s</b> %s" % (shortcut, tooltip) )
        self.shortcut = QString(shortcut)
        self.clicked.connect(self.__emitSignal)
        
    def __emitSignal(self):
        self.selected.emit(self.shortcut)
        
    def sizeHint(self):
        return QSize(25, 25)
