from constants import THEME_FILE
import evas
import edje
import elementary

from amsn2.ui import base

#TODO: del?
class aMSNLoginWindow(elementary.Layout, base.aMSNLoginWindow):
    def __init__(self, amsn_core, win):
        self._core = amsn_core
        self._evas = win._evas
        self._win = win
        self._account_views = []
        self._ui_manager = self._core._ui_manager

        edje.frametime_set(1.0 / 30)

        elementary.Layout.__init__(self, win)
        self.file_set(THEME_FILE, "amsn2/login_screen")

        self._edje = self.edje_get()

        self.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
        self.size_hint_align_set(evas.EVAS_HINT_FILL, evas.EVAS_HINT_FILL)

        sc = elementary.Scroller(self)
        sc.content_min_limit(0, 1)
        sc.policy_set(elementary.ELM_SCROLLER_POLICY_OFF,
                      elementary.ELM_SCROLLER_POLICY_OFF)
        sc.size_hint_weight_set(1.0, 0.0)
        sc.size_hint_align_set(-1.0, -1.0)
        self.content_set("username", sc)
        self.username = elementary.Entry(self)
        self.username.single_line_set(1)
        self.username.size_hint_weight_set(1.0, 0.0)
        self.username.size_hint_align_set(-1.0, -1.0)
        sc.content_set(self.username)
        self.username.show()
        sc.show()

        sc = elementary.Scroller(self)
        sc.content_min_limit(0, 1)
        sc.policy_set(elementary.ELM_SCROLLER_POLICY_OFF,
                      elementary.ELM_SCROLLER_POLICY_OFF)
        sc.size_hint_weight_set(1.0, 0.0)
        sc.size_hint_align_set(-1.0, -1.0)
        self.content_set("password", sc)
        self.password = elementary.Entry(self)
        self.password.single_line_set(1)
        self.password.password_set(1)
        self.password.size_hint_weight_set(1.0, 1.0)
        self.password.size_hint_align_set(-1.0, -1.0)
        sc.content_set(self.password)
        self.password.show()
        sc.show()

        self.presence = elementary.Hoversel(self)
        self.presence.hover_parent_set(self._win)
        for key in self._core.p2s:
            name = self._core.p2s[key]
            _, path = self._core._theme_manager.get_statusicon("buddy_%s" % name)
            if name == 'offline': continue
            def cb(hoversel, it, key):
                hoversel.label_set(it.label_get())
                (icon_file, icon_group, icon_type) = it.icon_get()
                ic = elementary.Icon(hoversel)
                ic.scale_set(0, 1)
                if icon_type == elementary.ELM_ICON_FILE:
                    ic.file_set(icon_file, icon_group)
                else:
                    ic.standart_set(icon_file)
                hoversel.icon_set(ic)
                ic.show()
                self.presence_key = data

            self.presence.item_add(name, path, elementary.ELM_ICON_FILE, cb,
                                   key)

        self.presence_key = self._core.Presence.ONLINE
        self.presence.label_set(self._core.p2s[self.presence_key])
        ic = elementary.Icon(self.presence)
        ic.scale_set(0, 1)
        _, path = self._core._theme_manager.get_statusicon("buddy_%s" %
                            self._core.p2s[self.presence_key])
        ic.file_set(path)
        self.presence.icon_set(ic)
        ic.show()
        self.presence.size_hint_weight_set(0.0, 0.0)
        self.presence.size_hint_align_set(0.5, 0.5)
        self.content_set("presence", self.presence)
        self.presence.show()

        self.save = elementary.Check(self)
        self.save.label_set("Remember Me")
        def cb(obj):
            if obj.state_get():
                self.save_password.disabled_set(False)
            else:
                self.save_password.disabled_set(True)
                self.save_password.state_set(False)
                self.autologin.disabled_set(True)
                self.autologin.state_set(False)
        self.save.callback_changed_add(cb)
        self.content_set("remember_me", self.save)
        self.save.show()

        self.save_password = elementary.Check(self)
        self.save_password.label_set("Remember Password")
        self.save_password.disabled_set(True)
        def cb(obj):
            if obj.state_get():
                self.autologin.disabled_set(False)
            else:
                self.autologin.disabled_set(True)
                self.autologin.state_set(False)
        self.save_password.callback_changed_add(cb)
        self.content_set("remember_password",
                                self.save_password)
        self.save_password.show()

        self.autologin = elementary.Check(self)
        self.autologin.label_set("Auto Login")
        self.autologin.disabled_set(True)
        self.content_set("auto_login", self.autologin)
        self.autologin.show()

        if self._edje.part_exists("signin"):
            self.signin_b = elementary.Button(self)
            self.signin_b.label_set("Sign in")
            self.signin_b.callback_clicked_add(self.__signin_button_cb)
            self.signin_b.show()
            self.content_set("signin", self.signin_b)
        else:
            self._edje.signal_callback_add("signin", "*", self.__signin_cb)

        self._win.child = self
        self.show()

    def set_accounts(self, accountviews):
        #TODO: support more than just 1 account...
        self._account_views = accountviews
        if accountviews:
            #Only select the first one
            acc = accountviews[0]
            self.username.entry_set(acc.email)
            self.password.entry_set(acc.password)

            self.presence_key = acc.presence
            self.presence.label_set(self._core.p2s[self.presence_key])
            ic = elementary.Icon(self.presence)
            ic.scale_set(0, 1)
            _, path = self._core._theme_manager.get_statusicon("buddy_%s" %
                                self._core.p2s[self.presence_key])
            ic.file_set(path)
            self.presence.icon_set(ic)
            ic.show()

            self.save.state_set(acc.save)
            if acc.save:
                self.save_password.disabled_set(False)
            else:
                self.save_password.disabled_set(True)
            self.save_password.state_set(acc.save_password)
            if acc.save_password:
                self.autologin.disabled_set(False)
            else:
                self.autologin.disabled_set(True)
            self.autologin.state_set(acc.autologin)


    def signin(self):
        ### Autologin change: This method is no longer used to tell the core to start the login

        #email = elementary.Entry.markup_to_utf8(self.username.entry_get()).strip()
        #password = elementary.Entry.markup_to_utf8(self.password.entry_get()).strip()
        #accv = self._ui_manager.getAccountViewFromEmail(email)
        #accv.password = password
        #accv.presence = self.presence_key
        #accv.save = self.save.state_get()
        #accv.save_password = self.save_password.state_get()
        #accv.autologin = self.autologin.state_get()
        #self._core.signinToAccount(self, accv)
        pass

    def signout(self):
        pass

    def on_connecting(self, progress, message):
        self._edje.signal_emit("connecting", "")
        msg1 = ""
        msg2 = ""
        try:
            msg1 = message.split("\n")[0]
        except IndexError:
            pass

        try:
            msg2 = message.split("\n")[1]
        except IndexError:
            pass
        self._edje.part_text_set("connection_status", msg1)
        self._edje.part_text_set("connection_status2", msg2)


    def __signin_cb(self, edje_obj, signal, source):
        self._core.signin_to_account(self, self.__get_account())

    def __signin_button_cb(self, bt):
        self._core.signin_to_account(self, self.__get_account())

    def __get_account(self):
        email = elementary.Entry.markup_to_utf8(self.username.entry_get()).strip()
        password = elementary.Entry.markup_to_utf8(self.password.entry_get()).strip()

        accv = self._ui_manager.get_accountview_from_email(email)
        accv.password = password

        accv.presence = self.presence_key

        accv.save = self.save.state_get()
        accv.save_password = self.save_password.state_get()
        accv.autologin = self.autologin.state_get()

        return accv

