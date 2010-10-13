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

class Test (KMainWindow):
    def __init__(self, parent=None):
        KMainWindow.__init__(self, parent)

        self.te1 = KFEChatTextEdit3()
        self.te1.setSmileyDict(aMSNSmileyManager(None).default_smileys_shortcuts)
        self.te2 = KTextEdit()
        self.te2.setReadOnly(True)
        self.te3 = KTextEdit()
        self.te3.setReadOnly(True)
        self.lab = QLabel()
        self.font = KPushButton("font")
        self.color = KPushButton("color")
        lay = QVBoxLayout()
        lay.addWidget(self.te1)
        lay.addWidget(self.te2)
        lay.addWidget(self.te3)
        lay.addWidget(self.lab)
        lay.addWidget(self.font)
        lay.addWidget(self.color)

        centralWidget = QWidget()
        centralWidget.setLayout(lay)
        self.setCentralWidget(centralWidget)

        self.te1.textChanged.connect(self.onTextChanged)
        self.te1.returnPressed.connect(self.onReturnPressed)
        self.font.clicked.connect(self.te1.showFontStyleSelector)
        self.color.clicked.connect(self.te1.showFontColorSelector)


    def onTextChanged(self):
        html = self.te1.toHtml()
        plain = self.te1.toPlainText()
        self.te2.setPlainText("["+html+"]")
        self.te3.setPlainText("["+plain+"]")

    def onReturnPressed(self):
        self.lab.setText(self.te1.toPlainText())



if __name__ == "__main__":
    def testStuff():
        class OptionsStub:
            def __init__(self):
                self.debug_protocol = False
                self.debug_amsn2 = False
                self.account = None
                self.front_end = 'curses'
        core = aMSNCore(OptionsStub())
        print "Theme Manager: ",
        print core._theme_manager
        KFEThemeManager.setManager(core._theme_manager)

    testStuff()
    about = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about)
    kapp = KApplication()
    mW = Test()
    mW.show()
    kapp.exec_()


