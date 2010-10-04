# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog
from amsn2.ui.front_ends.kde4 import adaptationLayer

from PyKDE4.kdeui   import  *

from PyQt4.QtGui    import  *

class KFEMainWindow (adaptationLayer.KFEAbstractMainWindow, KMainWindow):
    def constructor(self):
        KFELog().l("KFEMainWindow.constructor()")
        KMainWindow.__init__(self)
        self.setObjectName("mainwindow")
        
        self.setWindowIcon(KIcon("im-user"))
        self.widgetStack = QStackedWidget()
        self.setCentralWidget(self.widgetStack)

    def setMenu(self, menuBar):
        KFELog().l("KFEMainWindow.setMenu()")
        self.setMenuBar(menuBar)

    def setTitle(self, title):
        KFELog().l("KFEMainWindow.setTitle()")
        self.setPlainCaption(title)

    def show(self):
        KFELog().l("KFEMainWindow.show()")
        KMainWindow.show(self)
        self.onMainWindowShown()

    def switchToWidget(self, widget):
        KFELog().l("KFEMainWindow.switchToWidget()")
        index = self.widgetStack.indexOf(widget)
        if index == -1:
            index = self.widgetStack.addWidget(widget)
        self.widgetStack.setCurrentIndex(index)


# -------------------- QT_OVERRIDE
    def closeEvent(self, event):
        KFELog().l("KFEMainWindow.closeEvent()")
        event.accept()
        self.onClose()


