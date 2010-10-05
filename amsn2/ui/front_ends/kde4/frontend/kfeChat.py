# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import    KFELog,         \
                                                        KFEThemeManager

from widgets import KFEDisplayPic,      \
                    KFEEmoticonPopup,   \
                    KFETextEditMod
from amsn2.ui.front_ends.kde4 import adaptationLayer

from amsn2.views    import *

from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *

import sys
reload(sys)

class KFEChatWindow (adaptationLayer.KFEAbstractChatWindow, KMainWindow):
    def constructor(self, parent=None):
        KFELog().l("KFEChatWindow.constructor()")
        KMainWindow.__init__(self, parent)
        self.setObjectName("chatwindow#")
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.lay = QVBoxLayout()
        centralWidget.setLayout(self.lay)

        toolBar = KToolBar(self, True)
        toolBar.addAction( KAction("First Btn", self) )
        toolBar.addAction( KAction("Second Btn", self) )
        self.addToolBar(toolBar)

        self.sBar = self.statusBar()


    def addChatWidget(self, chatWidget):
        KFELog().l("KFEChatWindow.addChatWidget()", False, 1)
        self.lay.addWidget(chatWidget)
        chatWidget.setStatusBar(self.sBar)

    def show(self):
        KMainWindow.show(self)
        
    def setMenu(self, menuBar):
        self.setMenuBar(menuBar)

    def setTitle(self, title):
        KFELog().l("KFEChatWindow.setTitle()")
        self.setPlainCaption(title)



