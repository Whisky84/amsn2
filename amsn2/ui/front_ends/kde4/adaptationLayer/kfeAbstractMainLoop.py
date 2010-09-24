# -*- coding: utf-8 -*-

from amsn2.ui import base

class KFEAbstractMainLoop (base.aMSNMainLoop):
    def __init__(self, amsn_core):
        print "KFEAbstractMainLoop.__init__()" #here we cannot use KFELog 'cause we don't have a KApplication
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
        KFELog().l("KFEAbstractMainLoop.constructor()", False, 2)
    
    def run(self):
        KFELog().l("KFEAbstractMainLoop.run()", False, 2)

    def addIdler(self, idlerFunc):
        KFELog().l("KFEAbstractMainLoop.addIdler()", False, 2)

    def addTimer(self, delay, func):
        KFELog().l("KFEAbstractMainLoop.addTimer()", False, 2)

    def quit(self):
        KFELog().l("\FEAbstractMainLoop.quit()", False, 2)
        