# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager

from amsn2.views import StringView
from amsn2.core.smiley_manager import aMSNSmileyManager

import papyon

from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *

import math
import os



class KFEChatTextEdit3(KTextEdit):
    returnPressed = pyqtSignal()
    fontChanged = pyqtSignal()
    def __init__(self, parent=None):
        KTextEdit.__init__(self, parent)
        self.__chatLineList = [""]
        self.__shownChatLine = 0

        self.__smileyDict = {}
        self.__reverseSmileyDict = {}
        self.__maxShortcutLength = 0

        self.__qtColor = QColor("#000000")



    def setSmileyDict(self, smileyDict):
        themeManager = KFEThemeManager()
        shortcuts = smileyDict.keys()
        #print "shortcuts: " + unicode(shortcuts)
        for shortcut in shortcuts:
            #print " -> %d[%s] : [%s]" % ( len(unicode(shortcut)), unicode(shortcut), unicode(smileyDict[shortcut]))
            path = themeManager.pathOf(smileyDict[shortcut])
            path = os.path.abspath(path)
            self.__smileyDict[unicode(shortcut.lower())] = unicode(path)
            self.__reverseSmileyDict[unicode(path)] = unicode(shortcut.lower())
            l = len(shortcut)
            if l > self.__maxShortcutLength:
                self.__maxShortcutLength = l


    def insertTextAfterCursor(self, text):
        text = unicode(text)
        for i in range(len(text)):
            # It's a little bit dirty, but seems to work....
            fakeEvent = QKeyEvent(QEvent.KeyPress, 0, Qt.NoModifier, text[i])
            self.keyPressEvent(fakeEvent)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            if event.modifiers() == Qt.ControlModifier:
                temp = QKeyEvent(QEvent.KeyPress,
                                 Qt.Key_Return,
                                 Qt.NoModifier,
                                 event.text(),
                                 event.isAutoRepeat(),
                                 event.count())
                event = temp
            else:
                self.returnPressed.emit()
                return
        if event.key() == Qt.Key_Up and event.modifiers() == Qt.ControlModifier:
            self.__swapToChatLine(self.__shownChatLine + 1)
            return
        if event.key() == Qt.Key_Down and event.modifiers() == Qt.ControlModifier:
            self.__swapToChatLine(self.__shownChatLine - 1)
            return
        if event.text().length() > 0:
            if self.__insertChar(event.text()):
                return
        KTextEdit.keyPressEvent(self, event)


    def toPlainText(self):
        parser = myHTMLParser(self.__reverseSmileyDict)
        parser.feed(self.toHtml())
        return parser.get_data()


    def __insertChar(self, c):
        # this method uses python's builtin string type, not QString
        cursor = self.textCursor()
        maxShortcutLength = self.__maxShortcutLength
        shortcuts = self.__smileyDict.keys()
        smileyFound = False

        textSearch = unicode(c).lower()
        i = 0
        while i < maxShortcutLength-1:
            # TODO: check if the returned QChar is valid
            lastChar = self.document().characterAt(cursor.position()-1-i).toLower()
            if lastChar.isPrint():
                lastChar = QString(lastChar)
                textSearch = unicode(lastChar) + textSearch
            i += 1
            #print "parsing",
            #print [textSearch],
            l = len(textSearch)
            #print " (%d)" % l
            if textSearch in shortcuts:
                #print "\t FOUND"
                for i in range(l-1):
                    cursor.deletePreviousChar()
                cursor.insertHtml('<img src="%s" />' % self.__smileyDict[textSearch])
                smileyFound = True
        #print "\t No smiley Found"
        return smileyFound


    def __swapToChatLine(self, idx):
        if idx < 0 or idx > len(self.__chatLineList)-1:
            #print "(%d) doing nothing" % idx
            return
        else:
            #print "switching to %d" % idx
            self.__chatLineList[self.__shownChatLine] = self.toHtml()
            KTextEdit.setHtml(self, self.__chatLineList[idx])
            cur = self.textCursor()
            cur.setPosition( self.document().characterCount()-1 )
            self.setTextCursor(cur)
            self.__shownChatLine = idx


    def clear(self):
        self.__chatLineList.insert(0, "")
        self.__shownChatLine += 1
        if len(self.__chatLineList) > 100:
            self.__chatLineList = self.__chatLineList[0:99]
        self.__swapToChatLine(0)


    def canInsertFromMimeData(self, source):
        if source.hasText():
            return True
        else:
            return False


    def insertFromMimeData(self, source):
        self.insertTextAfterCursor(source.text())


    def createMimeDataFromSelection(self):
        mimeData = KTextEdit.createMimeDataFromSelection(self)
        if mimeData.hasHtml():
            parser = myHTMLParser(self.__reverseSmileyDict)
            parser.feed(mimeData.html())
            mimeData.setText(parser.get_data())
        return mimeData


    def showFontStyleSelector(self):
        qtFont = self.defaultFont()
        result,_ = KFontDialog.getFont(qtFont)
        if result == KFontDialog.Accepted:
            print "accepted"
            self.setDefaultFont(qtFont)
        else:
            print "canceled"


    def defaultPapyonFont(self):
        qtFont = self.defaultFont()
        fo = unicode(qtFont.family())
        print "Font's raw Name: " + fo
        print qtFont.family()
        print qtFont.defaultFamily()
        st = papyon.TextFormat.NO_EFFECT
        if qtFont.bold():
            st |= papyon.TextFormat.BOLD
        if qtFont.italic():
            st |= papyon.TextFormat.ITALIC
        if qtFont.underline():
            st |= papyon.TextFormat.UNDERLINE
        if qtFont.overline():
            st |= papyon.TextFormat.STRIKETHROUGH
        fa = 0
        papyonFont = papyon.TextFormat(font=fo, style=st, color='0', family=fa)
        print qtFont.toString()
        print papyonFont
        return papyonFont

    def setDefaultFont(self, font):
        self.document().setDefaultFont(font)
        self.fontChanged.emit() ## TODO emit only if really changed

    def defaultFont(self):
        return self.document().defaultFont()

    def showFontColorSelector(self):
        qtColor = self.__qtColor
        result = KColorDialog.getColor(qtColor)
        if result == KColorDialog.Accepted:
            print "accepted"
            self.setDefaultColor(qtColor)
        else:
            print "canceled"

    def setDefaultColor(self, color):
        self.__qtColor = color
        self.setStyleSheet("QTextDocument{color: %s;} " % color.name() )
        print type(self.viewport())
        print str(self.viewport().objectName())
        self.fontChanged.emit() # TODO: view above

    def defaultColor(self):
        return self.__qtColor


