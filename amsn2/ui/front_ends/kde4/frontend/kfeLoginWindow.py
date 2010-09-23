# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog


from mainWindowPages    import  KFEAccountPage,   \
                                KFESigningInPage

from amsn2.ui.front_ends.kde4 import adaptationLayer

from PyQt4.QtCore       import  QObject

class KFELoginWindow (adaptationLayer.KFEAbstractLoginPage, QObject):
    def constructor(self, parent):
        KFELog().l("\t\t   KFELoginWindow.constructor()")
        QObject.__init__(self, parent)
        self.signingInPage = KFESigningInPage()
        self.accountPage   = KFEAccountPage(self)

    def show(self):
        KFELog().l("\t\tKFELoginWindow.show()\n\t --> ")
        self.parent().switchToWidget(self.accountPage)
    
    def setAccountList(self, accountList):
        KFELog().l("\t\tKFELoginWindow.setAccountList()\n\t --> ")
        self.accountPage.setAccountList(accountList)

    def onSigningIn(self):
        KFELog().l("\t\tKFELoginWindow.onSigningIn()\n\t --> ")
        self.parent().switchToWidget(self.signingInPage)

    def onSigningOut(self):
        KFELog().l("\t\tKFELoginWindow.onSigningOut()\n\t --> ")
        self.parent().switchToWidget(self.accountPage)

    def onConnecting(self, progress, message):
        KFELog().l("\t\tKFELoginWindow.onConnecting()\n\t --> ")
        self.signingInPage.onConnecting(progress, message)

    # If we don't specify this, when calling hide(), base.aMSNLoginWindow's hide()
    # method gets called, resulting in a "NotImplementedException"

    def hide(self):
        pass
        