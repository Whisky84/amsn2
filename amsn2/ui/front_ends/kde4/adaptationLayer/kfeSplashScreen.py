
from amsn2.ui import base

class KFESplashScreen(base.aMSNSplashScreen):
    def __init__(self, amsn_core, parent):
        print "NotImplementedError:\t\tKFESplashScreen.__init__()"
        
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
        print "NotImplementedError:\t\tKFESplashScreen.show()"

    def hide(self):
        print "NotImplementedError:\t\tKFESplashScreen.hide()"

    def setText(self, text):
        print "NotImplementedError:\t\tKFESplashScreen.setText()"

    def setImage(self, image):
        print "NotImplementedError:\t\tKFESplashScreen.setImage()"
        