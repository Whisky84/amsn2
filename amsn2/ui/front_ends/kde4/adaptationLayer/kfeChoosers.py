
from kfeLog import KFELog

from amsn2.ui import base

class KFEFileChooser(base.aMSNFileChooser):
    def __init__(self, filters, directory, callback, title = "aMSN Display Picture Chooser"):
        KFELog().l("KFEFileChooser.__init__()", False, 3)

    def set_title(self, title):
        KFELog().l("KFEFileChooser.set_title()", False, 3)

    def show(self):
        KFELog().l("KFEFileChooser.show()", False, 3)





class KFEDisplayPicChooser(base.aMSNDPChoseer):
    def __init__(self, callback, backend_manager):
        KFELog().l("KFEDisplayPicChooser.__init__()", False, 3)

    def set_title(self, title):
        KFELog().l("KFEDisplayPicChooser.set_title()", False, 3)

    def show(self):
        KFELog().l("KFEDisplayPicChooser.show()", False, 3)