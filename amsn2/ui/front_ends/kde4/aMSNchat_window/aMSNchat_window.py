# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.widgets import KTextEditMod

from amsn2.ui import base

from amsn2.views import StringView


from PyKDE4.kdeui import KAction, \
                         KMainWindow, \
                         KTextBrowser, \
                         KToolBar, \
                         KPushButton
                         

from PyQt4.QtGui import QHBoxLayout, \
                        QLabel, \
                        QVBoxLayout, \
                        QSplitter, \
                        QWidget
                        
from PyQt4.QtCore import QObject, \
                         QString, \
                         Qt, \
                         SIGNAL


import sys
reload(sys)


#test main:
from PyKDE4.kdecore import KAboutData, \
                           KCmdLineArgs, \
                           ki18n

from PyKDE4.kdeui import KApplication
                         



class aMSNChatWindow(base.aMSNChatWindow, KMainWindow):
    """ This interface will represent a chat window of the UI
        It can have many aMSNChatWidgets"""
    def __init__(self, amsn_core, parent = None):
        print "PartiallyImplementedError:\taMSNChatWindow.__init__()"
        KMainWindow.__init__(self, parent)

        self._core = amsn_core
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.lay = QVBoxLayout()
        centralWidget.setLayout(self.lay)

        toolBar = KToolBar(self, True)
        toolBar.addAction( KAction("First Btn", self) )
        toolBar.addAction( KAction("Second Btn", self) )
        self.addToolBar(toolBar)
        
    def add_chat_widget(self, chat_widget):
        """ add an aMSNChatWidget to the window """
        print "PartiallyImplementedError:\taMSNChatWindow.add_chat_widget()"
        self.lay.addWidget(chat_widget)
    """TODO: move, remove, detach, attach (shouldn't we use add ?), close,
        flash..."""

    #TODO: this is copy-pasted from aMSNmain_window.py..... REFACTOR!
    def show(self):
        print "\t\t\t\taMSNChatWindow.show()"
        KMainWindow.show(self)


    def hide(self):
        print "\t\t\t\taMSNChatWindow.hide()"
        KMainWindow.hide(self)


    def set_title(self,title):
        print "\t\t\t\taMSNChatWindow.set_title()"
        self.setPlainCaption(title)


    def set_menu(self,menu):
        print "PartiallyImplementedError:\taMSNChatWindow.set_menu()"
        menu_bar = KMenuBar()
        #FIXME: REFACTOR THIS **CRAP**
        for i in menu.items:
            if i.type == MenuItemView.CASCADE_MENU:
                k_menu = menu_bar.addMenu(i.label)
                for j in i.items:
                    if j.label == "Log out":
                        k_action = k_menu.addAction(j.label)
                        QObject.connect(k_action, SIGNAL("triggered()"), self._core.sign_out_of_account)
                    else:
                        k_menu.addAction(j.label + " (!)")
        menu_bar.addMenu(self.helpMenu())
        self.setMenuBar(menu_bar)
    

class aMSNChatWidget(base.aMSNChatWidget, QWidget):
    """ This interface will present a chat widget of the UI """
    #TODO: We'll probably need a SIGNAL from the contact list model, to update the contact info here.
    def __init__(self, amsn_conversation, parent, contacts_uid):
        """ create the chat widget for the 'parent' window, but don't attach to
        it."""
        print "PartiallyImplementedError:\taMSNChatWidget.__init__()"
        QWidget.__init__(self, parent)

        self._amsn_conversation = amsn_conversation

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
        self.textEdit = KTextEditMod()
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
        
        QObject.connect(self.textEditBtn, SIGNAL("clicked()"), self.qslotSendMessage)
        QObject.connect(self.textEdit, SIGNAL("returnPressed()"), self.qslotSendMessage)
        sys.setdefaultencoding("utf8")
        
        
    def on_message_received(self, messageview, formatting):
        """ Called for incoming and outgoing messages
            message: a MessageView of the message"""
        print "PartiallyImplementedError:\taMSNChatWidget.on_message_received() messageview =",
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

        vertScrollBar = self.chatView.verticalScrollBar()
        if vertScrollBar.value() == vertScrollBar.maximum():
            atBottom = True
        else:
            atBottom = False
        
        self.chatText.append(tempStr)
        self.chatView.setText(self.chatText)

        if atBottom:
            vertScrollBar.setValue(vertScrollBar.maximum())

    def on_user_joined(self, nickname):
        print "\t\t\t\taMSNChatWidget.on_user_joined()"
        

    def nudge(self):
        print "NotImplementedError:\t\taMSNChatWidget.nudge()"

    def on_user_typing(self, contact):
        print "NotImplementedError:\t\taMSNChatWidget.on_user_typing()"


    # -------------------- QT_SLOTS

    def qslotSendMessage(self):
        messageString = str(self.textEdit.toPlainText())
        if len(messageString) == 0:
            return
        messageStringView = StringView()
        messageStringView.append_text(messageString)

        self.textEdit.setText("")
        self._amsn_conversation.send_message(messageStringView)


if __name__ == "__main__":
    about = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about)
    kapp = KApplication()
    w = aMSNChatWindow(None)
    w.add_chat_widget(aMSNChatWidget(None,w,"3"))
    w.show()
    kapp.exec_()


    