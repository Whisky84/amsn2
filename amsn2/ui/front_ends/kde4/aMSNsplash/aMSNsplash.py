# -*- coding: utf-8 -*-

from amsn2.ui import base

class aMSNSplashScreen(base.aMSNSplashScreen):
    """ This interface will represent the splashscreen of the UI"""
    def __init__(self, amsn_core, parent):
        """Initialize the interface. You should store the reference to the core in here
        as well as a reference to the window where you will show the splash screen
        """
        print "NotImplementedError:\t\taMSNSplashScreen.__init__()"

    def show(self):
        """ Draw the splashscreen """
        print "NotImplementedError:\t\taMSNSplashScreen.show()"

    def hide(self):
        """ Hide the splashscreen """
        print "NotImplementedError:\t\taMSNSplashScreen.hide()"

    def set_text(self, text):
        """ Shows a different text inside the splashscreen """
        print "NotImplementedError:\t\taMSNSplashScreen.set_text()"

    def set_image(self, image):
        """ Set the image to show in the splashscreen. This is an ImageView object """
        print "NotImplementedError:\t\taMSNSplashScreen.set_image()"

