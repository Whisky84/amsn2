# -*- coding: utf-8 -*-

from amsn2.views import StringView
from amsn2.core.smiley_manager import aMSNSmileyManager
from PyKDE4.kdeui import KTextEdit


from PyQt4.QtGui import *
from PyQt4.QtCore import *


class KFEChatTextEditStacked (QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)
        self.__w = KFEChatTextEdit()
        self.addWidget(self.__w)
        self.addWidget(self.__w.child)
        self.__w.child.setWindowOpacity(0)
        self.layout().setStackingMode(QStackedLayout.StackAll)
    def getWidget(self):
        return self.__w


class KFEChatTextEdit (KTextEdit):
    # TODO LIST:+
    # o keyboard editing, including selection
    # o mouse editing, including selection
    # + emoticon handling, (breaks the 2 formers)
    # - whitespace handling
    # - copy / paste handling
    # - drag / drop handling
    def __init__(self, parent = None):
        KTextEdit.__init__(self, parent)
        
        self.child = KTextEdit()
        self.child.setStyleSheet("QTextEdit{ background-color: rgb(178, 216, 255);}" )
        self.ReturnPressed = False
        self.positionSkip = {}
        self.oldP = 0
        self.assumeGood = 0
        
        self.child.textChanged.connect(self.onChildTextCanged)
        self.child.cursorPositionChanged.connect(self.onChildCursorPositionChanged)
        self.child.selectionChanged.connect(self.onChildSelectionChanged)
        

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            self.assumeGood = False
            if keyEvent.modifiers() == Qt.ControlModifier:
                keyEvent.accept()
                fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_Return, Qt.NoModifier)
                KTextEdit.keyPressEvent(self.child, fakeEvent)
            elif keyEvent.modifiers() == Qt.NoModifier:
                keyEvent.accept()
                self.ReturnPressed = True
            else:
                KTextEdit.keyPressEvent(self.child, keyEvent)
        elif keyEvent.key() == Qt.Key_Backspace:
            self.assumeGood = True
            KTextEdit.keyPressEvent(self.child, keyEvent)
        elif keyEvent.key() == Qt.Key_Space:
            fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_Ampersand, Qt.NoModifier)
            KTextEdit.keyPressEvent(self.child, fakeEvent)
            fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_N, Qt.NoModifier)
            KTextEdit.keyPressEvent(self.child, fakeEvent)
            fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_B, Qt.NoModifier)
            KTextEdit.keyPressEvent(self.child, fakeEvent)
            fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_S, Qt.NoModifier)
            KTextEdit.keyPressEvent(self.child, fakeEvent)
            fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_P, Qt.NoModifier)
            KTextEdit.keyPressEvent(self.child, fakeEvent)
            fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_Colon, Qt.NoModifier)
            KTextEdit.keyPressEvent(self.child, fakeEvent)
        else:
            self.assumeGood = False
            KTextEdit.keyPressEvent(self.child, keyEvent)


    def keyReleaseEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            if keyEvent.modifiers() == Qt.ControlModifier:
                keyEvent.accept()
                fakeEvent = QKeyEvent(QEvent.KeyRelease, Qt.Key_Return, Qt.NoModifier)
                KTextEdit.keyReleaseEvent(self.child, fakeEvent)
            elif keyEvent.modifiers() == Qt.NoModifier:
                if not self.ReturnPressed:
                    print "DEBUG:\t\t\t\tKTextEditMod.keyReleaseEvent(): There's some problem!"
                keyEvent.accept()
                self.ReturnPressed = False
                self.emit(SIGNAL("returnPressed()"))
            else:
                KTextEdit.keyReleaseEvent(self.child, keyEvent)
        else:
            KTextEdit.keyReleaseEvent(self.child, keyEvent)
            
    def mousePressEvent(self, mouseEvent):
        KTextEdit.mousePressEvent(self.child, mouseEvent)
    def mouseMoveEvent(self, mouseEvent):
        KTextEdit.mouseMoveEvent(self.child, mouseEvent)
    def mouseReleaseEvent(self, mouseEvent):
        KTextEdit.mouseReleaseEvent(self.child, mouseEvent)
        
    def insertTextAfterCursor(self, text):
        self.child.textCursor().insertText(text)
        
    def onChildTextCanged(self):
        # maybe this would be more efficient if done in the eventfilter, char by char
        text = self.child.toPlainText()
        smileyDict = aMSNSmileyManager(None).default_smileys_shortcuts
        foundSmileyDict = {}
        for shortcut in smileyDict.keys():
            idx = text.indexOf(shortcut, 0, Qt.CaseInsensitive)
            while not idx ==- 1 :
                if not shortcut in foundSmileyDict:
                    foundSmileyDict[shortcut] = []
                foundSmileyDict[shortcut].append(idx)
                idx = text.indexOf(shortcut, idx+1, Qt.CaseInsensitive)
        print str(foundSmileyDict),
        
        # list of found smileys ordered by position:
        orderedSmileyDict = {}
        for smiley in foundSmileyDict:
            list = foundSmileyDict[smiley]
            for position in list:
                orderedSmileyDict[position] = smiley
        print orderedSmileyDict
        
        self.positionSkip = {}
        proxyText = ""
        text = unicode(text)
        oldPosition = 0
        positionsList = orderedSmileyDict.keys()
        positionsList.sort()
        for position in positionsList:
            smiley = orderedSmileyDict[position]
            l = len(smiley)
            proxyText += text[oldPosition:position]
            sw = StringView()
            sw.append_text(text[position:position+l])
            sw = sw.parse_default_smileys()
            proxyText += sw.to_HTML_string()
            self.positionSkip[position] = l
            oldPosition = position + l
        proxyText += text[oldPosition:] 
        print proxyText
        print self.positionSkip
                
        KTextEdit.setHtml(self, proxyText)
        self.onChildCursorPositionChanged()
        
    def onChildCursorPositionChanged(self):
        # here we have to check first if the child's cursor is in the middle of an
        # emoticon shortcut, and correct the position.
        childCursor = self.child.textCursor()
        p = childCursor.position()
        
        goodPosition = False
        currentGoodP = 0
        nextGoodP = 0
        if self.assumeGood or p == 0:
            goodPosition = True
        while nextGoodP < p:
            currentGoodP = nextGoodP
            if nextGoodP in self.positionSkip:
                nextGoodP += self.positionSkip[nextGoodP]
            else:
                nextGoodP += 1
            if nextGoodP == p:
                goodPosition = True
        print "Good Position: %d || %d -> (%d, %d)" % (goodPosition, p, currentGoodP, nextGoodP)
        
        if not goodPosition:
            if p > self.oldP:
                p = nextGoodP
            else:
                p = currentGoodP
            newChildCursor = self.child.textCursor()
            newChildCursor.setPosition(p)
            self.child.setTextCursor(newChildCursor)
            return
        
        
        
        newCursor = self.textCursor()
        lastP = newCursor.currentFrame().lastPosition()
        p_ = self.c2p(p)
        if p_ > lastP:
            return
        newCursor.setPosition(p_)
        self.setTextCursor(newCursor)
        self.oldP = p
        
    def onChildSelectionChanged(self):
        childCursor = self.child.textCursor()
        a = childCursor.selectionStart()
        b = childCursor.selectionEnd()
        newCursor = self.textCursor()
        newCursor.setPosition(a)
        newCursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor, b-a)
        self.setTextCursor(newCursor)
        
    def c2p(self, pos):
        proxyPos = 0
        childPos = 0
        while childPos < pos:
            if childPos in self.positionSkip:
                childPos += self.positionSkip[childPos]
            else:
                childPos += 1
            proxyPos += 1
        print "proxyPos: %d -> %d" % (pos,proxyPos)
        return proxyPos
        
    def proxyCursorLastPosition(self):
        proxyCursor = self.textCursor()
        lastP = proxyCursor.currentFrame().lastPosition()
        for position in self.positionSkip:
            lastP = lastP - self.positionSkip[position] + 1
        return lastP
            
    def toPlainText(self):
        #TODO: stripping, maybe unnecessary
        return self.child.toPlainText()
        
    def setPlainText(self, text):
        self.child.setPlainText(text)
        
    
            


