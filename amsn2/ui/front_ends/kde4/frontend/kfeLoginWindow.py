# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog


from mainWindowPages    import  KFEAccountPage,   \
                                KFESigningInPage

from amsn2.ui.front_ends.kde4 import adaptationLayer

from PyQt4.QtCore       import  QObject

class KFELoginWindow (adaptationLayer.KFEAbstractLoginPage, QObject):
    def constructor(self, parent):
        KFELog().l("KFELoginWindow.constructor()")
        QObject.__init__(self, parent)
        self.signingInPage = KFESigningInPage()
        self.accountPage   = KFEAccountPage(self)

    def show(self):
        KFELog().l("KFELoginWindow.show()",  True)
        self.parent().switchToWidget(self.accountPage)
    
    def setAccountList(self, accountList):
        KFELog().l("KFELoginWindow.setAccountList()", True)
        self.accountPage.setAccountList(accountList)

    def onSigningIn(self):
        KFELog().l("KFELoginWindow.onSigningIn()", True)
        self.parent().switchToWidget(self.signingInPage)

    def onSigningOut(self):
        KFELog().l("KFELoginWindow.onSigningOut()", True)
        self.parent().switchToWidget(self.accountPage)

    def onConnecting(self, progress, message):
        KFELog().l("KFELoginWindow.onConnecting()", True)
        self.signingInPage.onConnecting(progress, message)

    # If we don't specify this, when calling hide(), base.aMSNLoginWindow's hide()
    # method gets called, resulting in a "NotImplementedException"

    def hide(self):
        pass
        