# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog

from PyQt4.QtGui    import  QHBoxLayout,    \
                            QLabel,         \
                            QProgressBar,   \
                            QVBoxLayout,    \
                            QWidget


class KFESigningInPage (QWidget):
    def __init__(self, parent = None):
        KFELog().l("\t\t      KFESigningInPage.__init__()")
        QWidget.__init__(self, parent)
        
        vLay = QVBoxLayout()
        hLay = QHBoxLayout()
        
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressMessage = QLabel("")
        
        vLay.addStretch()
        vLay.addWidget(self.progressBar)
        vLay.addWidget(self.progressMessage)
        vLay.addStretch()
        
        hLay.addStretch()
        hLay.addLayout(vLay)
        hLay.addStretch()
        
        QWidget.setLayout(self,hLay)
        

    def onConnecting(self, progress, message):
        KFELog().l("\t\t      KFESigningInPage.onConnecting()")
        self.progressBar.setValue(progress * 100)
        self.progressMessage.setText(message)
