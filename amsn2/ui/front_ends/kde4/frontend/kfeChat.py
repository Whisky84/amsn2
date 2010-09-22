# -*- coding: utf-8 -*-

from widgets import KFETextEditMod
from amsn2.ui.front_ends.kde4 import adaptationLayer

from amsn2.views    import *

from PyKDE4.kdeui   import *
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *

import sys
reload(sys)

class KFEChatWindow (adaptationLayer.KFEAbstractChatWindow, KMainWindow):
    def constructor(self, parent=None):
        print "PartiallyImplementedError:\tKFEChatWindow.constructor()"
        KMainWindow.__init__(self, parent)

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
        print "PartiallyImplementedError:\tKFEChatWindow.addChatWidget()"
        self.lay.addWidget(chatWidget)
        chatWidget.setStatusBar(self.sBar)

    def show(self):
        KMainWindow.show(self)
        
    def setMenu(self, menuBar):
        self.setMenuBar(menuBar)

    def setTitle(self, title):
        print "\t\t\t\tKFEChatWindow.setTitle()"
        self.setPlainCaption(title)



class KFEChatWidget (adaptationLayer.KFEAbstractChatWidget, QWidget):
    #TODO: We'll probably need a SIGNAL from the contact list model, to update the contact info here.
    def constructor(self, contacts_uid, parent=None):
        print "PartiallyImplementedError:\tKFEChatWidget.constructor()"
        self.statusBar = None
        QWidget.__init__(self, parent)


        label = QLabel(contacts_uid[0])

        topWidget = QWidget()
        topLay = QHBoxLayout()
        hisPicture = QLabel()
        self.chatText = QString("<i>New Chat</i><br>")
        self.chatView = KTextBrowser(None, True)
        self.chatView.setText(self.chatText)
        self.chatView.setText(self.chatText)
        topLay.addWidget(hisPicture)
        topLay.addWidget(self.chatView)
        topWidget.setLayout(topLay)

        bottomWidget = QWidget()
        bottomLay = QHBoxLayout()
        myPicture = QLabel()
        self.textEdit = KFETextEditMod()
        #self.textEdit.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.textEditBtn = KPushButton("Send")
        bottomLay.addWidget(myPicture)
        bottomLay.addWidget(self.textEdit)
        bottomLay.addWidget(self.textEditBtn)
        bottomWidget.setLayout(bottomLay)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(topWidget)
        splitter.addWidget(bottomWidget)

        lay = QVBoxLayout()
        lay.addWidget(label)
        lay.addWidget(splitter)
        self.setLayout(lay)

        splitter.setCollapsible (0, False)
        splitter.setCollapsible (1, False)
        _,splitterPos = splitter.getRange(1)
        splitter.moveSplitter(splitterPos,1)

        #model = self.parent()._core._ui_manager._contactlist.get_contactlist_widget().getModel()
        #index = model.getIndexByUid(contacts_uid[0])
        #if index is not None:
        #    hisPicture.setPixmap(model.data(QModelIndex(index,0,Qt.DecorationRole)))

        QObject.connect(self.textEditBtn, SIGNAL("clicked()"), self.onSendMessage)
        QObject.connect(self.textEdit, SIGNAL("returnPressed()"), self.onSendMessage)
        sys.setdefaultencoding("utf8")


    def onMessageReceived(self, messageview, formatting):
        """ Called for incoming and outgoing messages
            message: a MessageView of the message"""
        print "PartiallyImplementedError:\tKFEChatWidget.onMessageReceived() messageview =",
        print repr(messageview.msg)

        messageReceived = messageview.to_stringview().parse_default_smileys()
        print "-->" + repr(messageReceived)
        tempStr = QString("<br>")
        if formatting is not None:
            tempStr.append("<font face=\"%s\" color=\"#%s\">" % ( formatting.font, formatting.color ))


        tempStr.append(messageReceived.to_HTML_string())

        if formatting is not None:
            tempStr.append("</font>")
        tempStr.append("<br>")

        self.appendToChat(tempStr)
        

    def onUserJoined(self, nickname):
        print "\t\t\t\tKFEChatWidget.onUserJoined()"
        self.appendToChat("<i>%s has joined the chat </i>"%(unicode(nickname)))
        self.statusBar.insertItem("%s has joined the chat" % (nickname), 0)


    def onNudge(self):
        print "NotImplementedError:\t\tKFEChatWidget.OnNudge()"

    def onUserTyping(self, contact):
        print "\t\t\t\tKFEChatWidget.onUserTyping()"
        if self.statusBar.hasItem(1):
            self.statusBar.removeItem(1)
        self.statusBar.insertItem("%s is typing a message" % (contact), 1)
        self.statusBar.setItemAlignment(1, Qt.AlignLeft)


    # -------------------- QT_SLOTS

    def onSendMessage(self):
        messageString = str(self.textEdit.toPlainText())
        if len(messageString) == 0:
            return
        messageStringView = StringView()
        messageStringView.append_text(messageString)

        self.textEdit.setText("")
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
        


if __name__ == "__main__":
    about = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about)
    kapp = KApplication()
    w = KFEChatWindow(None)
    w.add_chat_widget(KFEChatWidget(None,w,"3"))
    w.show()
    kapp.exec_()
