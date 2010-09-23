# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4 import adaptationLayer
from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog
from amsn2.core     import  aMSNCore

from PyKDE4.kdeui   import  KApplication

from PyKDE4.kdecore import  KAboutData,     \
                            KCmdLineArgs,   \
                            ki18n

from PyQt4.QtCore   import  QObject,    \
                            QTimer,     \
                            SIGNAL

import gobject
import signal
import sys
import os

class KFEMainLoop(adaptationLayer.KFEAbstractMainLoop):
    """ This Interface represents the main loop abstraction of the application.
    Everythin related to the main loop will be delegates here """

    def constructor(self):
        #Qt event loop crashes if we don't set this
        os.putenv("QT_NO_GLIB","1")
        self.aboutData = KAboutData("amsn2", "", ki18n("aMSN2"), "0.001")
        KCmdLineArgs.init(sys.argv[2:], self.aboutData)
        self.app = KApplication()
        KFELog().l("KFEMainLoop.constructor()\n")
        #What are these for? :P
        self.gmainloop = gobject.MainLoop()
        self.gcontext = self.gmainloop.get_context()


    def run(self):
        """ This will run the the main loop"""
        KFELog().l("KFEMainLoop.run()\n")
        self.idleTimer = QTimer(KApplication.instance())
        QObject.connect(self.idleTimer, SIGNAL('timeout()'), self.onIdle)
        self.idleTimer.start(100)
        signal.signal(signal.SIGINT, self.on_keyboard_interrupt)
        self.app.exec_()


    #What are these methods for?
    def addIdler(self, idlerFunc):
        """
        This will add an idler function into the main loop's idler

        @type func: function
        """
        KFELog().l("KFEMainLoop.idler_add()\tNotImplementedError\n")


    def addTimer(self, delay, func):
        """
        This will add a timer into the main loop which will call a function

        @type delay:
        @type func: function
        """
        KFELog().l("KFEMainLoop.timer_add()\tNotImplementedError\n")
        

    def quit(self):
        """ This will be called when the core wants to exit """
        KFELog().l("KFEMainLoop.quit()")
        self.app.quit()


    # -------------------- QT_SLOTS

    def onIdle(self):
        iter = 0
        while iter < 10 and self.gcontext.pending():
            self.gcontext.iteration()
            iter += 1

    def on_keyboard_interrupt(self, signal, stack):
        aMSNCore().quit()




