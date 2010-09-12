# -*- coding: utf-8 -*-

from amsn2.ui import base

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from amsn2.ui.front_ends.kde4.widgets import KPresenceComboBox, KNickEdit
from amsn2.ui.front_ends.kde4.models import ContactListModel


"""TODO:
    * Let the aMSNContactListWidget be selectable to choose contacts to add to a
    conversation... each contact should have a checkbox on front of it
    * Drag contacts through groups
    * Drag groups
    ...
"""


class aMSNContactListWindow(base.aMSNContactListWindow, QWidget):
    """ This interface represents the main Contact List Window
        self._clwiget is an aMSNContactListWidget 
    """
    def __init__(self, amsn_core, parent = None):
        """Initialize the interface. You should store the reference to the core in here """
        print "\t\t\t\taMSNContactListWindow.__init__()"
        self._core = amsn_core
        self._main_window = parent
        
        QWidget.__init__(self, parent)
        
        lay = QVBoxLayout()
        
        my_info_lay = QHBoxLayout()
        my_info_lay_left = QVBoxLayout()
        
        self.nick = KNickEdit()
        self.psm = KNickEdit(allowEmpty = True, emptyMessage=QString("<u>Click here to set a personal message...</u>"))
        self.current_media = QLabel()
        
        self.presence_combo = KPresenceComboBox(self._core)
        
        my_info_lay_left.addWidget(self.nick)
        my_info_lay_left.addWidget(self.psm)
        my_info_lay_left.addWidget(self.current_media)
        my_info_lay_left.addWidget(self.presence_combo)
        
        dp = QLabel()
        _, path = self._core._theme_manager.get_value("dp_amsn")
        dp.setPixmap(QPixmap(path))
        my_info_lay.addWidget(dp)
        my_info_lay.addLayout(my_info_lay_left)
        
        self._clwidget = aMSNContactListWidget(self._core, self)
        
        lay.addLayout(my_info_lay)
        lay.addWidget(self._clwidget)
        
        self.setLayout(lay)
        
    
    def show(self):
        """ Show the contact list window """
        print "\t\t\t\taMSNContactListWindow.show()"
        QWidget.show(self)
        self._main_window.switch_to_widget(self)
        

    def hide(self):
        """ Hide the contact list window """
        print "NotImplementedError:\t\taMSNContactListWindow.hide()"
        

    def set_title(self, text):
        """ This will allow the core to change the current window's title
        @type text: str
        """
        print "\t\t\t\taMSNContactListWindow.set_title()"
        self._main_window.set_title(text)
        

    def set_menu(self, menu):
        """ This will allow the core to change the current window's main menu
        @type menu: MenuView
        """
        print "\t\t\t\taMSNContactListWindow.set_menu()"
        self._main_window.set_menu(menu)
        

    def my_info_updated(self, view):
        """ This will allow the core to change pieces of information about
        ourself, such as DP, nick, psm, the current media being played,...
        @type view: PersonalInfoView
        @param view: the PersonalInfoView of the ourself (contains DP, nick, psm,
        currentMedia,...)"""
        print "PartiallyImplementedError:\taMSNContactListWindow.my_info_updated()"
        self.nick.setText(view.nick.to_HTML_string())
        if not QString(str(view.psm)).isEmpty(): #Think carefully: i think we can remove this if (look at KPresenceComboBox.setText()'s implementation)
            self.psm.setText(view.psm.to_HTML_string())
        print "N. of personal Images:" + str(len(view.dp.imgs))
        if len(view.dp.imgs) > 0:
            print "WE HAVE A DP FROM THE CORE! UPDATE THE FRONT END CODE!!"
        self.current_media.setText(view.current_media.to_HTML_string())
        #TODO: view.presence holds a string.... shouldn0t it hold a papyon.Presence?
        #self.presence_combo.setPresence(view.presence) <-- this could be used when it will hold a papyon.Presence
        self.presence_combo.setCurrentIndex(self.presence_combo.findText(view.presence.capitalize()))
        

    def get_contactlist_widget(self):
        """This will allow the core to access the widget"""
        print "\t\t\t\taMSNContactListWindow.get_contactlist_widget()"
        return self._clwidget



class aMSNContactListWidget(base.aMSNContactListWidget, QTreeView):
    """ This interface implements the contact list of the UI """
    def __init__(self, amsn_core, parent):
        """Initialize the interface. You should store the reference to the core in here """
        print "PartiallyImplementedError:\taMSNContactListWidget.__init__()"
        self._core = amsn_core
        QTreeView.__init__(self, parent)
        self.cl_model = ContactListModel()
        self.setModel(self.cl_model)
        

    def show(self):
        """ Show the contact list widget """
        print "\t\t\t\taMSNContactListWidget.show()"
        #QTreeView.show(self)
        

    def hide(self):
        """ Hide the contact list widget """
        print "NotImplementedError:\t\taMSNContactListWidget.hide()"
        

    def contactlist_updated(self, clView):
        """ This method will be called when the core wants to notify
        the contact list of the groups that it contains, and where they
        should be drawn a group should be drawn.
        It will be called initially to feed the contact list with the groups
        that the CL should contain.
        It will also be called to remove any group that needs to be removed.

        @type clView: ContactListView
        @param clView : contains the list of groups contained in
        the contact list which will contain the list of ContactViews
        for all the contacts to show in the group."""
        print "NotImplementedError:\t\taMSNContactListWidget.contactlist_updated()"
        self.cl_model.contactlist_updated(clView)
        

    def group_updated(self, groupView):
        """ This method will be called to notify the contact list
        that a group has been updated.
        The contact list should update its icon and name
        but also its content (the ContactViews). The order of the contacts
        may be changed, in which case the UI should update itself accordingly.
        A contact can also be added or removed from a group using this method
        """
        print "NotImplementedError:\t\taMSNContactListWidget.group_updated()"
        print groupView
        

    def contact_updated(self, contactView):
        """ This method will be called to notify the contact list
        that a contact has been updated.
        The contact can be in any group drawn and his icon,
        name or DP should be updated accordingly.
        The position of the contact will not be changed by a call
        to this function. If the position was changed, a groupUpdated
        call will be made with the new order of the contacts
        in the affects groups.
        """
        print "NotImplementedError:\t\taMSNContactListWidget.contact_updated()"
        print contactView
        
