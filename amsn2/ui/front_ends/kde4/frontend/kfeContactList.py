# -*- coding: utf-8 -*-

from mainWindowPages    import  KFEContactListPage
from models             import  ContactDelegate,        \
                                ContactListModel,       \
                                ContactStyledDelegate
                                

from amsn2.ui.front_ends.kde4   import adaptationLayer
from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager, KFELog


from widgets        import  KFENickEdit,    \
                            KFEPresenceCombo
                            

from PyQt4.QtGui    import  *
from PyQt4.QtCore   import  *


class KFEContactListWindow (adaptationLayer.KFEAbstractContactListWindow):
    def constructor(self, parent=None):
        KFELog().l("KFEContactListWindow.constructor()")
        self._main_window = parent

        self._clwidget = KFEContactListWidget()
        QObject.connect(self._clwidget, SIGNAL("newConversationRequested(char*)"), self.onNewConversationRequested)
        self.contactListPage = KFEContactListPage(self._clwidget, self)

    def hide(self):
        pass
    
    def show(self):
        KFELog().l("KFEContactListWindow.show()")
        self._main_window.switchToWidget(self.contactListPage)

    def onMyInfoUpdated(self, view):
        KFELog().l("KFEContactListWindow.onMyInfoUpdated()")
        self.contactListPage.onMyInfoUpdated(view)


    def getContactListWidget(self):
        KFELog().l("KFEContactListWindow.getContactlistWidget()")
        return self._clwidget





class KFEContactListWidget(adaptationLayer.KFEAbstractContactListWidget, QTreeView):
    def constructor(self, parent=None):
        KFELog().l("KFEContactListWidget.constructor()")
        QListView.__init__(self, parent)

        self.cl_model = ContactListModel(self)
        self.setModel(self.cl_model)
        self.setItemDelegate(ContactStyledDelegate(self))
        self.setAnimated(True)
        self.setHeaderHidden(True)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setSortingEnabled(True)
        #self.setIndentation(0)
        QObject.connect(self, SIGNAL("doubleClicked(const QModelIndex&)"), self.onItemDoubleClicked)

    def edit(self, index, trigger, event):
        return False
        
    def onContactListUpdated(self, clView):
        KFELog().l("KFEContactListWidget.onContactListUpdated()")
        self.cl_model.onContactListUpdated(clView)


    def onGroupUpdated(self, groupView):
        KFELog().l("KFEContactListWidget.onGroupUpdated()")
        self.cl_model.onGroupUpdated(groupView)


    def onContactUpdated(self, contactView):
        #KFELog().l("KFEContactListWidget.onContactUpdated()")
        self.cl_model.onContactUpdated(contactView)

    # -------------------- QT_SLOTS

    def onItemDoubleClicked(self, item):
        self.emit(SIGNAL("newConversationRequested(char*)"), self.cl_model.data(item, Qt.UserRole))






