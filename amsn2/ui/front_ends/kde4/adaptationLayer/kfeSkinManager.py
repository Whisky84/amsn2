#TODO: What will we have to do with this stuff? (In terms of AdaptationLayer of course)

from kfeLog import KFELog

from amsn2.ui import base

class KFESkinManager(base.skins.SkinManager):
    def __init__(self, core):
        KFELog().l("KFESkinManager.__init__()", False, 1)
        self._core = core
        self.skin = KFESkin(core, "skins")

    def skin_set(self, name):
        self.skin = KFESkin(self._core, os.path.join("skins", name))
        KFELog().l("KFESkinManager.skin_set()", False, 2)

    def get_skins(self, path):
        KFELog().l("KFESkinManager.get_skins()", False, 2)





class KFESkin(base.skins.Skin):
    def __init__(self, core, path):
        KFELog().l("KFESkin.__init__()", False, 2)
        self._path = path
    
    def key_get(self, key, default):
        KFELog().l("KFESkin.key_get()", False, 2)
    
    def key_set(self, key, value):
        KFELog().l("KFESkin.key_set()", False, 2)
    