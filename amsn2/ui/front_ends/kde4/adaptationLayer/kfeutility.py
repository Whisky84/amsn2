
from amsn2.ui import base

class KFEErrorWindow (base.aMSNErrorWindow):
    def __init__(self, error_text, title = "aMSN Error"):
        KFELog().l("NotImplementedError\tKFEErrorWindow.__init__()")
        
    def set_title(self, title):
        KFELog().l("NotImplementedError\tKFEErrorWindow.set_title()")

    def show(self):
        KFELog().l("NotImplementedError\tKFEErrorWindow.show()")





class KFENotificationWindow (base.aMSNNotificationWindow):
    def __init__(self, notification_text, title = "aMSN Notification"):
        KFELog().l("NotImplementedError\tKFENotificationWindow.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError\tKFENotificationWindow.set_title()")

    def show(self):
        KFELog().l("NotImplementedError\tKFENotificationWindow.show()")





class KFEDialogWindow (base.aMSNDialogWindow):
    def __init__(self, message, actions, title = "aMSN Dialog"):
        KFELog().l("NotImplementedError\tKFEDialogWindow.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError\tKFEDialogWindow.set_title()")

    def show(self):
        KFELog().l("NotImplementedError\tKFEDialogWindow.show()")





class KFEContactInputWindow (base.aMSNContactInputWindow):
    def __init__(self, message, callback, groupviews, title = "aMSN Contact Input"):
        KFELog().l("NotImplementedError\tKFEContactInputWindow.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError\tKFEContactInputWindow.set_title()")

    def show(self):
        KFELog().l("NotImplementedError\tKFEContactInputWindow.show()")
        




class KFEGroupInputWindow (base.aMSNGroupInputWindow):
    def __init__(self, message, callback, contactviews, title = "aMSN Group Input"):
        KFELog().l("NotImplementedError\tKFEGroupInputWindow.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError\tKFEGroupInputWindow.set_title()")

    def show(self):
        KFELog().l("NotImplementedError\tKFEGroupInputWindow.show()")





class KFEContactDeleteWindow (base.aMSNContactDeleteWindow):
    def __init__(self, message, callback, contactviews, title = "aMSN Delete Contact"):
        KFELog().l("NotImplementedError\tKFEContactDeleteWindow.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError\tKFEContactDeleteWindow.set_title()")

    def show(self):
        KFELog().l("NotImplementedError\tKFEContactDeleteWindow.show()")





class KFEGroupDeleteWindow (base.aMSNGroupDeleteWindow):
    def __init__(self, message, callback, groupviews, title = "aMSN Delete Group"):
        KFELog().l("NotImplementedError\tKFEGroupDeleteWindow.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError\tKFEGroupDeleteWindow.set_title()")

    def show(self):
        KFELog().l("NotImplementedError\tKFEGroupDeleteWindow.show()")