# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.frontend.widgets  import  KFEPresenceCombo

from amsn2.ui.front_ends.kde4.adaptationLayer   import  kfeViews, KFELog
from amsn2.ui.front_ends.kde4.adaptationLayer   import  KFEPresence,    \
                                                        KFEThemeManager
import papyon

from PyKDE4.kdeui   import  KComboBox,      \
                            KLineEdit,      \
                            KPushButton

from PyKDE4.kdecore import  i18n

from PyQt4.QtGui    import  QCheckBox,      \
                            QLabel,         \
                            QVBoxLayout,    \
                            QPixmap,        \
                            QWidget

from PyQt4.QtCore   import  QObject,        \
                            Qt,             \
                            SIGNAL


#TODO: Consider reimplementing KFEAccountPage as a Qt state machine


class KFEAccountPage(QWidget):
    def __init__(self, loginPage, parent=None):
        KFELog().l("\t\t      KFEAccountPage.__init__()")
        QWidget.__init__(self, parent)
        self.loginPage = loginPage
        self.accountList = None
        
        lay = QVBoxLayout()
        
        self.displayPic = QLabel()
        themeManager = KFEThemeManager()
        displayPicPath = themeManager.pathOf("dp_amsn")
        self.displayPic.setPixmap(QPixmap(displayPicPath))
        self.displayPic.setAlignment(Qt.AlignCenter)
        
        
        self.accountCombo = KComboBox()
        self.accountCombo.setEditable(1)
        self.accountCombo.setDuplicatesEnabled(False) #not working... why?
        self.accountCombo.setInsertPolicy(KComboBox.NoInsert)
        self.accountComboCompletion = self.accountCombo.completionObject(True)
        self.isAccountValid = False
        #TODO: Check signal propagation - loop risk!
        QObject.connect(self.accountCombo, SIGNAL("currentIndexChanged(int)"), self.onChosenAccountChanged)
        QObject.connect(self.accountCombo, SIGNAL("editTextChanged(QString)"), self.onAccountComboTextChanged)
        
        self.passwordEdit = KLineEdit()
        self.passwordEdit.setPasswordMode()
        self.isThereSomePassword = False
        QObject.connect(self.passwordEdit, SIGNAL("textChanged(QString)"), self.onPasswordTextChanged)
        
        self.presenceValues = KFEPresence().presenceValues()
        self.presenceCombo = KFEPresenceCombo()
        
        self.saveAccountChk = QCheckBox(i18n("Remember this account"))
        self.savePasswordChk = QCheckBox(i18n("Save password"))
        self.autoLoginChk = QCheckBox(i18n("Login automagically"))
        
        self.loginBtn = KPushButton(i18n("Login"))
        QObject.connect(self.loginBtn, SIGNAL("clicked()"), self.startLogin)
        
        #lay.addWidget(self.dp_view)
        lay.addWidget(self.displayPic)
        lay.addWidget(self.accountCombo)
        lay.addWidget(self.passwordEdit)
        lay.addWidget(self.presenceCombo)
        lay.addWidget(self.saveAccountChk)
        lay.addWidget(self.savePasswordChk)
        lay.addWidget(self.autoLoginChk)
        lay.addWidget(self.loginBtn)
        self.setLayout(lay)
        
        
    def setAccountList(self, accountList):
        KFELog().l("\t\t      KFEAccountPage.setAccountList()")
        """ This method will be called when the core needs the login window to
        let the user select among some accounts.

        @param accountviews: list of accountviews describing accounts
        The first one in the list
        should be considered as default. """
        self.accountList = accountList
        #clear the content of accountCombo (setDuplicatesEnabled doesn't seem to work)
        self.accountCombo.clear()
        self.accountComboCompletion.clear()
        for account in accountList:
            self.accountCombo.addItem(account.email)
            self.accountComboCompletion.addItem(account.email)
      
        #if accountviews[0]:
        #    self.accountCombo.setCurrentIndex(self.accountCombo.findText(accountviews[0].email)) #shouldn't this be done by qslot_set_account?
        #    self.qslot_set_account(self.accountCombo.currentIndex())
        
    
    # -------------------- QT_SLOTS
    
    
    def onAccountComboTextChanged(self, newText): #new text is a QString
        index = self.accountCombo.findText(newText)
        if isValidMail(str(newText)):
            self.isAccountValid = True
            if index > -1:
                self.onChosenAccountChanged(index)
            else:
                self.clearLoginForm()
        else:
            self.clearLoginForm()
            self.isAccountValid = False
        self.widgetEnabledStatusRefresh()
           
        
    def onPasswordTextChanged(self, pwd):
        if pwd.isEmpty():
            self.isThereSomePassword = False
        else:
            self.isThereSomePassword = True
        self.widgetEnabledStatusRefresh()
        
        
    def onChosenAccountChanged(self, acc_index):
        #mail & password:
        #print "DEBUG:\t\t\t\tKFEAccountPage.onChosenAccountChanged(): email=%s" % (str(self.accountCombo.itemText(acc_index)))
        account = self.loginPage.getAccountFromEmail(str(self.accountCombo.itemText(acc_index)))
        if account.password:
            self.passwordEdit.setText(account.password)
        else:
            self.passwordEdit.clear()
        #presence:
        self.presenceCombo.setPresence(account.presence)
        #checkboxes:
        self.saveAccountChk.setChecked(account.save)
        KFELog().l("DEBUG:\t\t      KFEAccountPage.onChosenAccountChanged() -> I'm about to read savePassword")
        self.savePasswordChk.setChecked(account.savePassword)
        KFELog().l("DEBUG:\t\t      KFEAccountPage.onChosenAccountChanged() -> I'm about to read autoLogin")
        self.autoLoginChk.setChecked(account.autoLogin)
        
        
    def startLogin(self):
        selectedAccount = self.loginPage.getAccountFromEmail(str(self.accountCombo.currentText()))
        if selectedAccount is None:
            KFELog().l("DEBUG:\t\t      KFEAccountPage.startLogin(): selectedAccount is None")
            selectedAccount = kfeViews.KFEAccount(str(self.accountCombo.currentText()))

        selectedAccount.password = str(self.passwordEdit.text())
        selectedAccount.presence = self.presenceCombo.presence()
        selectedAccount.save = self.saveAccountChk.isChecked()
        KFELog().l("DEBUG:\t\t      KFEAccountPage.startLogin() -> I'm about to write savePassword")
        selectedAccount.savePassword = self.savePasswordChk.isChecked()
        KFELog().l("DEBUG:\t\t      KFEAccountPage.startLogin() -> I'm about to wite autoLogin")
        selectedAccount.autoLogin = self.autoLoginChk.isChecked()
        
        self.loginPage.onLoginRequested(selectedAccount)
        
        
    # -------------------- OTHER_METHODS
    
    
    def clearLoginForm(self):
        self.passwordEdit.clear()
        self.presenceCombo.setPresence(papyon.Presence.ONLINE)
        self.saveAccountChk.setChecked(False)
        self.savePasswordChk.setChecked(False)
        self.autoLoginChk.setChecked(False)
        
        
    def widgetEnabledStatusRefresh(self):
        if self.isAccountValid:
            validity = True
            if self.isThereSomePassword:
                self.savePasswordChk.setEnabled(True)
                self.loginBtn.setEnabled(True)
            else: 
                self.savePasswordChk.setEnabled(False)
                self.loginBtn.setEnabled(False)
        else:
            validity = False
            self.loginBtn.setEnabled(False)
        self.passwordEdit.setEnabled(validity)
        self.presenceCombo.setEnabled(validity)
        self.saveAccountChk.setEnabled(validity)
        #self.savePasswordChk.setEnabled(validity)
        self.autoLoginChk.setEnabled(validity)
    
        
# -------------------- FUNCTIONS


GENERIC_DOMAINS = "aero", "asia", "biz", "cat", "com", "coop", \
    "edu", "gov", "info", "int", "jobs", "mil", "mobi", "museum", \
    "name", "net", "org", "pro", "tel", "travel"
    

def isValidMail(emailaddress, domains = GENERIC_DOMAINS):
    """Checks for a syntactically invalid email address.
    Taken from http://commandline.org.uk/python/email-syntax-check/"""

    # Email address must be 7 characters in total.
    if len(emailaddress) < 7:
        return False # Address too short.

    # Split up email address into parts.
    try:
        localpart, domainname = emailaddress.rsplit('@', 1)
        host, toplevel = domainname.rsplit('.', 1)
    except ValueError:
        return False # Address does not have enough parts.

    # Check for Country code or Generic Domain.
    if len(toplevel) != 2 and toplevel not in domains:
        return False # Not a domain name.

    for i in '-_.%+.':
        localpart = localpart.replace(i, "")
    for i in '-_.':
        host = host.replace(i, "")

    if localpart.isalnum() and host.isalnum():
        return True # Email address is fine.
    else:
        return False # Email address has funny characters.
        