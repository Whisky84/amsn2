# -*- coding: utf-8 -*-

from amsn2.ui import base

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from kloginpage import KLoginPage
from ksignininpage import KSigninInPage

class aMSNLoginWindow(base.aMSNLoginWindow, QStackedWidget):
    """ This interface will represent the login window of the UI"""
    def __init__(self, amsn_core, parent):
        """Initialize the interface. You should store the reference to the core in here """
        print "\t\t\t\taMSNLoginWindow.__init__()"
        QStackedWidget.__init__(self, parent)
        
        self._core = amsn_core
        self._main_window = parent
        
        self._account_views = None
        
        self.signin_in_page = KSigninInPage()
        self.login_page = KLoginPage(self._core)
        
        self.addWidget(self.signin_in_page)
        self.addWidget(self.login_page)
        
        self.setCurrentWidget(self.login_page)
        

    def show(self):
        """ Draw the login window """
        print "\t\t\t\taMSNLoginWindow.show()"
        self._main_window.switch_to_widget(self)
        QStackedWidget.show(self)


    def hide(self):
        """ Hide the login window """
        print "NotImplementedError:\t\taMSNLoginWindow.hide()"
        

    def set_accounts(self, accountviews):
        """ This method will be called when the core needs the login window to
        let the user select among some accounts.

        @param accountviews: list of accountviews describing accounts
        The first one in the list
        should be considered as default. """
        print "\t\t\t\taMSNLoginWindow.set_accounts()"
        self._account_views = accountviews
        self.login_page.set_accounts(accountviews)
        

    def signing_in(self):
        """ This method will be called when the core needs the login window to start the signin process.
        This is intended only to change the look of the login window. """
        print "\t\t\t\taMSNLoginWindow.signin()"
        self.setCurrentWidget(self.signin_in_page)
        

    def signout(self):
        """ This method will be called when the core needs the login window to stop the signin process.
        This is intended only to change the look of the login window. """
        print "\t\t\t\taMSNLoginWindow.signout()"
        self.setCurrentWidget(self.login_page)

    def on_connecting(self, progress, message):
        """ This method will be called to notify the UI that we are connecting.

        @type progress: float
        @param progress: the current progress of the connexion (to be
        exploited as a progress bar, for example)
        @param message: the message to show while loging in """
        print "\t\t\t\taMSNLoginWindow.on_connecting()"
        self.signin_in_page.on_connecting(progress, message)

