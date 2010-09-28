# -*- coding: utf-8 -*-

from amsn2.core import aMSNCore
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
            self.widget = KFELogWidget()
            KFELog.__isInitialized = True

    def l(self, message, nextIndented = False, status = 0):
        if status not in [0, 1, 2]:
            self.d("Invalid status!", "KFELog.l()")
            status = 3
        formattedMessage = "<div style=\"text-indent:%dpx; color:%s; font-weight:bold; margin-bottom=0px\">%s</div>" \
                % (self.ind, self.color[status], message)
        self.widget.p(formattedMessage)
        if not nextIndented:
            self.ind = 0
        else:
            self.ind +=20
        


    def d(self, message, method=""):
        formattedMessage = "<div> <i>%s</i> %s</div>" % (method, message)
        self.widget.p(formattedMessage)
        
        

        
        
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
    
    
class KFELogWidget(QWidget):
    def __init__(self):
        mainWin = aMSNCore().get_main_window()
        QWidget.__init__(self,  mainWin)
        lay = QVBoxLayout()
        self.textEdit = KTextEdit()
        self.text = QString()
        self.textEdit.setReadOnly(True)
        btn = KPushButton("Flush")
        lay.addWidget(self.textEdit)
        lay.addWidget(btn)
        
        btn.clicked.connect(self.onFlushClicked)
        
        self.setLayout(lay)
        self.resize(QSize(800,600))
        self.show()
        
    def p(self, message):
        vertScrollBar = self.textEdit.verticalScrollBar()
        if vertScrollBar.value() == vertScrollBar.maximum():
            atBottom = True
        else:
            atBottom = False

        self.text.append(message)
        self.textEdit.setHtml(self.text)

        if atBottom:
            vertScrollBar.setValue(vertScrollBar.maximum())
            
    def onFlushClicked(self):
        self.text = QString()
        self.textEdit.setHtml(self.text)
        self.p("(***)")
        
        
    def flush(self):
        KFELog().onFlushClicked()
  
  
  
  
  
  
