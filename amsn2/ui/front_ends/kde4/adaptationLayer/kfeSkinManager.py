#TODO: What will we have to do with this stuff? (In terms of AdaptationLayer of course)

from amsn2.ui import base

class KFESkinManager(base.skins.SkinManager):
    def __init__(self, core):
        print "NotImplementedError:\t\tKFESkinManager.__init__()"
        self._core = core
        self.skin = KFESkin(core, "skins")

    def skin_set(self, name):
        self.skin = KFESkin(self._core, os.path.join("skins", name))
        print "NotImplementedError:\t\tKFESkinManager.skin_set()"

    def get_skins(self, path):
        print "NotImplementedError:\t\tKFESkinManager.get_skins()"





class KFESkin(base.skins.Skin):
    def __init__(self, core, path):
        print "NotImplementedError:\t\tKFESkin.__init__()"
        self._path = path
    
    def key_get(self, key, default):
        print "NotImplementedError:\t\tKFESkin.key_get()"
    
    def key_set(self, key, value):
        print "NotImplementedError:\t\tKFESkin.key_set()"
    