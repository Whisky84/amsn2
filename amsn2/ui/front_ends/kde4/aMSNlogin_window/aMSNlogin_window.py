# -*- coding: utf-8 -*-

from amsn2.ui import base

class aMSNLoginWindow(base.aMSNLoginWindow):
    """ This interface will represent the login window of the UI"""
    def __init__(self, amsn_core, parent):
        """Initialize the interface. You should store the reference to the core in here """
        print "NotImplementedError:\t\taMSNLoginWindow.__init__()"

    def show(self):
        """ Draw the login window """
        print "NotImplementedError:\t\taMSNLoginWindow.show()"

    def hide(self):
        """ Hide the login window """
        print "NotImplementedError:\t\taMSNLoginWindow.hide()"

    def set_accounts(self, accountviews):
        """ This method will be called when the core needs the login window to
        let the user select among some accounts.

        @param accountviews: list of accountviews describing accounts
        The first one in the list
        should be considered as default. """
        print "NotImplementedError:\t\taMSNLoginWindow.set_accounts()"

    def signin(self):
        """ This method will be called when the core needs the login window to start the signin process.
        This is intended only to change the look of the login window. """
        print "NotImplementedError:\t\taMSNLoginWindow.signin()"

    def signout(self):
        """ This method will be called when the core needs the login window to stop the signin process.
        This is intended only to change the look of the login window. """
        print "NotImplementedError:\t\taMSNLoginWindow.signout()"

    def on_connecting(self, progress, message):
        """ This method will be called to notify the UI that we are connecting.

        @type progress: float
        @param progress: the current progress of the connexion (to be
        exploited as a progress bar, for example)
        @param message: the message to show while loging in """
        print "NotImplementedError:\t\taMSNLoginWindow.on_connecting()"

