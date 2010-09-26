# -*- coding: utf-8 -*-


from amsn2.ui.front_ends.kde4.frontend.widgets  import  KFEPresenceCombo,   \
                                                        KFENickEdit
from amsn2.ui.front_ends.kde4.adaptationLayer   import  KFEThemeManager, KFELog

from PyQt4.QtGui    import *
from PyQt4.QtCore   import *

class KFEContactListPage (QWidget):
    def __init__(self, contactListWidget,contactListWindow, parent=None):
        KFELog().l("KFEContactListPage.__init__()")
        QWidget.__init__(self, parent)

        lay = QVBoxLayout()
        myInfoLay = QHBoxLayout()
        myInfoLayLeft = QVBoxLayout()

        self.nick = KFENickEdit()
        QObject.connect(self.nick, SIGNAL("nickChanged(QString)"), contactListWindow.onNewNickSet)
        self.psm = KFENickEdit(allowEmpty = True, emptyMessage=QString("<u>Click here to set a personal message...</u>"))
        QObject.connect(self.psm, SIGNAL("nickChanged(QString)"), contactListWindow.onNewPsmSet)
        self.currentMedia = QLabel()
        self.presenceCombo = KFEPresenceCombo()
        self.presenceCombo.presenceChanged.connect(contactListWindow.onNewPresenceSet)
        #QObject.connect(self.presenceCombo, SIGNAL("presenceChanged(papyon.Presence)"), contactListWindow.onNewPresenceSet)

        myInfoLayLeft.addWidget(self.nick)
        myInfoLayLeft.addWidget(self.psm)
        myInfoLayLeft.addWidget(self.currentMedia)
        myInfoLayLeft.addWidget(self.presenceCombo)
        
        # TODO: remove the personal info setting from here
        self.displayPic = QLabel()
        self.displayPic.setFrameStyle(QFrame.Box)
        self.displayPic.setFrameShadow(QFrame.Sunken)
        path = KFEThemeManager().pathOf("dp_amsn")
        self.displayPic.setPixmap(QPixmap(path))
        self.displayPic.installEventFilter( DisplayPicEventFilter(self.displayPic) )
        QObject.connect(self.displayPic, SIGNAL("clicked()"), contactListWindow.onDisplayPicChooseRequest)
        
        myInfoLay.addWidget(self.displayPic)
        myInfoLay.addLayout(myInfoLayLeft)

        lay.addLayout(myInfoLay)
        lay.addWidget(contactListWidget)

        QWidget.setLayout(self, lay)
        

    def onMyInfoUpdated(self, view):
        KFELog().l("KFEContactListPage.onMyInfoUpdated()", 1)
        self.nick.setText(view.nick.to_HTML_string())
        if not QString(str(view.psm)).isEmpty(): #Think carefully: i think we can remove this if (look at KPresenceComboBox.setText()'s implementation)
            self.psm.setText(view.psm.to_HTML_string())
        KFELog().d("N. of personal Images:" + str(len(view.dp.imgs)))
        if len(view.dp.imgs) > 0:
            KFELog().d("We have display pics, setting the first as the image shown")
            KFELog().d(view.dp.imgs[0])
            _, path = view.dp.imgs[0]
            self.displayPic.setPixmap(QPixmap(path, "PNG"))
        self.currentMedia.setText(view.current_media.to_HTML_string())
        #TODO: view.presence holds a string.... shouldn0t it hold a papyon.Presence?
        #self.presence_combo.setPresence(view.presence) <-- this could be used when it will hold a papyon.Presence
        self.presenceCombo.setCurrentIndex(self.presenceCombo.findText(view.presence.capitalize()))





class DisplayPicEventFilter (QObject):
    def eventFilter(self, label, event):
        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            label.emit(SIGNAL("clicked()"))
            return True
        else:
            return False
