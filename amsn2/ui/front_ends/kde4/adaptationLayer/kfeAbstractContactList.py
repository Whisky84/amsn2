# -*- coding: utf-8 -*-

from amsn2.ui import base

class KFEAbstractContactListWindow (base.aMSNContactListWindow): # removed KFEWindow mother class
    def __init__(self, amsn_core, parent):
        print "\t\t\t\tKFEAbstractContactListWindow.__init__()"
        self.amsn_core = amsn_core
        self.constructor(parent)

    #CORE SIDE INTERFACE
    def my_info_updated(self, view):
        self.onMyInfoUpdated(view)

    def get_contactlist_widget(self):
        return self.getContactListWidget()

    #FRONT END SIDE INTERFACE
    def onMyInfoUpdated(self, window):
        print "NotImplementedError:\t\tKFEAbstractContactListWindow.onMyInfoUpdated()"

    def onNewConversationRequested(self, uid):
        print "\t\t\t\tKFEAbstractContactListWindow.onNewConversationRequested()"
        self.amsn_core._conversation_manager.new_conversation([uid])

    def getContactListWidget(self):
        print "NotImplementedError:\t\tKFEAbstractContactListWindow.getContactListWidget()"
        

class KFEAbstractContactListWidget(base.aMSNContactListWidget):
    def __init__(self, parent=None):
        print "NotImplementedError:\t\tKFEContactListWidget.__init__()"
        self.constructor(parent)

    #CORE SIDE INTERFACE
    def contactlist_updated(self, clView):
        self.onContactListUpdated(clView)

    def group_updated(self, groupView):
        self.onGroupUpdated(groupView)

    def contact_updated(self, contactView):
        self.onContactUpdated(contactView)

    #FRONT END SIDE INTERFACE
    def onContactListUpdated(self, clView):
        print "NotImplementedError:\t\tKFEAbstractContactListWidget.onContactListUpdated()"

    def onGroupUpdated(self, groupView):
        print "NotImplementedError:\t\tKFEAbstractContactListWidget.onGroupUpdated()"

    def onContactUpdated(self, contactView):
        print "NotImplementedError:\t\tKFEAbstractContactListWidget.onContactUpdated()"