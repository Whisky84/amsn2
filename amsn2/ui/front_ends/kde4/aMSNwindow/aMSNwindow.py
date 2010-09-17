# -*- coding: utf-8 -*-

from amsn2.ui import base

from PyQt4.QtGui import QWidget

class aMSNWindow(base.aMSNWindow, QWidget):
    """ This Interface represents a window of the application. Everything will be done from here """
    def __init__(self, amsn_core):
        """
        @type amsn_core: aMSNCore
        """
        print "\t\t\t\taMSNWindow.__init__()"
        QWidget.__init__(self, None)

    def show(self):
        """ This launches the window, creates it, etc.."""
        print "\t\t\t\taMSNWindow.show()"
        QWidget.show(self)

    def hide(self):
        """ This should hide the window"""
        print "\t\t\t\taMSNWindow.hide()"
        QWidget.hide(self)

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
