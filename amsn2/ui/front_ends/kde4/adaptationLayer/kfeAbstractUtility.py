# -*- coding: utf-8 -*-

from kfeLog import KFELog

from amsn2.ui import base

class KFEAbstractErrorWindow (base.aMSNErrorWindow):
    def __init__(self, error_text, title = "aMSN Error"):
        KFELog().l("KFEAbstractErrorWindow.__init__()", False, 2)
        
    def set_title(self, title):
        KFELog().l("KFEAbstractErrorWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEErrorWindow.show()", False, 2)





class KFEAbstractNotificationWindow (base.aMSNNotificationWindow):
    def __init__(self, notification_text, title = "aMSN Notification"):
        KFELog().l("KFEAbstractNotificationWindow.__init__()", False, 2)

    def set_title(self, title):
        KFELog().l("KFEAbstractNotificationWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEAbstractNotificationWindow.show()", False, 2)





class KFEAbstractDialogWindow (base.aMSNDialogWindow):
    def __init__(self, message, actions, title = "aMSN Dialog"):
        KFELog().l("KFEAbstractDialogWindow.__init__()", False, 2)

    def set_title(self, title):
        KFELog().l("KFEAbstractDialogWindow.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEAbstractDialogWindow.show()", False, 2)





class KFEAbstractContactInputWindow (base.aMSNContactInputWindow):
    def __init__(self, message, callback, groupviews, title = "aMSN Contact Input"):
        KFELog().l("KFEAbstractContactInputWindow.__init__()", True, 1)
        self.constructor()
        KFELog().d("callback: %s, message: %s, groupviews: %s, title: %s " % \
            (repr(callback), message, repr(groupviews), title))
        
    #CORE SIDE INTERFACE
    def set_title(self, title):
        self.setTitle(self, title)

    #def show(self):
        #this method has already a good interface

    #FRONT END SIDE INTERFACE
    def constructor(self):
        KFELog().l("KFEAbstractContactInputWindow.constructor()", False, 2)
        
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