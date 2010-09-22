
from amsn2.ui import base

class KFEFileChooser(base.aMSNFileChooser):
    def __init__(self, filters, directory, callback, title = "aMSN Display Picture Chooser"):
        print "NotImplementedError:\t\tKFEFileChooser.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFEFileChooser.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEFileChooser.show()"





class KFEDisplayPicChooser(base.aMSNDPChoseer):
    def __init__(self, callback, backend_manager):
        print "NotImplementedError:\t\tKFEDisplayPicChooser.__init__()"

    def set_title(self, title):
        print "NotImplementedError:\t\tKFEDisplayPicChooser.set_title()"

    def show(self):
        print "NotImplementedError:\t\tKFEDisplayPicChooser.show()"