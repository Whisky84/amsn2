# -*- coding: utf-8 -*-

from kfeLog import KFELog

from amsn2.ui       import base
from amsn2.core     import aMSNCore

from PyKDE4.kdeui   import KMessageBox

class KFEAbstractErrorWindow (base.aMSNErrorWindow):
    def __init__(self, error_text, title = "aMSN Error"):
        KFELog().l("KFEAbstractErrorWindow.__init__()", False, 1)
        self.message = error_text
        self.title = title
        
    def set_title(self, title):
        KFELog().l("KFEAbstractErrorWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEErrorWindow.show()", False, 1)
        main_window = aMSNCore().get_main_window()
        KMessageBox.error(main_window, self.message, self.title)




class KFEAbstractNotificationWindow (base.aMSNNotificationWindow):
    def __init__(self, notification_text, title = "aMSN Notification"):
        KFELog().l("KFEAbstractNotificationWindow.__init__()", False, 1)
        self.message = notification_text
        self.title = title

    def set_title(self, title):
        KFELog().l("KFEAbstractNotificationWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEAbstractNotificationWindow.show()", False, 1)
        main_window = aMSNCore().get_main_window()
        KMessageBox.information(main_window, self.message, self.title)




class KFEAbstractDialogWindow (base.aMSNDialogWindow):
    def __init__(self, message, actions, title = "aMSN Dialog"):
        KFELog().l("KFEAbstractDialogWindow.__init__()", False, 1)
        self.message = message
        self.title = title
        self.actions = actions
        KFELog().d(str(actions)+"|||"+repr(actions), "KFEAbstractDialogWindow.__init__()")

    def set_title(self, title):
        KFELog().l("KFEAbstractDialogWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEAbstractDialogWindow.show()", False, 1)
        main_window = aMSNCore().get_main_window()
        ans = KMessageBox.questionYesNo(main_window, self.message, self.title)
        if ans == KMessageBox.Yes:
            KFELog().d("Yes pressed", "KFEAbstractDialogWindow.show()")
            self.actions[0][1]()
        elif ans == KMessageBox.No:
            KFELog().d("No pressed", "KFEAbstractDialogWindow.show()")
            self.actions[1][1]()
        else:
            KFELog().d("WTF?!", "KFEAbstractDialogWindow.show()")




class KFEAbstractContactInputWindow (base.aMSNContactInputWindow):
    def __init__(self, message, callback, groupviews, title = "aMSN Contact Input"):
        KFELog().l("KFEAbstractContactInputWindow.__init__()", True, 1)
        self.callback = callback
        main_window = aMSNCore().get_main_window()
        self.constructor(main_window)
        
        
    #CORE SIDE INTERFACE
    def set_title(self, title):
        self.setTitle(self, title)

    #def show(self):
        #this method has already a good interface

    #FRONT END SIDE INTERFACE
    def constructor(self):
        KFELog().l("KFEAbstractContactInputWindow.constructor()", False, 2)

    def onContactAddRequest(self, address):
        KFELog().l("KFEAbstractContactInputWindow.onContactAddRequest()", 1)
        self.callback(address)
        
    def setTitle(self, title):
        KFELog().l("KFEAbstractContactInputWindow.setTitle()", False, 2)
        
    def show(self):
        KFELog().l("KFEAbstractContactInputWindow.show()", False, 2)
        




class KFEAbstractGroupInputWindow (base.aMSNGroupInputWindow):
    def __init__(self, message, callback, contactviews, title = "aMSN Group Input"):
        KFELog().l("KFEAbstractGroupInputWindow.__init__()", True, 1)
        self.constructor()
        KFELog().d("callback: %s, message: %s, contactviews: %s, title: %s " % \
            (repr(callback), message, repr(contactviews), title))

    #CORE SIDE INTERFACE
    def set_title(self, title):
        self.setTitle(self, title)

    def set_title(self, title):
        self.setTitle(self, title)
        
    #def show(self):
        #this method has already a good interface

    #FRONT END SIDE INTERFACE
    def constructor(self):
        KFELog().l("KFEAbstractGroupInputWindow.constructor()", False, 2)

    def setTitle(self, title):
        KFELog().l("KFEAbstractGroupInputWindow.setTitle()", False, 2)

    def show(self):
        KFELog().l("KFEAbstractGroupInputWindow.show()", False, 2)





class KFEAbstractContactDeleteWindow (base.aMSNContactDeleteWindow):
    #now this is subsituted by KFEAbstractContactInputWindow. they have same behaviour
    def __init__(self, message, callback, contactviews, title = "aMSN Delete Contact"):
        KFELog().l("KFEAbstractContactDeleteWindow.__init__()", False, 2)

    def set_title(self, title):
        KFELog().l("KFEAbstractContactDeleteWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEAbstractContactDeleteWindow.show()", False, 2)





class KFEAbstractGroupDeleteWindow (base.aMSNGroupDeleteWindow):
    def __init__(self, message, callback, groupviews, title = "aMSN Delete Group"):
        KFELog().l("KFEAbstractGroupDeleteWindow.__init__()", False, 2)

    def set_title(self, title):
        KFELog().l("KFEAbstractGroupDeleteWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEGroupDeleteWindow.show()", False, 2)