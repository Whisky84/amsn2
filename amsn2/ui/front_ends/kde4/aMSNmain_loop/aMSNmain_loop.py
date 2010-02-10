# -*- coding: utf-8 -*-

import os
import sys

from amsn2.ui import base

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from PyQt4.QtCore import *
from PyQt4.QtCore import SIGNAL
import gobject


class aMSNMainLoop(base.aMSNMainLoop):
    """ This Interface represents the main loop abstraction of the application.
    Everythin related to the main loop will be delegates here """
    def __init__(self, amsn_core):
        """
        @type amsn_core: aMSNCore
        """
        print "\t\t\t\taMSNMainLoop.__init__()"
        self._core = amsn_core
        #Qt event loop crashes if we don't set this
        os.putenv("QT_NO_GLIB","1") 
        self.aboutData = KAboutData("amsn2", "", ki18n("aMSN2"), "0.001")
        KCmdLineArgs.init(sys.argv[2:], self.aboutData)
        self.app = KApplication()
        #What are these for? :P
        self.gmainloop = gobject.MainLoop()
        self.gcontext = self.gmainloop.get_context()


    def run(self):
        """ This will run the the main loop"""
        print "\t\t\t\taMSNMainLoop.run()"
        self.idletimer = QTimer(KApplication.instance())
        QObject.connect(self.idletimer, SIGNAL('timeout()'), self.qslot_on_idle)
        self.idletimer.start(100)
        self.app.exec_()

    
    #What are these methods for? 
    def idler_add(self, func):
        """
        This will add an idler function into the main loop's idler

        @type func: function
        """
        print "NotImplementedError:\t\taMSNMainLoop.idler_add()"
        

    def timer_add(self, delay, func):
        """
        This will add a timer into the main loop which will call a function

        @type delay:
        @type func: function
        """
        print "NotImplementedError:\t\taMSNMainLoop.timer_add()"
        

    def quit(self):
        """ This will be called when the core wants to exit """
        print "\t\t\t\taMSNMainLoop.quit()"
        self.app.quit()
        
    
    # -------------------- QT_SLOTS
    
    def qslot_on_idle(self):
        iter = 0
        while iter < 10 and self.gcontext.pending():
            self.gcontext.iteration()
            iter += 1
            