from HTMLParser import HTMLParser
class myHTMLParser (HTMLParser):
    def __init__(self, reverseImgDict):
        HTMLParser.__init__(self)
        self.__reverseImgDict = reverseImgDict
        self.reset()

    def reset(self):
        HTMLParser.reset(self)
        self.__inBody = False
        self.__data = ""

    def feed(self, html_string):
        if isinstance(html_string, QString):
            html_string = unicode(html_string)
        HTMLParser.feed(self, html_string)

    def handle_starttag(self, tag, attrs):
        #print "TAG: %s, ATTRS: %s" % (tag, attrs)
        if self.__inBody:
            if tag == "body":
                raise NameError("Malformed HTML")
            if tag == "img":
                key = attrs[0][1]
                if key in self.__reverseImgDict.keys():
                    alt = self.__reverseImgDict[key]
                    self.__data += alt
                else:
                    raise NameError("Unrecognized Image")
        else:
            if tag == "body":
                self.__inBody = True

    def handle_endtag(self, tag):
        if self.__inBody:
            if tag == "body":
                self.__inBody = False

    def handle_data(self, data):
        #print "DATA :",
        #print data
        if self.__inBody:
            self.__data += data

    def get_data(self):
        # [1:] is to trim the leading line break.
        return self.__data[1:]





class KFEFont (QFont):
    def __init__(self):
        QFont.__init__(self)

    def fromString(self, description):
        print "KFEFont,fromString"
        QFont.fromString(description)

    def setBold(self, enable):
        print "KFEFont.setBold"
        QFont.setBold(self, enbale)

    def setCapitalization(self, caps):
        print "KFEFont.setCapitalization"
        QFont.setCapitalization(self, caps)

    def setFamily (self, family):
        print "KFEFont.setFamily"
        QFont.setFamily(self, family)

    def setFixedPitch (self, enable):
        print "KFEFont.setFixedPitch"
        QFont.setFixedPitch(self, enable)

    def setItalic(self, enable):
        print "KFEFont.setItalic"
        QFont.setItalic(self, enable)

    def setKerning (self, enable):
        print "KFEFont.setKerning"
        QFont.setKerning(self, enable)

    def setLetterSpacing (self, spacingType, spacing):
        print "KFEFont.setLetterSpacing"
        QFont.setLetterSpacing(self, spacingType, spacing)

    def setOverline (self, enable):
        print "KFEFont.setOverline"
        QFont.setOverline(self, enable)

    def setPixelSize (self, pixelSize):
        print "KFEFont.setPixelSize"
        QFont.setPixelSize(self, pixelSize)

    def setPointSize (self, pointSize):
        print "KFEFont.setPointSize"
        QFont.setPointSize(self, pointSize)

    def setPointSizeF (self, pointSize):
        print "KFEFont.setPointSizeF"
        QFont.setPointSizeF(self, pointSize)

    def setRawMode (self, enable):
        print "KFEFont.setRawMode"
        QFont.setRawMode(self, enable)

    def setRawName(self, name):
        print "KFEFont.setRawName"
        QFont.setRawName(self, name)

    def setStretch (self, factor):
        print "KFEFont.setStretch"
        QFont.setStretch(self, factor)

    def setStrikeOut (self, enable):
        print "KFEFont.setStrikeOut"
        QFont.setStrikeOut(self, enable)

    def setStyle (self, style):
        print "KFEFont.setStyle"
        QFont.setStyle(self, style)

    def setStyleHint (self, styleHint, styleStrategy=QFont.PreferDefault):
        print "KFEFont.setStyleHint"
        QFont.setStyleHint(self, styleHint, styleStrategy)

    def setStyleStrategy (self, styleStrategy):
        print "KFEFont.setStyleStrategy"
        QFont.setStyleStrategy(self, styleStrategy)

    def setUnderline (self, enable):
        print "KFEFont.setUnderline"
        QFont.setUnderline(self, enable)

    def setWeight (self, weight):
        print "KFEFont.setWeight"
        QFont.setWeight(self, weight)

    def setWordSpacing (self, spacing):
        print "KFEFont.setWordSpacing"
        QFont.setWordSpacing(self, spacing)













