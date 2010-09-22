# -*- coding: utf-8 -*-

class KFEPresence:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = KFEPresence.__shared_state

    def setCore(self, amsn_core):
        #the whole core or just the presences?
        self.amsn_core = amsn_core

    def presenceValues(self):
        return self.amsn_core.p2s