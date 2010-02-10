# -*- coding: utf-8 -*-

from amsn2.ui import base

class aMSNMainWindow(base.aMSNMainWindow):
    """ This Interface represents the main window of the application. Everything will be done from here 
    When the window is shown, it should call: amsn_core.mainWindowShown()
    When the user wants to close that window, amsn_core.quit() should be called.
    """

    def __init__(self, amsn_core):
        """
        @type amsn_core: aMSNCore
        """
        print "NotImplementedError:\t\taMSNMainWindow.__init__()"
        pass

    def show(self):
        print "NotImplementedError:\t\taMSNMainWindow.show()"

    def hide(self):
        print "NotImplementedError:\t\taMSNMainWindow.hide()"

    def set_title(self,title):
        print "NotImplementedError:\t\taMSNMainWindow.set_title()"

    def set_menu(self,menu):
        print "NotImplementedError:\t\taMSNMainWindow.set_menu()"

