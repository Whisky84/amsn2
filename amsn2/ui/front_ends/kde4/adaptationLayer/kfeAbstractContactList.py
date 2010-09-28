# -*- coding: utf-8 -*-

from kfeLog   import KFELog
from amsn2.ui import base

class KFEAbstractContactListWindow (base.aMSNContactListWindow): # removed KFEWindow mother class
    def __init__(self, amsn_core, parent):
        KFELog().l("KFEAbstractContactListWindow.__init__()", True)
        self.amsn_core = amsn_core
        self.constructor(parent)

    #CORE SIDE INTERFACE
    def my_info_updated(self, view):
        self.onMyInfoUpdated(view)

    def get_contactlist_widget(self):
        return self.getContactListWidget()

    #FRONT END SIDE INTERFACE
    def onMyInfoUpdated(self, window):
        KFELog().l("KFEAbstractContactListWindow.onMyInfoUpdated()", False, 2)

    def onNewConversationRequested(self, uid):
        KFELog().l("KFEAbstractContactListWindow.onNewConversationRequested()")
        self.amsn_core._conversation_manager.new_conversation([uid])

    def getContactListWidget(self):
        KFELog().l("KFEAbstractContactListWindow.getContactListWidget()", False, 2)

    #FESI'
    def onNewNickSet(self, nick):
        self.amsn_core._personalinfo_manager._on_nick_changed(str(nick))
        KFELog().d(nick, "KFEAbstractContactListWindow.onNewNickSet()")
        
    def onNewPsmSet(self, psm):
        self.amsn_core._personalinfo_manager._on_PSM_changed(str(psm))
        KFELog().d(psm, "KFEAbstractContactListWindow.onNewPsmSet()")
        
    def onNewPresenceSet(self, presence):
        #Why the core communicates the presence eith a string, WHY?!?!!? ;_________;
        if presence in self.amsn_core.p2s.keys():
            KFELog().d("presence: %s" % presence, "KFEAbstractContactListWindow.onNewPresenceSet()")
            self.amsn_core._personalinfo_manager._on_presence_changed(self.amsn_core.p2s[presence])

    def onDisplayPicChooseRequest(self):
        self.amsn_core._personalinfo_manager._on_DP_change_request()
        
        



class KFEAbstractContactListWidget(base.aMSNContactListWidget):
    def __init__(self, parent=None):
        KFELog().l("KFEAbstractContactListWidget.__init__()", True)
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
        KFELog().l("KFEAbstractContactListWidget.onContactListUpdated()", False, 2)

    def onGroupUpdated(self, groupView):
        KFELog().l("KFEAbstractContactListWidget.onGroupUpdated()", False, 2)

    def onContactUpdated(self, contactView):
        KFELog().l("KFEAbstractContactListWidget.onContactUpdated()", False, 2)