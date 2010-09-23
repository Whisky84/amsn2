# -*- coding: utf-8 -*-

from PyKDE4.kdeui import *
from PyQt4.QtGui  import *

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
        self.text 
        self.textEdit.setReadOnly(True)
        lay.addWidget(self.textEdit)

        self.w = QWidget()
        self.w.setLayout(lay)
        self.w.size(QSize(800,600)
        self.w.show()


    def l(self, message):
        vertScrollBar = self.textEdit.verticalScrollBar()
        if vertScrollBar.value() == vertScrollBar.maximum():
            atBottom = True
        else:
            atBottom = False
        
        text = self.textEdit.toPlainText()
        text.append(message)
        self.textEdit.setPlainText(text)
        
        if atBottom:
            vertScrollBar.setValue(vertScrollBar.maximum())
            