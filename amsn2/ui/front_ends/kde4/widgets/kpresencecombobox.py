# -*- coding: utf-8 -*-

import papyon

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *


#Here we DO use camelCase, cause Qt uses it :)
#Maybe we need another class which makes presence info more abstract? (a Qt Delegate?! Does KComboBox support them?)


class KPresenceComboBox(KComboBox):
    # is passing amsn_core the best solution?
    def __init__(self, amsn_core, parent = None):
        KComboBox.__init__(self, parent)
        
        self._core = amsn_core
        
        #TODO: watch carefully for core changes :P
        self.presence_strings = {}
        self.presence_values = self._core.p2s
        
        for p_key in self.presence_values:
            self.presence_strings[p_key] = i18n( self.presence_values[p_key].capitalize() ) 
        
        #p_key is of papyon.Presence type
        #p_value is a dumb string used by the core :P
        for p_key in self._core.p2s:
            if p_key == papyon.Presence.OFFLINE:
                continue
            p_value = self._core.p2s[p_key]
            _, icon_path = self._core._theme_manager.get_value("buddy_%s" % p_value)
            self.addItem(QIcon(icon_path), self.presence_strings[p_key], p_key)
        
        self.setPresence(papyon.Presence.ONLINE)
        
        
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
        
