# -*- coding: utf-8 -*-

from PyKDE4.kdeui   import  KLineEdit

from PyQt4.QtGui    import  QLabel,         \
                            QSizePolicy,    \
                            QStackedWidget, \
                            QWidget

from PyQt4.QtCore   import  QObject,    \
                            QString,    \
                            Qt,         \
                            SIGNAL

# imports for the Test class
from PyKDE4.kdeui   import  KMainWindow


class Test(KMainWindow):
    def __init__(self):
        KMainWindow.__init__(self)
        self.nickEdit = KNickEdit2(allowEmpty = True)
        self.nickEdit.setText("Nick")
        btn = KPushButton(":E")
        lab = QLabel(":O")
        
        lay = QHBoxLayout()
        lay.addWidget(self.nickEdit)
        #lay.addWidget(btn)
        #lay.addWidget(lab)
        
        QObject.connect(self.nickEdit, SIGNAL("nickChanged()"), self.cucu)
        w = QWidget()
        w.setLayout(lay)
        self.setCentralWidget(w)
        self.setGeometry(100,100,370,230)
        
        
    def cucu(self):
        print "New Text:", self.nickEdit.text()




class KFENickEdit(QStackedWidget):
    def __init__(self, allowEmpty = False, emptyMessage = QString("Click here to write"), parent = None):
        QStackedWidget.__init__(self, parent)
        
        self._allowEmpty = allowEmpty
        self._emptyMessage = QString("<u>") + emptyMessage + QString("</u>")
        self._isEmptyMessageDisplayed = False
        
        self.lineEdit = KLineEdit()
        
        self.label = QLabel_("If you see this, please invoke setText on KNickEdit.")
        self.setText(QString())
            
        self.addWidget(self.lineEdit)
        self.addWidget(self.label)
        self.setCurrentWidget(self.label)
        
        QObject.connect(self.label, SIGNAL("clicked()"), self.onLabelClicked)
        QObject.connect(self.lineEdit, SIGNAL("editingFinished()"), self.onLineEdited)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        
    def text(self):
        if self._isEmptyMessageDisplayed:
            return QString()
        return self.label.text()
        
        
    def setText(self, text):
        #NOTE: do we have to set also the KLineEdit's text? <-> method could be called while the KLEdit is active? 
        text = QString(text) 
        if not text.isEmpty():
            self._isEmptyMessageDisplayed = False
            self.label.setText(text)
        elif self._allowEmpty:
            self._isEmptyMessageDisplayed = True
            self.label.setText(self._emptyMessage)

    
    # -------------------- QT_SLOTS
    
    
    def onLabelClicked(self):
        if self._isEmptyMessageDisplayed:
            text = QString()
        else:
            text = self.label.text()
        self.lineEdit.setText(text)
        self.setCurrentWidget(self.lineEdit)
        self.lineEdit.setFocus(Qt.MouseFocusReason)
    
    
    def onLineEdited(self):
        text = self.lineEdit.text()
        self.setText(text)
        #if the text is empty, and it is not allowed to be so, the label remains unchanged
        self.setCurrentWidget(self.label)
        self.emit(SIGNAL("nickChanged(QString)"), text)




class QLabel_(QLabel):
    
    _le = QString("<u><em>")
    _ri = QString("</em></u>")
    
    def __init__(self, text=QString(), parent = None):
        QLabel.__init__(self)
        self._text = QString()
        self.setText(text)
        
    def setText(self, text): #you can pass either a pythonic string or a QString
        text = QString(text)
        self._text = QString(text) 
        QLabel.setText(self, text)
        
    def text(self): #returns a QString
        return self._text
        
    def mousePressEvent(self,ev):
        QLabel.mousePressEvent(self, ev)
        if ev.button() == Qt.LeftButton:
            self.emit(SIGNAL("clicked()"))    
    
    def enterEvent(self, ev): #received even if mouse tracking not explicitly enabled
        QLabel.setText(self, QLabel_._le + self._text + QLabel_._ri)
        
    def leaveEvent(self, ev): #received even if mouse tracking not explicitly enabled
        QLabel.setText(self, self._text)
        
######################################################################################

class KFENickEdit2(QWidget):
    def __init__(self, allowEmpty = False, parent = None):
        QWidget.__init__(self, parent)
        
        self.lineEdit = KLineEdit(self)
        self.label = QLabel_(parent = self)
        
        self.editButton = KPushButton("edit", self)
        self.okButton = KPushButton("ok", self)
        self.cancelButton = KPushButton("cancel",self)
        
        self.viewState = QState()
        self.viewState.assignProperty(self.editButton, "geometry", QRect(180, 5, 70, 30))
        self.viewState.assignProperty(self.okButton, "geometry", QRect(110, -35, 70, 30))
        self.viewState.assignProperty(self.cancelButton, "geometry", QRect(180, -35, 70, 30))
        self.viewState.assignProperty(self.label, "geometry", QRect(5, 5, 175, 30))
        self.viewState.assignProperty(self.lineEdit, "geometry", QRect(-110,5, 105, 30))
        
        self.editState = QState()
        self.editState.assignProperty(self.editButton, "geometry", QRect(180, 55, 70, 30))
        self.editState.assignProperty(self.okButton, "geometry", QRect(110, 5, 70, 30))
        self.editState.assignProperty(self.cancelButton, "geometry", QRect(180, 5, 70, 30))
        self.editState.assignProperty(self.label, "geometry", QRect(-200, 5, 175, 30))
        self.editState.assignProperty(self.lineEdit, "geometry", QRect(5,5, 105, 30))
        
        self.viewState.addTransition(self.editButton, SIGNAL("clicked()"), self.editState)
        self.editState.addTransition(self.okButton, SIGNAL("clicked()"), self.viewState)
        self.editState.addTransition(self.cancelButton, SIGNAL("clicked()"), self.viewState)
        
        self.machine = QStateMachine(self)
        self.machine.addState(self.viewState)
        self.machine.addState(self.editState)
        self.machine.setInitialState(self.viewState)

        
        
        #self.pa.setEasingCurve(QEasingCurve.InOutBack)
        self.pa2 = QPropertyAnimation(self.lineEdit, "geometry")
        self.machine.addDefaultAnimation(self.pa2);
        self.pa = QPropertyAnimation(self.editButton, "geometry")
        self.pa.setEasingCurve(QEasingCurve.OutBack)
        self.machine.addDefaultAnimation(self.pa)
        
        
        self.machine.start()
    
    def setText(self, text):
        pass
        
        
if __name__ == "__main__":
    about_data = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about_data)
    kapp = KApplication()
    win = Test()
    win.show()
    kapp.exec_()