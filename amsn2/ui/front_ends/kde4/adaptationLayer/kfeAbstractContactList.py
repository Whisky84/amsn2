# -*- coding: utf-8 -*-

from kfeLog   import KFELog
from amsn2.ui import base

class KFEAbstractContactListWindow (base.aMSNContactListWindow): # removed KFEWindow mother class
    def __init__(self, amsn_core, parent):
        KFELog().l("KFEAbstractContactListWindow.__init__()\n\t")
        self.amsn_core = amsn_core
        self.constructor(parent)

    #CORE SIDE INTERFACE
    def my_info_updated(self, view):
        self.onMyInfoUpdated(view)

    def get_contactlist_widget(self):
        return self.getContactListWidget()

    #FRONT END SIDE INTERFACE
    def onMyInfoUpdated(self, window):
        KFELog().l("KFEAbstractContactListWindow.onMyInfoUpdated()\tNotImplementedError\n")

    def onNewConversationRequested(self, uid):
        KFELog().l("KFEAbstractContactListWindow.onNewConversationRequested()\n")
        self.amsn_core._conversation_manager.new_conversation([uid])

    def getContactListWidget(self):
        KFELog().l("KFEAbstractContactListWindow.getContactListWidget()\tNotImplementedError\n")
        

class KFEAbstractContactListWidget(base.aMSNContactListWidget):
    def __init__(self, parent=None):
        KFELog().l("KFEAbstractContactListWidget.__init__()\n")
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
        KFELog().l("KFEAbstractContactListWidget.onContactListUpdated()\tNotImplementedError\n")

    def onGroupUpdated(self, groupView):
        KFELog().l("KFEAbstractContactListWidget.onGroupUpdated()\tNotImplementedError\n")

    def onContactUpdated(self, contactView):
        KFELog().l("KFEAbstractContactListWidget.onContactUpdated()\tNotImplementedError\n")