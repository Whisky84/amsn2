# -*- coding: utf-8 -*-

from PyQt4.QtGui import *


class KSigninInPage(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        
        lay = QVBoxLayout()
        h_lay = QHBoxLayout() 
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_message = QLabel("")
        
        lay.addStretch()
        lay.addWidget(self.progress_bar)
        lay.addWidget(self.progress_message)
        lay.addStretch()
        
        h_lay.addStretch()
        h_lay.addLayout(lay)
        h_lay.addStretch()
        
        QWidget.setLayout(self,h_lay)
        
        
    # -------------------- QT_OVERLOAD
    
    
    def show(self):
        self.parent.setCurrentWidget(self)
        QWidget.show(self)
        
    
    # -------------------- OTHER_METHODS
    
    
    def on_connecting(self, progress, message):
        self.progress_bar.setValue(progress * 100)
        self.progress_message.setText(message)
