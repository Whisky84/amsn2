# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.frontend import KFEChatWidget, KFEChatWindow
from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager
from amsn2.core.theme_manager import aMSNThemeManager

from PyKDE4.kdeui   import *
from PyKDE4.kdecore import *

import sys

if __name__ == "__main__":
    def testStuff():
        KFEThemeManager.setManager(aMSNThemeManager(None))
    testStuff()
    about = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about)
    kapp = KApplication()
    w = KFEChatWindow(None)
    w.add_chat_widget(KFEChatWidget(None,w,"3"))
    w.show()
    kapp.exec_()

    
