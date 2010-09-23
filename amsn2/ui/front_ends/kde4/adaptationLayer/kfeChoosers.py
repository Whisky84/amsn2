
from kfeLog import KFELog

from amsn2.ui import base

class KFEFileChooser(base.aMSNFileChooser):
    def __init__(self, filters, directory, callback, title = "aMSN Display Picture Chooser"):
        KFELog().l("NotImplementedError:\tKFEFileChooser.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError:\tKFEFileChooser.set_title()")

    def show(self):
        KFELog().l("NotImplementedError:\tKFEFileChooser.show()")





class KFEDisplayPicChooser(base.aMSNDPChoseer):
    def __init__(self, callback, backend_manager):
        KFELog().l("NotImplementedError:\tKFEDisplayPicChooser.__init__()")

    def set_title(self, title):
        KFELog().l("NotImplementedError:\tKFEDisplayPicChooser.set_title()")

    def show(self):
        KFELog().l("NotImplementedError:\tKFEDisplayPicChooser.show()")