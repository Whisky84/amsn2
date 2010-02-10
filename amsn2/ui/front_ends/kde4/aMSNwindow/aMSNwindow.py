# -*- coding: utf-8 -*-

from amsn2.ui import base

class aMSNWindow(base.aMSNWindow):
    """ This Interface represents a window of the application. Everything will be done from here """
    def __init__(self, amsn_core):
        """
        @type amsn_core: aMSNCore
        """

        print "NotImplementedError:\t\taMSNWindow.__init__()"

    def show(self):
        """ This launches the window, creates it, etc.."""
        print "NotImplementedError:\t\taMSNWindow.show()"

    def hide(self):
        """ This should hide the window"""
        print "NotImplementedError:\t\taMSNWindow.hide()"

    def set_title(self, text):
        """
        This will allow the core to change the current window's title

        @type text: str
        """
        print "NotImplementedError:\t\taMSNWindow.set_title()"

    def set_menu(self, menu):
        """
        This will allow the core to change the current window's main menu

        @type menu: MenuView
        """
        print "NotImplementedError:\t\taMSNWindow.set_menu()"
