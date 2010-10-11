# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager

from amsn2.views import StringView
from amsn2.core.smiley_manager import aMSNSmileyManager

from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *



class KFEChatTextEdit3(KTextEdit):
    # TODO:
    # - create plain text from parent's HTML
    # - handle clipboard
    # - handle drag & drop
   
    def __init__(self, parent=None):
        KTextEdit.__init__(self, parent)
        #self.installEventFilter(self)
        
        self.cur = self.textCursor() # mmmh
        self.setTextCursor(self.cur)
        self.doc = self.cur.document()
        self.__smileyDict = {}
        self.smileyLengths = []
        

    def eventFilter(self, obj, event):
        type = event.type()
        if (type == QEvent.KeyPress):
            return False
        else:
            return False
            
    def setSmileyDict(self, smileyDict):
        shortcuts = smileyDict.keys()
        for shortcut in shortcuts:
            self.__smileyDict[QString(shortcut)] = smileyDict[shortcut]
            l = len(shortcut)
            if l not in self.smileyLengths:
                self.smileyLengths.append(l)
        self.smileyLengths.sort()
        print self.smileyLengths
        
        
    def smileyDict(self):
        return self.__smileyDict
            
    def keyPressEvent(self, event):
        # rewrite trying to use python's builtin types.....
        themeManager = KFEThemeManager()
        cursor = self.textCursor()
        searchText = event.text()
        if len(self.smileyLengths) > 0:
            for i in range(max(self.smileyLengths) ):
                searchText.prepend(self.doc.characterAt(cursor.position()-i) )
            print "Controllo in: [%s]" % searchText
            for l in self.smileyLengths:
                print "\t [%s]" % searchText.mid(searchText.length()-l-1, searchText.length())
                if searchText.mid(searchText.length()-l-1, searchText.length()) in self.__smileyDict.keys():
                    path = themeManager.pathOf(str(self.__smileyDict[searchText[l:]]))
                    cursor.insertHtml('<img src="%s" alt="%s">' % (path, searchText[l:]) )
                    return
        KTextEdit.keyPressEvent(self, event)
            
    def toPlainText(self):
        # TODO: reimplement
        return self.toPlainText()
        
        
specialKeys = { Qt.Key_Space        : "&nbsp;",
                Qt.Key_Ampersand    : "&amp;" }
                
                
                
