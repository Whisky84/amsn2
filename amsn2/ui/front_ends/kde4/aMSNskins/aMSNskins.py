# -*- coding: utf-8 -*-

import os.path

from amsn2.ui import base

class Skin(base.Skin):
    def __init__(self, core, path):
        """
        @type core: aMSNCore
        @type path:
        """

        self._path = path
        print "NotImplementedError:\t\tSkin.__init__()"
        pass

    def key_get(self, key, default):
        print "NotImplementedError:\t\tSkin.key_get()"
        pass

    def key_set(self, key, value):
        print "NotImplementedError:\t\tSkin.key_set()"
        pass



class SkinManager(base.SkinManager):
    def __init__(self, core):
        """
        @type core: aMSNCore
        """
        self._core = core
        self.skin = Skin(core, "skins")

    def skin_set(self, name):
        self.skin = Skin(self._core, os.path.join("skins", name))
        print "NotImplementedError:\t\tSkinManager.skin_set()"
        pass

    def get_skins(self, path):
        print "NotImplementedError:\t\tSkinManager.get_skins()"
        pass
