# -*- coding: utf-8 -*-

from amsn2.ui import base

from amsn2.views import MessageView, \
                        StringView

from PyKDE4.kdeui import KMainWindow, \
                         KToolBar, \
                         KAction, \
                         KTextBrowser, \
                         KPushButton, \
                         KLineEdit

from PyQt4.QtGui import QWidget, \
                        QVBoxLayout, \
                        QHBoxLayout, \
                        QLabel, \
                        QSplitter
                        
from PyQt4.QtCore import QObject, \
                         QString, \
                         Qt, \
                         SIGNAL

#test main:
from PyKDE4.kdecore import KAboutData, \
                           KCmdLineArgs, \
                           ki18n

from PyKDE4.kdeui import KApplication
                         

import sys

class aMSNChatWindow(base.aMSNChatWindow, KMainWindow):
    """ This interface will represent a chat window of the UI
        It can have many aMSNChatWidgets"""
    def __init__(self, amsn_core, parent = None):
        print "PartiallyImplementedError:\taMSNChatWindow.__init__()"
        KMainWindow.__init__(self, parent)
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
    def __init__(self, amsn_conversation, parent, contacts_uid):
        """ create the chat widget for the 'parent' window, but don't attach to
        it."""
        print "PartiallyImplementedError:\taMSNChatWidget.__init__()"
        QWidget.__init__(self, parent)

        self._amsn_conversation = amsn_conversation

        label = QLabel(contacts_uid[0])
        
        self.chatText = QString("<i>New Chat</i><br>Go!")
        self.chatView = KTextBrowser(None, True)
        self.chatView.setText(self.chatText)
        self.chatText.append("<img src=\"/home/fastfading/Immagini/schro.jpeg\">")
        self.chatView.setText(self.chatText)

        bottomWidget = QWidget()
        editLay = QHBoxLayout()
        self.lineEdit = KLineEdit()
        self.lineEditBtn = KPushButton("Send")
        editLay.addWidget(self.lineEdit)
        editLay.addWidget(self.lineEditBtn)
        bottomWidget.setLayout(editLay)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.chatView)
        splitter.addWidget(bottomWidget)

        lay = QVBoxLayout()
        lay.addWidget(label)
        lay.addWidget(splitter)
        self.setLayout(lay)

        QObject.connect(self.lineEditBtn, SIGNAL("clicked()"), self.qslotSendMessage)
        QObject.connect(self.lineEdit, SIGNAL("returnPressed()"), self.qslotSendMessage)

        
        
    def on_message_received(self, messageview, formatting):
        """ Called for incoming and outgoing messages
            message: a MessageView of the message"""
        print "PartiallyImplementedError:\taMSNChatWidget.on_message_received() messageview =",
        print repr(messageview.msg)

        tempStr = QString("<br>")
        if formatting is not None:
            tempStr.append("<font face=\"%s\" color=\"#%s\">" % ( formatting.font, formatting.color ))
        tempStr.append(messageview.to_stringview().to_HTML_string())
        if formatting is not None:
            tempStr.append("</font>")
        tempStr.append("<br>")
        
        self.chatText.append(tempStr)
        self.chatView.setText(self.chatText)
        

    def on_user_joined(self, nickname):
        print "NotImplementedError:\t\taMSNChatWidget.on_user_joined()"

    def nudge(self):
        print "NotImplementedError:\t\taMSNChatWidget.nudge()"

    def on_user_typing(self, contact):
        print "NotImplementedError:\t\taMSNChatWidget.on_user_typing()"


    # -------------------- QT_SLOTS

    def qslotSendMessage(self):
        message = StringView()
        message.append_text(str(self.lineEdit.text()))
        self.lineEdit.setText("")
        self._amsn_conversation.send_message(message)

if __name__ == "__main__":
    about = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about)
    kapp = KApplication()
    w = aMSNChatWindow(None)
    w.add_chat_widget(aMSNChatWidget(None,w,"3"))
    w.show()
    kapp.exec_()


    