# -*- coding: utf-8 -*-

from amsn2.ui import base

class aMSNMainLoop(base.aMSNMainLoop):
    """ This Interface represents the main loop abstraction of the application.
    Everythin related to the main loop will be delegates here """
    def __init__(self, amsn_core):
        """
        @type amsn_core: aMSNCore
        """

        print "NotImplementedError:\t\taMSNMainLoop.__init__()"

    def run(self):
        """ This will run the the main loop"""
        print "NotImplementedError:\t\taMSNMainLoop.run()"

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
        print "NotImplementedError:\t\taMSNMainLoop.quit()"

