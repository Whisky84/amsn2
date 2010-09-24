# -*- coding: utf-8 -*-

from PyKDE4.kdeui import KTextEdit


from PyQt4.QtGui import QKeyEvent
from PyQt4.QtCore import *


class KFETextEditMod (KTextEdit):
    def __init__(self, parent = None):
        KTextEdit.__init__(self, parent)
        self.ReturnPressed = False
        

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            if keyEvent.modifiers() == Qt.ControlModifier:
                keyEvent.accept()
                fakeEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_Return, Qt.NoModifier)
                KTextEdit.keyPressEvent(self, fakeEvent)
            elif keyEvent.modifiers() == Qt.NoModifier:
                keyEvent.accept()
                self.ReturnPressed = True
            else:
                KTextEdit.keyPressEvent(self, keyEvent)
        else:
            KTextEdit.keyPressEvent(self, keyEvent)


    def keyReleaseEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            if keyEvent.modifiers() == Qt.ControlModifier:
                keyEvent.accept()
                fakeEvent = QKeyEvent(QEvent.KeyRelease, Qt.Key_Return, Qt.NoModifier)
                KTextEdit.keyReleaseEvent(self, fakeEvent)
            elif keyEvent.modifiers() == Qt.NoModifier:
                if not self.ReturnPressed:
                    KFELog().d("There's some problem!", "KTextEditMod.keyReleaseEvent()")
                keyEvent.accept()
                self.ReturnPressed = False
                self.emit(SIGNAL("returnPressed()"))
            else:
                KTextEdit.keyPressEvent(self, keyEvent)
        else:
            KTextEdit.keyPressEvent(self, keyEvent)

            

