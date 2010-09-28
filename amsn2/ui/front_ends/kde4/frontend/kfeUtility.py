# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog

from amsn2.ui.front_ends.kde4   import  adaptationLayer

from PyKDE4.kdeui               import *
from PyQt4.QtGui                import *
from PyQt4.QtCore               import *

class KFEContactInputWindow (adaptationLayer.KFEAbstractContactInputWindow, KDialog):
    onContactEmailInserted = pyqtSignal(basestring)
    def constructor(self, parent = 0):
        KFELog().l("KFEContactInputWindow.constructor()", False, 1)
        KDialog.__init__(self, parent)
        #self.contactTextEdit = KTextEdit()
        #lay = QVBoxLayout()
        #lay.addWidget( QLabel("New contact's email:") )
        #lay.addWidget(self.contactTextEdit)
        #mainWidget = QWidget()
        #mainWidget.setLayout(lay)
        #self.setMainWidget(mainWidget)
        mainWidget = QWidget(self)
        lay = QVBoxLayout()
        self.contactTextEdit = KLineEdit()
        lbl = QLabel("New contact's email:")
        
        
        lay.addWidget(lbl)
        lay.addWidget(self.contactTextEdit)
        mainWidget.setLayout(lay)
        self.setMainWidget(mainWidget)
        
        self.setCaption("aMSN")
        #self.setButtons(KDialog.Close | KDialog.Ok)
        self.okClicked.connect(self.onOkClicked)
        self.onContactEmailInserted.connect(self.onContactAddRequest)
        
        

    def setTitle(self, title):
        KFELog().l("KFEContactInputWindow.setTitle()", False, 2)

    def show(self):
        KFELog().l("KFEContactInputWindow.show()")
        self.setModal(True)
        KDialog.show(self)

    def onOkClicked(self):
        self.onContactEmailInserted.emit(str(self.contactTextEdit.text()))