# -*- coding: utf-8 -*-

from kfeViews   import KFEAccount
from amsn2.ui   import base


class KFEAbstractLoginPage (base.aMSNLoginWindow): # removed KFEWindow mother class
    def __init__(self, amsn_core, parent):
        print "\t\t\t\tKFEAbstractLoginPage.__init__() - " + repr(amsn_core)
        self.amsn_core = amsn_core
        self._account_views = None # The core relies on this to be set...
        self.constructor(parent)

    #CORE SIDE INTERFACE
    def set_accounts(self, accountviews):
        self._account_views = accountviews
        accountList = []
        for account in accountviews:
            accountList.append( KFEAccount.fromAccountView(account) )
        self.setAccountList(accountList)
        
    def signing_in(self):
        self.onSigningIn()

    def signout(self):
        self.onSigningOut()

    def on_connecting(self, progress, message):
        self.onConnecting(progress, message)

    #FRONT END SIDE INTERFACE
    def constructor(self, parent):
        print "NotImplementedError:\t\tKFEAbstractLoginPage.constructor()"

    def getAccountFromEmail(self, email):
        print "\t\t\t\tKFEAbstractLoginPage.getAccountFromEmail()"
        return KFEAccount.fromAccountView(
                self.amsn_core._ui_manager.get_accountview_from_email(email) )
        
    def setAccountList(self, accountList):
        print "NotImplementedError:\t\tKFEAbstractLoginPage.setAccountList()"

    def onLoginRequested(self, account):
        print "\t\t\t\tKFEAbstractLoginPage.onLoginRequested()"
        self.amsn_core.signin_to_account(self, account)
        
    def onSigningIn(self):
        print "NotImplementedError:\t\tKFEAbstractLoginPage.onSigningIn()"

    def onSigningOut(self):
        print "NotImplementedError:\t\tKFEAbstractLoginPage.onSigningOut()"

    def onConnecting(self):
        print "NotImplementedError:\t\tKFEAbstractLoginPage.onConnecting()"

