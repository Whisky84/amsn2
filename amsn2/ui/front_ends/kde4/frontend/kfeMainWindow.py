# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog
from amsn2.ui.front_ends.kde4 import adaptationLayer

from PyKDE4.kdeui   import  *

from PyQt4.QtGui    import  *

class KFEMainWindow (adaptationLayer.KFEAbstractMainWindow, KMainWindow):
    def constructor(self):
        KFELog().l("\t\t   KFEMainWindow.constructor()")
        KMainWindow.__init__(self)
        self.setWindowIcon(KIcon("im-user"))
        self.widgetStack = QStackedWidget()
        self.setCentralWidget(self.widgetStack)

    def setMenu(self, menuBar):
        KFELog().l("\t\tKFEMainWindow.setMenu()")
        self.setMenuBar(menuBar)

    def setTitle(self, title):
        KFELog().l("\t\tKFEMainWindow.setTitle()")
        self.setPlainCaption(title)

    def show(self):
        KFELog().l("\t\tKFEMainWindow.show()")
        KMainWindow.show(self)
        self.onMainWindowShown()

    def switchToWidget(self, widget):
        KFELog().l("\t\t   KFEMainWindow.switchToWidget()")
        index = self.widgetStack.indexOf(widget)
        if index == -1:
            index = self.widgetStack.addWidget(widget)
        self.widgetStack.setCurrentIndex(index)


# -------------------- QT_OVERLOAD
    def closeEvent(self, event):
        KFELog().l("\t\t\t\tKFEMainWindow.closeEvent()")
        event.accept()
        self.onClose()


