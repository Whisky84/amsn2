# -*- coding: utf-8 -*-
from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager
from amsn2.core.smiley_manager  import aMSNSmileyManager
from amsn2.core.theme_manager   import aMSNThemeManager

from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *

import math


class KFEEmoticonPopup (QFrame):
    emoticonSelected = pyqtSignal("QString")
    def __init__(self, parent=None):
        QWidget.__init__(self, parent, Qt.Popup)
        themeManager = KFEThemeManager()
        # FIXME: Smiley manager's implementation will likely change heavily
        smileyDict = aMSNSmileyManager(None).default_smileys_shortcuts
        smileyKActionList = []
    
        for i in smileyDict.keys():
            icon = KIcon(QIcon(themeManager.pathOf(smileyDict[i])))
            action = KEmoticonAction(icon, "%s - %s" %(i, smileyDict[i]), i, self)
            action.selected.connect(self.onEmoticonSelected)
            smileyKActionList.append(action)
            
        #calculate dimensions:
        # consraints: x*y = len(smileyDict) = r AND  x/y = 1.6
        # which gives: y = sqrt(p/r) AND x = sqrt(r*p)
        p = len(smileyKActionList)
        y = math.ceil(math.sqrt(1.6 * p))
        x = p / y
        
        counter = 0
        bars = []
        for i in range(x):
            bar = KToolBar(self)
            for j in range(y):
                if counter >= p:
                    continue
                bar.addAction(smileyKActionList[counter])
                counter += 1
            bar.setToolButtonStyle(Qt.ToolButtonIconOnly)
            bar.setIconSize(QSize(16,16))
            bars.append(bar)
            
        lay = QVBoxLayout()
        for i in range(x):
            lay.addWidget(bars[i])
        self.setLayout(lay)
        
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        #self.setWindowFlags(Qt.SubWindow)
        
    def onEmoticonSelected(self, shortcut):
        self.hide()
        self.emoticonSelected.emit(shortcut)
        
    def show(self):
        pos = QCursor.pos()
        self.move(pos)
        QWidget.show(self)



class KEmoticonAction (KAction):
    selected = pyqtSignal("QString")
    def __init__(self, icon, text, shortcut, parent):
        KAction.__init__(self, icon, text, parent)
        self.shortcut = QString(shortcut)
        self.triggered.connect(self.__emitSignal)
        
    def __emitSignal(self):
        self.selected.emit(self.shortcut)
