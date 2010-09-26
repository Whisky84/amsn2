# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import    KFEPresence,        \
                                                        KFEThemeManager
import papyon

from PyKDE4.kdeui   import  KComboBox

from PyKDE4.kdecore import  i18n

from PyQt4.QtGui    import  QIcon
from PyQt4.QtCore   import  *

#Maybe we need another class which makes presence info more abstract? (a Qt Delegate?! Does KComboBox support them?)
#TODO: put inizialization out of constructor, add setPresenceValues method.

class KFEPresenceCombo(KComboBox):
    presenceChanged = pyqtSignal(papyon.Presence)
    
    # is passing amsn_core the best solution?
    def __init__(self, parent = None):
        KComboBox.__init__(self, parent)
        
        #TODO: watch carefully for core changes :P
        self.presenceStrings = {}
        self.presenceValues = KFEPresence().presenceValues()
        
        for presenceKey in self.presenceValues:
            self.presenceStrings[presenceKey] = i18n( self.presenceValues[presenceKey].capitalize() )
        
        #presenceKey is of papyon.Presence type
        #presenceValue is a dumb string used by the core :P
        themeManager = KFEThemeManager()
        for presenceKey in self.presenceValues:
            if presenceKey == papyon.Presence.OFFLINE:
                continue
            presence = self.presenceValues[presenceKey]
            iconPath = themeManager.pathOf("buddy_%s" % presence)
            self.addItem(QIcon(iconPath), self.presenceStrings[presenceKey], presenceKey)
        
        self.setPresence(papyon.Presence.ONLINE)
        QObject.connect(self, SIGNAL("currentIndexChanged(int)"), self.onCurrentIndexChanged)
        
        
    def setPresence(self, presence):
        """Sets the presence in the KPresenceComboBox.
        
        @type presence: papyon.Presence
        @param presence: the presence to set
        """
        if presence is not papyon.Presence:
            pass
        KComboBox.setCurrentIndex(self,  self.findData(presence))
        
    def presence(self):
        #we don't say "getPresence" to make it more Qt-Stylish
        return str(self.itemData( self.currentIndex() ).toPyObject())
        
        
    # -------------------- QT_OVERLOAD
    
    def setCurrentIndex(self, index):
        print "Oh, boy.... what an ugly way to set the displayed presence!"
        print "Come on, use setPresence() instead! :("
        #the personalinfoview holds a string... so this is necessary...
        #maybe this will be removed in the future... I hope...
        KComboBox.setCurrentIndex(self, index)
        
        
    def onCurrentIndexChanged(index):
        presenceChanged.emit(self.presence())
        
