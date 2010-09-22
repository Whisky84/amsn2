# -*- coding: utf-8 -*-

from mainWindowPages    import  KFEContactListPage
from models             import  ContactDelegate,        \
                                ContactListModel,       \
                                ContactStyledDelegate
                                

from amsn2.ui.front_ends.kde4   import adaptationLayer
from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager


from widgets        import  KFENickEdit,    \
                            KFEPresenceCombo
                            

from PyQt4.QtGui    import  *
from PyQt4.QtCore   import  *


class KFEContactListWindow (adaptationLayer.KFEAbstractContactListWindow):
    def constructor(self, parent=None):
        print "\t\t\t\tKFEContactListWindow.constructor()"
        self._main_window = parent

        self._clwidget = KFEContactListWidget()
        QObject.connect(self._clwidget, SIGNAL("newConversationRequested(char*)"), self.onNewConversationRequested)
        self.contactListPage = KFEContactListPage(self._clwidget)

    def hide(self):
        pass
    
    def show(self):
        print "\t\t\t\tKFEContactListWindow.show()"
        self._main_window.switchToWidget(self.contactListPage)

    def onMyInfoUpdated(self, view):
        print "\t\t\t\tKFEContactListWindow.onMyInfoUpdated()"
        self.contactListPage.onMyInfoUpdated(view)


    def getContactListWidget(self):
        print "\t\t\t\tKFEContactListWindow.getContactlistWidget()"
        return self._clwidget





class KFEContactListWidget(adaptationLayer.KFEAbstractContactListWidget, QListView):
    def constructor(self, parent=None):
        print "PartiallyImplementedError:\tKFEContactListWidget.constructor()"
        QListView.__init__(self, parent)

        self.cl_model = ContactListModel(self)
        self.setModel(self.cl_model)
        self.setItemDelegate(ContactStyledDelegate(self))

        QObject.connect(self, SIGNAL("doubleClicked(const QModelIndex&)"), self.onItemDoubleClicked)


    def onContactlistUpdated(self, clView):
        print "\t\t\t\tKFEContactListWidget.onContactlistUpdated()"
        self.cl_model.onContactListUpdated(clView)


    def onGroupUpdated(self, groupView):
        self.cl_model.onGroupUpdated(groupView)


    def onContactUpdated(self, contactView):
        self.cl_model.onContactUpdated(contactView)

    # -------------------- QT_SLOTS

    def onItemDoubleClicked(self, item):
        self.emit(SIGNAL("newConversationRequested(char*)"), self.cl_model.data(item, Qt.UserRole))






