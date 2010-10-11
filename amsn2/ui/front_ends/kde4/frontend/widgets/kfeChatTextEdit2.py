# -*- coding: utf-8 -*-

from amsn2.views import StringView
from amsn2.core.smiley_manager import aMSNSmileyManager

from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *




#class KFEChatTextEdit (Widget):
#    def __init__(self, parent=None):
#        QWidget.__init__(self, parent)
#        self.view = KTextEdit()
#        self.view.installEventFilter(self)
#        self.text = QString("")
#        self.debug = QTextEdit()
#        self.debug.setReadOnly(True)
#        
#        self.view.setHtml('<img src="/home/fastfading/src/amsn2/amsn2/themes/smileys/default/angel.png" alt="(A)">')
#        print unicode(self.view.toPlainText())
#        
#        
#        lay = QHBoxLayout()
#        lay.addWidget(self.view)
#        lay.addWidget(self.debug)
#        self.setLayout(lay)
#        
#    def eventFilter(self, obj, event):
#        if (not obj == self.view):
#            return False
#        if (not event.type() == QEvent.KeyPress): #and (not event.type() == QEvent.KeyRelease):
#            return False
#    
#        key = event.key()
#        if key in specialKeys.keys():
#            self.appendSpecialChar(key)
#            return True
#            
#        return False
#            
#            
#    def appendSpecialChar(self, key):
#        self.saveCursor()
#        self.text.append(specialKeys[key])
#        self.updateText()
#        self.restoreAndMoveCursor(+1, QTextCursor.MoveAnchor)
#        
#    def updateText(self):
#        self.view.setHtml(self.text)
#        self.debug.setPlainText(self.text)
#        
#        
#        
#    def saveCursor(self):
#        self.savedCursor = self.view.textCursor()
#    def restoreAndMoveCursor(self, steps, moveMode):
#        if steps >= 0:
#            moveOperation = QTextCursor.NextCharacter
#        else:
#            moveOperation = QTextCursor.PreviousCharacter
#            steps = -steps
#        newCursor = self.view.textCursor()
#        newCursor.setPosition(self.savedCursor.position())
#        newCursor.movePosition(moveOperation, moveMode, steps)
#        self.view.setTextCursor(newCursor)

class KFEChatTextEdit2(QScrollArea):
    def __init__(self, parent=None):
        QScrollArea.__init__(self, parent)
        self.setWidget(KFEChatTextEditViewport())
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

class KFEChatTextEditViewport (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.doc = QTextDocument()
        self.cur = QTextCursor(self.doc)
        
        self.installEventFilter(self)
        
    def paintEvent(self, event):
        print "PAINT"
        painter = QStylePainter()
        # set this widget as the painter's QPaintDevice:
        painter.begin(self) 
        painter.setClipRect(event.rect())
        painter.setClipping(False)
        
        option = QStyleOptionFrameV3()
        option.init(self)
        option.features = QStyleOptionFrameV2.None
        option.frameShape = QFrame.StyledPanel
        painter.drawPrimitive(QStyle.PE_PanelLineEdit, option)

        self.doc.setTextWidth(event.rect().size().width())
        self.doc.adjustSize()
        paintContext = QAbstractTextDocumentLayout.PaintContext()
        
        paintContext.clip = QRectF(event.rect())
        paintContext.cursorPosition = self.cur.position()
        self.doc.documentLayout().draw(painter, paintContext)
        
        painter.end()
        
    def sizeHint(self):
        self.doc.setTextWidth(self.parent().size().width())
        print "sizehisnt: %s" % self.doc.size()
        return self.doc.size().toSize()
#        
#    def minimumHeight
#
#    def sizeHint(self):
        
        
    def eventFilter(self, obj, event):
        type = event.type()
        if (type == QEvent.KeyPress):
            print "key pressed!!!"
            return False
        else:
            return False
            
    def keyPressEvent(self, event):
        key = event.key()
        needsUpdating = False
        # TODO: handle strange charachters and IMEs (;__;)
        if ((Qt.Key_A <= key and key <= Qt.Key_Z) or
            (Qt.Key_0 <= key and key <= Qt.Key_9)):
                # TODO: Handle text insertion (we have to parse emoticons
                self.cur.insertText(event.text())
                needsUpdating = True
        if key == Qt.Key_Space:
            self.cur.insertHtml(QString("&nbsp;"))
            needsUpdating = True
        if key == Qt.Key_Backspace:
            # TODO: handle text deletion
            self.cur.deletePreviousChar()
            needsUpdating = True
            
        if needsUpdating:
            self.update()
            
    
    
            
        
        
specialKeys = { Qt.Key_Space        : "&nbsp;",
                Qt.Key_Ampersand    : "&amp;" }
                
                
                
