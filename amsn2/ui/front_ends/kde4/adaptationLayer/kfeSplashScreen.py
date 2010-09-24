from kfeLog import KFELog
from amsn2.ui import base

class KFESplashScreen(base.aMSNSplashScreen):
    def __init__(self, amsn_core, parent):
        KFELog().l("KFESplashScreen.__init__()", False, 2)
        
    #CORE SIDE INTERFACE
    #def show(self):
        #this method has already a good interface

    #def hide(self):
        #this method has already a good interface

    def set_text(self, text):
        self.setText(text)

    def set_image(self, image):
        self.setImage(self, image)

    #FRONT END SIDE INTERFACE
    def show(self):
        KFELog().l("KFESplashScreen.show()", False, 2)

    def hide(self):
        KFELog().l("NKFESplashScreen.hide()", False, 2)

    def setText(self, text):
        KFELog().l("KFESplashScreen.setText()", False, 2)

    def setImage(self, image):
        KFELog().l("KFESplashScreen.setImage()", False, 2)