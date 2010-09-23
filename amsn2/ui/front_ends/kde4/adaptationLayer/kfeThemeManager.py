# -*- coding: utf-8 -*-

from kfeLog import KFELog

class KFEThemeManager:
    __sharedState = {}
    __MANAGER = None
    def __init__(self):
        if not KFEThemeManager.__MANAGER:
            KFELog().l("** WARNING KFEThemeManager is inizialized without a theme manager!! WARNING **")
            self.__dict__ = {}
        else:
            self.__dict__ = KFEThemeManager.__sharedState

    @staticmethod
    def setManager(manager):
        KFEThemeManager.__MANAGER = manager

    def pathOf(self, identifier):
        _,path = KFEThemeManager.__MANAGER.get_value(identifier)
        return path



#class  KFEThemeManager:

    #class __impl (object):
        #def __init__(self):
            #self.themeManager = KFEThemeManager.MANAGER
        #def pathOf(self, identifier):
            #_,path = self.themeManager.get_value(identifier)
            #return path



    #__INSTANCE = None
    #MANAGER = None

    #def __init__(self):
        #""" Create singleton instance """
        ## Check whether we already have an instance
        #if KFEThemeManager.__INSTANCE is None:
            #if KFEThemeManager.MANAGER is None:
                #print "** WARNING KFEThemeManager is inizialized without a theme manager!! WARNING **"
            ## Create and remember instance
            #KFEThemeManager.__INSTANCE = KFEThemeManager.__impl()

            ## Store instance reference as the only member in the handle
            #self.__dict__['_KFEThemeManager__INSTANCE'] = KFEThemeManager.__INSTANCE

    #@staticmethod
    #def setManager(manager):
        #KFEThemeManager.MANAGER = manager


    #def __getattr__(self, attr):
        #""" Delegate access to implementation """
        #return getattr(self.__INSTANCE, attr)

    #def __setattr__(self, attr, value):
        #""" Delegate access to implementation """
        #return setattr(self.__INSTANCE, attr, value)