from kfeLog import KFELog
from amsn2.ui import base

class KFESplashScreen(base.aMSNSplashScreen):
    def __init__(self, amsn_core, parent):
        KFELog().l("NotImplementedError:\tKFESplashScreen.__init__()")
        
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
        KFELog().l("NotImplementedError:\tKFESplashScreen.show()")

    def hide(self):
        KFELog().l("NotImplementedError:\tKFESplashScreen.hide()")

    def setText(self, text):
        KFELog().l("NotImplementedError:\tKFESplashScreen.setText()")

    def setImage(self, image):
        KFELog().l("NotImplementedError:\tKFESplashScreen.setImage()")