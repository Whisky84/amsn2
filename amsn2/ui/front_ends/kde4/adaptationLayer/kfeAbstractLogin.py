# -*- coding: utf-8 -*-

from kfeLog     import KFELog

from kfeViews   import KFEAccount
from amsn2.ui   import base


class KFEAbstractLoginPage (base.aMSNLoginWindow): # removed KFEWindow mother class
    def __init__(self, amsn_core, parent):
        KFELog().l("KFEAbstractLoginPage.__init__()\n\t")
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
        KFELog().l("KFEAbstractLoginPage.constructor()\tNotImplementedError\n")

    def getAccountFromEmail(self, email):
        KFELog().l("KFEAbstractLoginPage.getAccountFromEmail()\n")
        return KFEAccount.fromAccountView(
                self.amsn_core._ui_manager.get_accountview_from_email(email) )
        
    def setAccountList(self, accountList):
        KFELog().l("KFEAbstractLoginPage.setAccountList()\tNotImplementedError\n")

    def onLoginRequested(self, account):
        KFELog().l("KFEAbstractLoginPage.onLoginRequested()\n")
        self.amsn_core.signin_to_account(self, account)
        
    def onSigningIn(self):
        KFELog().l("KFEAbstractLoginPage.onSigningIn()\tNotImplementedError\n")

    def onSigningOut(self):
        KFELog().l("KFEAbstractLoginPage.onSigningOut()\tNotImplementedError\n")

    def onConnecting(self):
        KFELog().l("KFEAbstractLoginPage.onConnecting()\tNotImplementedError\n")