class KFEChatWidget (adaptationLayer.KFEAbstractChatWidget, QWidget):
    #TODO: We'll probably need a SIGNAL from the contact list model, to update the contact info here.
    def constructor(self, contacts_uid, parent=None):
        #KFELog().l("KFEChatWidget.constructor()", False, 1)
        self.statusBar = None
        themeManager = KFEThemeManager()
        QWidget.__init__(self, parent)


        label = QLabel(contacts_uid[0])
        # TOP LEFT
        topLeftWidget = QWidget()
        topLeftLay = QHBoxLayout()
        self.chatText = QString("<i>New Chat</i><br>")
        self.chatView = KTextBrowser(None, True)
        self.chatView.setText(self.chatText)
        self.chatView.setText(self.chatText)
        topLeftLay.addWidget(self.chatView)
        topLeftWidget.setLayout(topLeftLay)

        # BOTTOM LEFT
        bottomLeftWidget = QWidget()
        bottomLeftLay = QVBoxLayout()
        toolbar = KToolBar(self)
        self.smileyChooser = KFEEmoticonPopup()
        a = toolbar.addAction(KIcon(QIcon(themeManager.pathOf("button_smile"))), "Add Smiley")
        a.triggered.connect(self.onShowEmoticonChooser)
        toolbar.addAction(KIcon(QIcon(themeManager.pathOf("button_nudge"))), "Send Nudge")
        toolbar.addSeparator()
        toolbar.addAction(KIcon("preferences-desktop-fonts"), "Change Font")
        toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        #
        textEditLay = QHBoxLayout()
        self.textEditWidget = KFETextEditMod()
        self.textEditBtn = KPushButton("Send")
        textEditLay.addWidget(self.textEditWidget)
        textEditLay.addWidget(self.textEditBtn)
        #
        bottomLeftLay.addWidget(toolbar)
        bottomLeftLay.addLayout(textEditLay)
        bottomLeftWidget.setLayout(bottomLeftLay)
        
        # LEFT (TOP & BOTTOM)
        leftWidget = QSplitter(Qt.Vertical)
        leftWidget.addWidget(topLeftWidget)
        leftWidget.addWidget(bottomLeftWidget)

        leftLay = QVBoxLayout()
        leftLay.addWidget(label)
        leftLay.addWidget(leftWidget)

        leftWidget.setCollapsible (0, False)
        leftWidget.setCollapsible (1, False)
        _,splitterPos = leftWidget.getRange(1)
        leftWidget.moveSplitter(splitterPos,1)
        
        # RIGHT
        rightLay = QVBoxLayout()
        self.hisPicture = KFEDisplayPic()
        self.myPicture = KFEDisplayPic()
        rightLay.addWidget(self.hisPicture)
        rightLay.addStretch()
        rightLay.addWidget(self.myPicture)
        
        # LEFT & RIGHT
        lay = QHBoxLayout()
        lay.addLayout(leftLay)
        lay.addLayout(rightLay)
        self.setLayout(lay)

        #model = self.parent()._core._ui_manager._contactlist.get_contactlist_widget().getModel()
        #index = model.getIndexByUid(contacts_uid[0])
        #if index is not None:
        #    hisPicture.setPixmap(model.data(QModelIndex(index,0,Qt.DecorationRole)))

        QObject.connect(self.textEditBtn, SIGNAL("clicked()"), self.onSendMessage)
        QObject.connect(self.textEditWidget, SIGNAL("returnPressed()"), self.onSendMessage)
        self.smileyChooser.emoticonSelected.connect(self.onEmoticonSelected)
        sys.setdefaultencoding("utf8")
        
    def onShowEmoticonChooser(self):
        print "onShowEmoticonChooser"
        self.smileyChooser.show()
        

    def onEmoticonSelected(self, shortcut):
        # TODO: handle cursor position!
        self.textEditWidget.setText(self.textEditWidget.toPlainText() + shortcut)
    
    def onMessageReceived(self, messageview, formatting):
        """ Called for incoming and outgoing messages
            message: a MessageView of the message"""
        KFELog().l("KFEChatWidget.onMessageReceived()", False, 1)
        KFELog().d("messageview ="+repr(messageview.msg), "KFEChat.onMessageReceived()")

        messageReceived = messageview.to_stringview().parse_default_smileys()
        KFELog().d("-->" + repr(messageReceived))
        tempStr = QString("<br>")
        if formatting is not None:
            tempStr.append("<font face=\"%s\" color=\"#%s\">" % ( formatting.font, formatting.color ))


        tempStr.append(messageReceived.to_HTML_string())

        if formatting is not None:
            tempStr.append("</font>")
        tempStr.append("<br>")

        self.appendToChat(tempStr)
        

    def onUserJoined(self, nickname):
        KFELog().l("KFEChatWidget.onUserJoined()")
        self.appendToChat("<i>%s has joined the chat </i>"%(unicode(nickname)))
        self.statusBar.insertItem("%s has joined the chat" % (nickname), 0)


    def onNudge(self):
        KFELog().l("KFEChatWidget.OnNudge()",False, 2)

    def onUserTyping(self, contact):
        KFELog().l("KFEChatWidget.onUserTyping()", False, 1)
        if self.statusBar.hasItem(1):
            self.statusBar.removeItem(1)
        self.statusBar.insertItem("%s is typing a message" % (contact), 1)
        self.statusBar.setItemAlignment(1, Qt.AlignLeft)


    # -------------------- QT_SLOTS

    def onSendMessage(self):
        messageString = str(self.textEditWidget.toPlainText())
        if len(messageString) == 0:
            return
        messageStringView = StringView()
        messageStringView.append_text(messageString)

        self.textEditWidget.setText("")
        self.sendMessage(messageStringView)

    def appendToChat(self, htmlString):
        vertScrollBar = self.chatView.verticalScrollBar()
        if vertScrollBar.value() == vertScrollBar.maximum():
            atBottom = True
        else:
            atBottom = False
            
        self.chatText.append(htmlString)
        self.chatView.setText(self.chatText)

        if atBottom:
            vertScrollBar.setValue(vertScrollBar.maximum())

    def setStatusBar(self, statusBar):
        self.statusBar = statusBar
        
        
class emoticonButtonAction (KToolBarPopupAction):		
    def __init__(self, icon, text, parent):
        KToolBarPopupAction.__init__(self, icon, text, parent)
    def createWidget(self, parent):
        w = KToolBarPopupAction.createWidget(self, parent)
        l = QHBoxLayout()
        l.addWidget(QLabel("Ciao"))
        w.setLayout(l)
        return w
        


