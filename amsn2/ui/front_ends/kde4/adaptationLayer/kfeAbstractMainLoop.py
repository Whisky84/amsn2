# -*- coding: utf-8 -*-

from amsn2.ui import base

class KFEAbstractMainLoop (base.aMSNMainLoop):
    def __init__(self, amsn_core):
        print "\t\t\t\tKFEAbstractMainLoop.__init__()"
        self.amsn_core = amsn_core
        self.constructor()

    #CORE SIDE INTERFACE
    #def run(self):
        #this method has already a good interface

    def idler_add(self, func):
        self.wrappedClass.addIdler(self, func)

    def timer_add(self, delay, func):
        self.wrappedClass.AddTimer(self, delay, func)

    #def quit(self):
        #this method has already a good interface
        
    #FRONT END INTERFACE
    def constructor(self):
        print "NotImplementedError:\t\tKFEAbstractMainLoop.constructor()"
    
    def run(self):
        print "NotImplementedError:\t\tKFEAbstractMainLoop.run()"

    def addIdler(self, idlerFunc):
        print "NotImplementedError:\t\tKFEAbstractMainLoop.addIdler()"

    def addTimer(self, delay, func):
        print "NotImplementedError:\t\tKFEAbstractMainLoop.addTimer()"

    def quit(self):
        print "NotImplementedError:\t\tKFEAbstractMainLoop.quit()"
        