# -*- coding: utf-8 -*-

from .. kfeLog      import KFELog

from amsn2.views import AccountView,    \
                        ImageView,      \
                        StringView      \

from amsn2.core import  aMSNCore

                        
class KFEAccount (object, AccountView):
    def __init__(self, email):
        AccountView.__init__(self, aMSNCore(), email)
        object.__init__(self)

    def getAutoLogin(self):
        KFELog().l("\t\tKFEAccount.getAutoLogin()")
        return self.autologin

    def setAutoLogin(self, autoLogin):
        KFELog().l("\t\tKFEAccount.setAutoLogin()")
        self.autologin = autoLogin
    
    
    
    def getSavePassword(self):
        KFELog().l("\t\tKFEAccount.getSavePassword()")
        return self.save_password
    def setSavePassword(self, savePassword):
        KFELog().l("\t\tKFEAccount.setSavePassword()")
        self.save_password = savePassword

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
