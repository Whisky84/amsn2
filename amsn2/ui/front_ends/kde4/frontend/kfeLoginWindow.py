# -*- coding: utf-8 -*-

from mainWindowPages    import  KFEAccountPage,   \
                                KFESigningInPage

from amsn2.ui.front_ends.kde4 import adaptationLayer

from PyQt4.QtCore       import  QObject

class KFELoginWindow (adaptationLayer.KFEAbstractLoginPage, QObject):
    def constructor(self, parent):
        print "\t\t\t\tKFELoginWindow.constructor()"
        QObject.__init__(self, parent)
        self.signingInPage = KFESigningInPage()
        self.accountPage   = KFEAccountPage(self)

    def show(self):
        print "\t\t\t\tKFELoginWindow.show()"
        self.parent().switchToWidget(self.accountPage)
    
    def setAccountList(self, accountList):
        print "\t\t\t\t KFELoginWindow.setAccountList()"
        self.accountPage.setAccountList(accountList)

    def onSigningIn(self):
        print "\t\t\t\tKFELoginWindow.onSigningIn()"
        self.parent().switchToWidget(self.signingInPage)

    def onSigningOut(self):
        print "\t\t\t\tKFELoginWindow.onSigningOut()"
        self.parent().switchToWidget(self.accountPage)

    def onConnecting(self, progress, message):
        print "\t\t\t\tKFELoginWindow.onConnecting()"
        self.signingInPage.onConnecting(progress, message)

    # If we don't specify this, when calling hide(), base.aMSNLoginWindow's hide()
    # method gets called, resulting in a "NotImplementedException"

    def hide(self):
        pass
        