# -*- coding: utf-8 -*-

import sys

from amsn2.core import aMSNUserInterfaceManager


#Loading of front end modules
def load():
    import kde4frontend
    return kde4frontend    


#kde4 front end registration:
print "Trying to register KDE4 front-end...\n"
try:
    import imp
    imp.find_module("PyQt4")
    imp.find_module("PyKDE4")
    
    print sys.modules[__name__]
    print __name__
    aMSNUserInterfaceManager.register_frontend("kde4", sys.modules[__name__])
except ImportError:
    print "Unable to register kde4 front-end"
