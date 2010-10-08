# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.frontend.widgets.kfeChatTextEdit import KFEChatTextEdit
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
        self.front_end = 'gtk'

if __name__ == "__main__":
    def testStuff():
        #KFEThemeManager.setManager(aMSNThemeManager(None))
        core = aMSNCore(OptionsStub())
        pass
    testStuff()
    about = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about)
    kapp = KApplication()
    w = QWidget()
    e = KFEChatTextEdit()
    l = QVBoxLayout()
    l.addWidget(e)
    l.addWidget(e.child)
    #l.setStackingMode(QStackedLayout.StackAll)
    w.setLayout(l)
    w.show()
    kapp.exec_()

