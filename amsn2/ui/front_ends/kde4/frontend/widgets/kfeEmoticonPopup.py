# -*- coding: utf-8 -*-
from amsn2.core.adaptationLayer import KFEThemeManager
from amsn2.core.smiley_manager  import aMSNSmileyManager
from amsn2.core.theme_manager   import aMSNThemeManager


class KFEEmoticonPopup (QWidget):
    emoticonSelected = pyqtSignal("QString")
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        themeManager = KFEThemeManager()
        # FIXME: Smiley manager's implementation will likely change heavily
        smileyDict = aMSNSmileyManager().default_smileys_shortcuts()
        smileyKActionList = []
        for i in smileyList.keys():
            icon = KIcon(QIcon(themeManager.pathOf(smileyDict[i])))
            action = KAction(icon, i, self)
            self.emoticonSelected.connect(self.emoticonSelected)
            
            
            



class KActionMod (KAction):
    selected = pyqtSignal("QString")
    def __init__(self, icon, text, parent):
        KAction.__init__(self, icon, text, parent)
        self.text = QString(text)
        self.triggered.connect(self.__emit_signal)
        
    def __emitSignal(self):
        self.selected.emit(text)
