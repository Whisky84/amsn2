# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4 import adaptationLayer

from amsn2.core import aMSNUserInterfaceManager

import sys


#Loading of front end modules
def load():
    import kde4frontend
    return kde4frontend    


#kde4 front end registration:
try:
    import imp
    imp.find_module("PyQt4")
    imp.find_module("PyKDE4")
    aMSNUserInterfaceManager.register_frontend("kde4", sys.modules[__name__])
except ImportError:
    print "Unable to register kde4 front-end"
