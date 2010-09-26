
from kfeLog import KFELog

from amsn2.core import aMSNCore

from amsn2.ui import base

from PyKDE4.kio import *
from PyKDE4.kdecore  import *

class KFEFileChooser(base.aMSNFileChooserWindow):
    def __init__(self, filters, directory, callback, title = "aMSN Display Picture Chooser"):
        KFELog().l("KFEFileChooser.__init__()", False, 1)
        KFileDialog.__init__(self, KUrl("."), "image/png", aMSNCore().get_main_window())
        KFELog().d("filters, directory, callback: %s, title: %s " % \
        (filters, directory, callback, title))

    def set_title(self, title):
        KFELog().l("KFEFileChooser.set_title()", False, 2)

    #def show(self):
        #KFELog().l("KFEFileChooser.show()", False, 2)





class KFEDisplayPicChooser(KFileDialog, base.aMSNDPChooserWindow):
    def __init__(self, callback, backend_manager, title):
        KFELog().l("KFEDisplayPicChooser.__init__()", False, 1)
        KFELog().d("callback: %s, backend_manager %s, title: %s " % \
        (callback, backend_manager, title))
        self.callback = callback
        self.title = title

    def set_title(self, title):
        KFELog().l("KFEDisplayPicChooser.set_title()", False, 2)

    def show(self):
        KFELog().l("KFEDisplayPicChooser.show()", False, 1)
        chosenImage = KFileDialog.getImageOpenUrl(KUrl("."), aMSNCore().get_main_window(), self.title)
        #msnObject = MSNObject( string representing the account, 
        #aMSNCore()._personalinfo_manager._on_DP_changed(str(chosenImage.toString()))
        #self.callback(str(chosenImage.path()))
        self.callback(KFELog())
        print repr(chosenImage)




        