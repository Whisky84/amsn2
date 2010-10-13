# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.frontend.widgets.kfeChatTextEdit3 import KFEChatTextEdit3
from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager
from amsn2.core.smiley_manager  import aMSNSmileyManager
from amsn2.core import aMSNCore
from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class OptionsStub:
    def __init__(self):
        self.debug_protocol = False
        self.debug_amsn2 = False
        self.account = None
        self.front_end = 'curses'

if __name__ == "__main__":
    def testStuff():
        #KFEThemeManager.setManager(aMSNThemeManager(None))
        core = aMSNCore(OptionsStub())
        print "Theme Manager: ",
        print core._theme_manager
        KFEThemeManager.setManager(core._theme_manager)
        pass
    testStuff()
    about = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about)
    kapp = KApplication()
    W = KMainWindow()
    w = QWidget()
    e = KFEChatTextEdit3()
    e.setSmileyDict(aMSNSmileyManager(None).default_smileys_shortcuts)
    l = QVBoxLayout()
    l.addWidget(e)
    #l.addWidget(e.child)
    #l.setStackingMode(QStackedLayout.StackAll)
    w.setLayout(l)
    W.setCentralWidget(w)
    W.show()
    kapp.exec_()

