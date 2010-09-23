#TODO: What will we have to do with this stuff? (In terms of AdaptationLayer of course)

from kfeLog import KFELog

from amsn2.ui import base

class KFESkinManager(base.skins.SkinManager):
    def __init__(self, core):
        KFELog().l("NotImplementedError:\tKFESkinManager.__init__()")
        self._core = core
        self.skin = KFESkin(core, "skins")

    def skin_set(self, name):
        self.skin = KFESkin(self._core, os.path.join("skins", name))
        KFELog().l("NotImplementedError:\tKFESkinManager.skin_set()")

    def get_skins(self, path):
        KFELog().l("NotImplementedError:\tKFESkinManager.get_skins()")





class KFESkin(base.skins.Skin):
    def __init__(self, core, path):
        KFELog().l("NotImplementedError:\tKFESkin.__init__()")
        self._path = path
    
    def key_get(self, key, default):
        KFELog().l("NotImplementedError:\tKFESkin.key_get()")
    
    def key_set(self, key, value):
        KFELog().l("NotImplementedError:\tKFESkin.key_set()")
    