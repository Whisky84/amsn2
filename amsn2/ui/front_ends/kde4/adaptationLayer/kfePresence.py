# -*- coding: utf-8 -*-

from amsn2.core import aMSNCore
import papyon

#class KFEPresence:
    #__shared_state = {}
    #def __init__(self):
        #self.__dict__ = KFEPresence.__shared_state

    #def setCore(self, amsn_core):
        ##the whole core or just the presences?
        #self.amsn_core = amsn_core

    #def presenceValues(self):
        #return self.amsn_core.p2s


class KFEPresence:
    def __init__(self, presence = papyon.Presence.ONLINE):
        self.state = presence

    def state(self):
        return self.state

    def setState(self, presence):
        if presence is not papyon.Presence:
            pass
        self.state = presence

    def __str__(self):
        return self.presenceValues()[self.state]

    @staticmethod
    def presenceValues():
        return aMSNCore().p2s