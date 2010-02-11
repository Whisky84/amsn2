# -*- coding: utf-8 -*-

from amsn2.ui import base

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from amsn2.ui.front_ends.kde4.widgets import KPresenceComboBox

#TODO: Consider reimplementing KLoginPage as a Qt state machine


class KLoginPage(QWidget):
    def __init__(self, amsn_core, parent = None):
        QWidget.__init__(self, parent)
        self._core = amsn_core
        
        self._account_views = None
        
        lay = QVBoxLayout()
        
        self.dp = QLabel()
        _, dp_path = self._core._theme_manager.get_value("dp_amsn")
        self.dp.setPixmap(QPixmap(dp_path))
        self.dp.setAlignment(Qt.AlignCenter)
        
        
        self.account_combo = KComboBox()
        self.account_combo.setEditable(1)
        self.account_combo.setDuplicatesEnabled(False) #not working... why?
        self.account_combo.setInsertPolicy(KComboBox.NoInsert)
        self.account_combo_completion = self.account_combo.completionObject(True)
        self.is_account_valid = False
        #TODO: Check signal propagation - loop risk!
        QObject.connect(self.account_combo, SIGNAL("currentIndexChanged(int)"), self.qslot_set_account)
        QObject.connect(self.account_combo, SIGNAL("editTextChanged(QString)"), self.qslot_account_combo_text_changed)
        
        self.password_edit = KLineEdit()
        self.password_edit.setPasswordMode()
        self.is_there_some_password = False
        QObject.connect(self.password_edit, SIGNAL("textChanged(QString)"), self.qslot_password_text_changed)
        
        self.presence_combo = KPresenceComboBox(self._core)
        
        self.save_account = QCheckBox(i18n("Remember this account"))
        self.save_password = QCheckBox(i18n("Save password"))
        self.autologin = QCheckBox(i18n("Login automagically"))
        
        self.login_btn = KPushButton(i18n("Login"))
        QObject.connect(self.login_btn, SIGNAL("clicked()"), self.qslot_start_login)
        
        #lay.addWidget(self.dp_view)
        lay.addWidget(self.dp)
        lay.addWidget(self.account_combo)
        lay.addWidget(self.password_edit)
        lay.addWidget(self.presence_combo)
        lay.addWidget(self.save_account)
        lay.addWidget(self.save_password)
        lay.addWidget(self.autologin)
        
        lay.addWidget(self.login_btn)
        self.setLayout(lay)
        
        
    def set_accounts(self, accountviews):
        """ This method will be called when the core needs the login window to
        let the user select among some accounts.

        @param accountviews: list of accountviews describing accounts
        The first one in the list
        should be considered as default. """
        self._account_views = accountviews
        #clear the content of account_combo (setDuplicatesEnabled doesn't seem to work)
        self.account_combo.clear()
        self.account_combo_completion.clear()
        i=0
        for a in accountviews:
            self.account_combo.addItem(a.email)
            self.account_combo_completion.addItem(a.email)
        if accountviews[0]:
            self.account_combo.setCurrentIndex(self.account_combo.findText(accountviews[0].email)) #shouldn't this be done by qslot_set_account?
            self.qslot_set_account(self.account_combo.currentIndex())
        
    
    # -------------------- QT_SLOTS
    
    
    def qslot_account_combo_text_changed(self, new_text): #new text is a QString
        index = self.account_combo.findText(new_text)
        if is_mail_valid(str(new_text)):
            self.is_account_valid = True
            if index > -1:
                self.set_account_(index)
            else:
                self.clear_login_settings()
        else:
            self.clear_login_settings()
            self.is_account_valid = False
        self.widget_enabled_status_refresh()
           
        
    def qslot_password_text_changed(self, pwd):
        if pwd.isEmpty():
            self.is_there_some_password = False
        else:
            self.is_there_some_password = True
        self.widget_enabled_status_refresh()
        
        
    def qslot_set_account(self, acc_index):
        #mail & password:
        accountview = self._core._ui_manager.get_accountview_from_email(str(self.account_combo.itemText(acc_index)))
        if accountview.password:
            self.password_edit.setText(accountview.password)
        else:
            self.password_edit.clear()
        #presence:
        self.presence_combo.setPresence(accountview.presence)
        #checkboxes:
        self.save_account.setChecked(accountview.save)
        self.save_password.setChecked(accountview.save_password)
        self.autologin.setChecked(accountview.autologin)
        
        
    def qslot_start_login(self):
        accv = self.core._ui_manager.get_accountview_from_email(str(self.account_combo.currentText()))
        if accv is None:
            accv = AccountView(self.core, str(self.account_combo.currentText()))

        accv.password = str(self.password_edit.text())
        accv.presence = self.presence_combo.presence()
        accv.save = self.save_account.isChecked()
        accv.save_password = self.save_password.isChecked()
        accv.autologin = self.autologin.isChecked()
        
        self.core.signin_to_account(self, accv)
        
        
    # -------------------- OTHER_METHODS
    
    
    def clear_login_settings(self):
        self.password_edit.clear()
        self.presence_combo.setCurrentIndex(self.presence_combo.findData(self.core.Presence.ONLINE))
        self.save_account.setChecked(False)
        self.save_password.setChecked(False)
        self.autologin.setChecked(False)
        
        
    def widget_enabled_status_refresh(self):
        if self.is_account_valid:
            validity = True
            if self.is_there_some_password:
                self.login_btn.setEnabled(True)
            else: 
                self.login_btn.setEnabled(False)
        else:
            validity = False
            self.login_btn.setEnabled(False)
        self.password_edit.setEnabled(validity)
        self.presence_combo.setEnabled(validity)
        self.save_account.setEnabled(validity)
        self.save_password.setEnabled(validity)
        self.autologin.setEnabled(validity)
    
        
# -------------------- FUNCTIONS


GENERIC_DOMAINS = "aero", "asia", "biz", "cat", "com", "coop", \
    "edu", "gov", "info", "int", "jobs", "mil", "mobi", "museum", \
    "name", "net", "org", "pro", "tel", "travel"
    

def is_mail_valid(emailaddress, domains = GENERIC_DOMAINS):
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
        