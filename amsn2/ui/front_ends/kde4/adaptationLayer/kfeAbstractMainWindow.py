# -*- coding: utf-8 -*-

from kfeLog             import KFELog

from kfePresence        import KFEPresence
from kfeThemeManager    import KFEThemeManager
from kfeStatic          import kMenuBarFromMenuView

from amsn2.ui  import base

from PyQt4.QtCore   import *



class KFEAbstractMainWindow (base.aMSNMainWindow, base.aMSNWindow): # removed KFEWindow mother class, added base.aMSNWindow
    def __init__(self, amsn_core):
        KFELog().l("KFEAbstractMainWindow.__init__()\n  ")
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
        KFELog().l("KFEAbstractMainWindow.set_menu()\n\t")
        menuBar = kMenuBarFromMenuView(menuView, self)
        self.setMenu(menuBar)

    #def show(self):
        #this method has already a good interface


    #FRONT END SIDE INTERFACE
    def constructor(self):
        KFELog().l("KFEAbstractMainWindow.constructor()\tNotImplementedError\n")

    def hide(self):
        KFELog().l("KFEAbstractMainWindow.hide()\tNotImplementedError\n")
        
    def onClose(self):
        KFELog().l("KFEAbstractMainWindow.onClose()")
        self.amsn_core.quit()

    def onMainWindowShown(self):
        KFELog().l("KFEAbstractMainWindow.onMainWindowShown()")
        self.amsn_core.main_window_shown()
        
    def setMenu(self, menuBar):
        KFELog().l("KFEAbstractMainWindow.setMenu()\tNotImplementedError\n")
        
    def setTitle(self, title):
        KFELog().l("KFEAbstractMainWindow.setTile()\tNotImplementedError\n")
        
    def switchToWidget(self, widget):
        KFELog().l("KFEAbstractMainWindow.switchToWidget()\tNotImplementedError\n")

