# -*- coding: utf-8 -*-

from amsn2.ui import base

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class aMSNMainWindow(base.aMSNMainWindow, KMainWindow):
    """ This Interface represents the main window of the application. Everything will be done from here 
    When the window is shown, it should call: amsn_core.mainWindowShown()
    When the user wants to close that window, amsn_core.quit() should be called.
    """

    def __init__(self, amsn_core):
        """
        @type amsn_core: aMSNCore
        """
        print "\t\t\t\taMSNMainWindow.__init__()"
        KMainWindow.__init__(self)
        self._core = amsn_core
        
        self.setWindowIcon(KIcon("im-user"))
        
        self.widget_stack = QStackedWidget()
        self.setCentralWidget(self.widget_stack)
        

    def show(self):
        print "\t\t\t\taMSNMainWindow.show()"
        KMainWindow.show(self)
        self._core.main_window_shown()
        

    def hide(self):
        print "\t\t\t\taMSNMainWindow.hide()"
        KMainWindow.hide(self)
        

    def set_title(self,title):
        print "NWAE:\t\taMSNMainWindow.set_title()"
        self.setPlainCaption(title)
        
        
    def set_menu(self,menu):
        print "NotImplementedError:\t\taMSNMainWindow.set_menu()"


# -------------------- QT_OVERLOAD

    
    def closeEvent(self, event):
        print "\t\t\t\tmainwindow.closeEvent()"
        self.core.quit()
        event.accept()
        
        
# -------------------- OTHER_METHODS
    
    def switch_to_widget(self, widget):
        index = self.widget_stack.indexOf(widget)
        if index == -1:
            index = self.widget_stack.addWidget(widget)
    self.widget_stack.setCurrentIndex(index) 
