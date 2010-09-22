# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.frontend.widgets  import  KFEPresenceCombo,   \
                                                        KFENickEdit
from amsn2.ui.front_ends.kde4.adaptationLayer   import  KFEThemeManager

from PyQt4.QtGui    import *
from PyQt4.QtCore   import *

class KFEContactListPage (QWidget):
    def __init__(self, contactListWidget, parent=None):
        print "\t\t\t\tKFEContactListPage.__init__()"
        QWidget.__init__(self, parent)

        lay = QVBoxLayout()
        myInfoLay = QHBoxLayout()
        myInfoLayLeft = QVBoxLayout()

        self.nick = KFENickEdit()
        self.psm = KFENickEdit(allowEmpty = True, emptyMessage=QString("<u>Click here to set a personal message...</u>"))
        self.currentMedia = QLabel()
        self.presenceCombo = KFEPresenceCombo()

        myInfoLayLeft.addWidget(self.nick)
        myInfoLayLeft.addWidget(self.psm)
        myInfoLayLeft.addWidget(self.currentMedia)
        myInfoLayLeft.addWidget(self.presenceCombo)

        dp = QLabel()
        path = KFEThemeManager().pathOf("dp_amsn")
        dp.setPixmap(QPixmap(path))
        myInfoLay.addWidget(dp)
        myInfoLay.addLayout(myInfoLayLeft)

        lay.addLayout(myInfoLay)
        lay.addWidget(contactListWidget)

        QWidget.setLayout(self, lay)

    def onMyInfoUpdated(self, view):
        print "PartiallyImplementedError:\tKFEContactListPage.onMyInfoUpdated()"
        self.nick.setText(view.nick.to_HTML_string())
        if not QString(str(view.psm)).isEmpty(): #Think carefully: i think we can remove this if (look at KPresenceComboBox.setText()'s implementation)
            self.psm.setText(view.psm.to_HTML_string())
        print "\t\t\t\t\tN. of personal Images:" + str(len(view.dp.imgs))
        if len(view.dp.imgs) > 0:
            print "WE HAVE A DP FROM THE CORE! UPDATE THE FRONT END CODE!!"
        self.currentMedia.setText(view.current_media.to_HTML_string())
        #TODO: view.presence holds a string.... shouldn0t it hold a papyon.Presence?
        #self.presence_combo.setPresence(view.presence) <-- this could be used when it will hold a papyon.Presence
        self.presenceCombo.setCurrentIndex(self.presenceCombo.findText(view.presence.capitalize())) 
