# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog

from PyQt4.QtGui    import  *
from PyQt4.QtCore   import  *


class KFESigningInPage (QWidget):
    def __init__(self, parent = None):
        KFELog().l("KFESigningInPage.__init__()")
        QWidget.__init__(self, parent)
        
        hpLay = QHBoxLayout()
        vLay = QVBoxLayout()
        hLay = QHBoxLayout()
        
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimumWidth(220)
        self.progressMessage = QLabel("")
        self.progressMessage.setAlignment(Qt.AlignCenter)
        throbber = QLabel()
        movie = QMovie("amsn2/ui/front_ends/kde4/throbber.gif")
        print "movie valid %s" % movie.isValid()
        throbber.setMovie(movie)
        movie.start()
        
        hpLay.addStretch()
        hpLay.addWidget(self.progressBar)
        hpLay.addStretch()
        
        vLay.addStretch()
        vLay.addWidget(throbber)
        vLay.addSpacing(40)
        vLay.addLayout(hpLay)
        vLay.addSpacing(30)
        vLay.addWidget(self.progressMessage)
        vLay.addStretch()
        
        hLay.addStretch()
        hLay.addLayout(vLay)
        hLay.addStretch()
        
        QWidget.setLayout(self,hLay)
        

    def onConnecting(self, progress, message):
        KFELog().l("KFESigningInPage.onConnecting()")
        self.progressBar.setValue(progress * 100)
        self.progressMessage.setText(message)
