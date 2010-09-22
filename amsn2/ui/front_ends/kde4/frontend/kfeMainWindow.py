# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4 import adaptationLayer

from PyKDE4.kdeui   import  *

from PyQt4.QtGui    import  *

class KFEMainWindow (adaptationLayer.KFEAbstractMainWindow, KMainWindow):
    def constructor(self):
        print "\t\t\t\tKFEMainWindow.constructor()"
        KMainWindow.__init__(self)
        self.setWindowIcon(KIcon("im-user"))
        self.widgetStack = QStackedWidget()
        self.setCentralWidget(self.widgetStack)

    def setMenu(self, menuBar):
        print "\t\t\t\tKFEMainWindow.constructor()"
        self.setMenuBar(menuBar)

    def setTitle(self, title):
        print "\t\t\t\tKFEMainWindow.setTitle()"
        self.setPlainCaption(title)

    def show(self):
        print "\t\t\t\tKFEMainWindow.show()"
        KMainWindow.show(self)
        self.onMainWindowShown()

    def switchToWidget(self, widget):
        print "\t\t\t\tKFEMainWindow.switchToWidget()"
        index = self.widgetStack.indexOf(widget)
        if index == -1:
            index = self.widgetStack.addWidget(widget)
        self.widgetStack.setCurrentIndex(index)


# -------------------- QT_OVERLOAD
    def closeEvent(self, event):
        print "\t\t\t\tKFEMainWindow.closeEvent()"
        event.accept()
        self.onClose()


