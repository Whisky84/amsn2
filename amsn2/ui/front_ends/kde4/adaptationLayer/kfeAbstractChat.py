# -*- coding: utf-8 -*-

from kfeStatic          import kMenuBarFromMenuView

from amsn2.ui import base

class KFEAbstractChatWindow (base.aMSNChatWindow): 
    def __init__(self, amsn_core):
        print "\t\t\t\tKFEAbstractChatWindow.__init__()"
        self.amsn_core = amsn_core
        self.constructor()

    #CORE SIDE INTERFACE
    def add_chat_widget(self, chat_widget):
        self.addChatWidget(chat_widget)

    def set_menu(self, menuView):
        print "\t\t\t\tKFEAbstractChatWindow.set_menu()"
        menuBar = kMenuBarFromMenuView(menuView, self)
        self.setMenu(menuBar)

    def set_title(self, title):
        self.setTitle(title)

    #FRONT END SIDE INTERFACE
    def addChatWidget(self, chatWidget):
        print "NotImplementedError:\t\tKFEAbstractChatWindow.addChatWidget()"

    def setTitle(self, title):
        print "NotImplementedError:\t\tKFEAbstractChatWindow.setTitle()"



class KFEAbstractChatWidget (base.aMSNChatWidget):
    def __init__(self, amsn_conversation, parent, contacts_uid):
        print "\t\t\t\tKFEAbstractChatWidget.__init__()"
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
        print "NotImplementedError:\t\tKFEAbstractChatWidget.onMessageReceived()"

    def onNudge(self):
        print "NotImplementedError:\t\tKFEAbstractChatWidget.onNudge()"

    def onUserTyping(self, contact):
        print "NotImplementedError:\t\tKFEAbstractChatWidget.onUserTyping()"

    def sendMessage(self, message):
        print "\t\t\t\tKFEAbstractChatWidget.sendMessage()"
        self.amsn_conversation.send_message(message)





    
        