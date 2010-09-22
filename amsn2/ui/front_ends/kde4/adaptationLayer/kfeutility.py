
from amsn2.ui import base

class KFEErrorWindow (base.aMSNErrorWindow):
    def __init__(self, error_text, title = "aMSN Error"):
        print "NotImplementedError:\t\tKFEErrorWindow.__init__()"
        
    def set_title(self, title):
        print "NotImplementedError:\t\tKFEErrorWindow.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEErrorWindow.show()"





class KFENotificationWindow (base.aMSNNotificationWindow):
    def __init__(self, notification_text, title = "aMSN Notification"):
        print "NotImplementedError:\t\tKFENotificationWindow.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFENotificationWindow.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFENotificationWindow.show()"





class KFEDialogWindow (base.aMSNDialogWindow):
    def __init__(self, message, actions, title = "aMSN Dialog"):
        print "NotImplementedError:\t\tKFEDialogWindow.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFEDialogWindow.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEDialogWindow.show()"





class KFEContactInputWindow (base.aMSNContactInputWindow):
    def __init__(self, message, callback, groupviews, title = "aMSN Contact Input"):
        print "NotImplementedError:\t\tKFEContactInputWindow.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFEContactInputWindow.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEContactInputWindow.show()"
        




class KFEGroupInputWindow (base.aMSNGroupInputWindow):
    def __init__(self, message, callback, contactviews, title = "aMSN Group Input"):
        print "NotImplementedError:\t\tKFEGroupInputWindow.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFEGroupInputWindow.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEGroupInputWindow.show()"





class KFEContactDeleteWindow (base.aMSNContactDeleteWindow):
    def __init__(self, message, callback, contactviews, title = "aMSN Delete Contact"):
        print "NotImplementedError:\t\tKFEContactDeleteWindow.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFEContactDeleteWindow.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEContactDeleteWindow.show()"





class KFEGroupDeleteWindow (base.aMSNGroupDeleteWindow):
    def __init__(self, message, callback, groupviews, title = "aMSN Delete Group"):
        print "NotImplementedError:\t\tKFEGroupDeleteWindow.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFEGroupDeleteWindow.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEGroupDeleteWindow.show()"