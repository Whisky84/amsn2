# -*- coding: utf-8 -*-

from kfeLog   import KFELog
from kfeStatic          import kMenuBarFromMenuView

from amsn2.ui import base

class KFEAbstractChatWindow (base.aMSNChatWindow): 
    def __init__(self, amsn_core):
        KFELog().l("KFEAbstractChatWindow.__init__()\n\t")
        self.amsn_core = amsn_core
        self.constructor()

    #CORE SIDE INTERFACE
    def add_chat_widget(self, chat_widget):
        self.addChatWidget(chat_widget)

    def set_menu(self, menuView):
        KFELog().l("tKFEAbstractChatWindow.set_menu()\n\t")
        menuBar = kMenuBarFromMenuView(menuView, self)
        self.setMenu(menuBar)

    def set_title(self, title):
        self.setTitle(title)

    #FRONT END SIDE INTERFACE
    def addChatWidget(self, chatWidget):
        KFELog().l("KFEAbstractChatWindow.addChatWidget()\tNotImplementedError\n")

    def setTitle(self, title):
        KFELog().l("KFEAbstractChatWindow.setTitle()\tNotImplementedError\n")



class KFEAbstractChatWidget (base.aMSNChatWidget):
    def __init__(self, amsn_conversation, parent, contacts_uid):
        KFELog().l("KFEAbstractChatWidget.__init__()\n\t")
        self.amsn_conversation = amsn_conversation
        self.constructor(contacts_uid, parent)

    #CORE SIDE INTERFACE
    def on_message_received(self, messageview, formatting):
        #TODO: transalte messageview into something more KDEish
        self.onMessageReceived(messageview, formatting)

    def nudge(self):
        self.onNudge()

    def on_user_typing(self, contact):
        self.onUserTyping(contact)

    #FRONT END SIDE INTERFACE
    def onMessageReceived(self, messageView, formatting):
        KFELog().l("KFEAbstractChatWidget.onMessageReceived()\tNotImplementedError\n")

    def onNudge(self):
        KFELog().l("KFEAbstractChatWidget.onNudge()\tNotImplementedError\n")

    def onUserTyping(self, contact):
        KFELog().l("KFEAbstractChatWidget.onUserTyping()\tNotImplementedError\n")

    def sendMessage(self, message):
        KFELog().l("KFEAbstractChatWidget.sendMessage()\n\t")
        self.amsn_conversation.send_message(message)





    
        