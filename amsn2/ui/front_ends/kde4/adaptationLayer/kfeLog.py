# -*- coding: utf-8 -*-

from PyKDE4.kdeui import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *

# imports for the test main:
from PyKDE4.kdecore import *
import sys

class KFELog (object):
    __shared_state = {'text': "",
                      'textEdit': None,
                      'w': None}
    __isInitialized = False
    
    def __init__(self):
        self.__dict__ = KFELog.__shared_state
        if not KFELog.__isInitialized:
            self.initialize()
            KFELog.__isInitialized = True

    def initialize(self):        
        lay = QHBoxLayout()
        self.textEdit = KTextEdit()
        self.text = QString()
        self.textEdit.setReadOnly(True)
        lay.addWidget(self.textEdit)

        self.w = QWidget()
        self.w.setLayout(lay)
        self.w.resize(QSize(800,600))
        self.w.show()


    def l(self, message):
        vertScrollBar = self.textEdit.verticalScrollBar()
        if vertScrollBar.value() == vertScrollBar.maximum():
            atBottom = True
        else:
            atBottom = False
        
        
        self.text.append(message)
        self.textEdit.setPlainText(self.text)
        
        if atBottom:
            vertScrollBar.setValue(vertScrollBar.maximum())


if __name__ == "__main__" :
    aboutData = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, aboutData)
    app = KApplication()
    KFELog().l("Ciao Ciao\n")
    KFELog().l("\tBu!\n:)")
    sys.exit(app.exec_())
  
  
  
  
  
  