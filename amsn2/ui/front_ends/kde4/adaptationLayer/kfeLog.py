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
                      'w': None,
                      'ind': 0,
                      'color': ["green", "orange", "red", "purple"]}
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


    def __p(self, message):
        vertScrollBar = self.textEdit.verticalScrollBar()
        if vertScrollBar.value() == vertScrollBar.maximum():
            atBottom = True
        else:
            atBottom = False

        self.text.append(message)
        self.textEdit.setHtml(self.text)

        if atBottom:
            vertScrollBar.setValue(vertScrollBar.maximum())


    def l(self, message, nextIndented = False, status = 0):
        if status not in [0, 1, 2]:
            self.d("Invalid status!", "KFELog.l()")
            status = 3
        formattedMessage = "<div style=\"text-indent:%dpx; color:%s; font-weight:bold; margin-bottom=0px\">%s</div>" \
                % (self.ind, self.color[status], message)
        self.__p(formattedMessage)
        if not nextIndented:
            self.ind = 0
        else:
            self.ind +=20
        


    def d(self, message, method=""):
        formattedMessage = "<div> <i>%s</i> %s</div>" % (method, message)
        self.__p(formattedMessage)
        


if __name__ == "__main__":
    aboutData = KAboutData("a", "b", ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, aboutData)
    app = KApplication()
    KFELog().l("Ciao")
    KFELog().l("Ciao", True, 1)
    KFELog().l("Ciao", True, 2)
    KFELog().l("Ciao", False, 1)
    KFELog().l("Ciao")
    sys.exit(app.exec_())
  
  
  
  
  
  