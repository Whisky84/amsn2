# -*- coding: utf-8 -*-

from kfePresence        import KFEPresence
from kfeThemeManager    import KFEThemeManager
from kfeStatic          import kMenuBarFromMenuView

from amsn2.ui  import base

from PyQt4.QtCore   import *



class KFEAbstractMainWindow (base.aMSNMainWindow, base.aMSNWindow): # removed KFEWindow mother class, added base.aMSNWindow
    def __init__(self, amsn_core):
        print "\t\t\t\tKFEAbstractMainWindow.__init__()"
        self.amsn_core = amsn_core
        KFEThemeManager.setManager(self.amsn_core._theme_manager)
        KFEPresence().setCore(self.amsn_core)
        self.constructor()
        
    #CORE SIDE INTERFACE
    #FROM aMSNWindow
    #def hide(self):
        #this method has already a good interface

    def set_title(self, title):
        self.setTitle(title)
        
    def set_menu(self, menuView):
        print "\t\t\t\tKFEAbstractMainWindow.set_menu()"
        menuBar = kMenuBarFromMenuView(menuView, self)
        self.setMenu(menuBar)

    #def show(self):
        #this method has already a good interface


    #FRONT END SIDE INTERFACE
    def constructor(self):
        print "NotImplementedError:\t\tKFEAbstractMainWindow.constructor()"

    def hide(self):
        print "NotImplementedError:\t\tKFEAbstractMainWindow.hide()"
        
    def onClose(self):
        print "\t\t\t\tKFEAbstractMainWindow.onClose()"
        self.amsn_core.quit()

    def onMainWindowShown(self):
        print "\t\t\t\tKFEAbstractMainWindow.onMainWindowShown()"
        self.amsn_core.main_window_shown()
        
    def setMenu(self, menuBar):
        print "NotImplementedError:\t\tKFEAbstractMainWindow.setMenu()"
        
    def setTitle(self, title):
        print "NotImplementedError:\t\tKFEAbstractMainWindow.setTile()"
        
    def switchToWidget(self, widget):
        print "NotImplementedError:\t\tKFEAbstractMainWindow.switchToWidget()"

