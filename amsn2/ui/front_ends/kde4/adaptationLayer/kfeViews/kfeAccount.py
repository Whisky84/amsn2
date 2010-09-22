# -*- coding: utf-8 -*-

from amsn2.views import AccountView,    \
                        ImageView,      \
                        StringView      \

from amsn2.core import  aMSNCore

                        
class KFEAccount(AccountView):
    def __init__(self, email):
        AccountView.__init__(self, aMSNCore(), email)

    def getAutoLogin(self):
        print "\t\t\t\tKFEAccount.getAutoLogin()"
        return self.autologin

    def setAutoLogin(self, bool):
        print "\t\t\t\tKFEAccount.setAutoLogin()"
        self.autologin = bool
        
    def getSavePassword(self):
        print "\t\t\t\tKFEAccount.getSavePassword()"
        return self.save_password
        
    def setSavePassword(self, bool):
        print "\t\t\t\tKFEAccount.setSavePassword()"
        self.save_password = bool

    autoLogin = property(getAutoLogin, setAutoLogin)
    savePassword = property(getSavePassword, setSavePassword)

    @staticmethod
    def fromAccountView(accountView):
        newKfeAccount = KFEAccount(accountView.email)
        newKfeAccount._core     = accountView._core
        newKfeAccount.email     = accountView.email
        newKfeAccount.password  = accountView.password
        newKfeAccount.nick      = accountView.nick
        newKfeAccount.psm       = accountView.psm
        newKfeAccount.presence  = accountView.presence
        newKfeAccount.dp        = accountView.dp
        newKfeAccount.save          = accountView.save
        newKfeAccount.save_password = accountView.save_password
        newKfeAccount.autologin     = accountView.autologin
        newKfeAccount.preferred_ui      = accountView.preferred_ui
        newKfeAccount.preferred_backend = accountView.preferred_backend
        return newKfeAccount