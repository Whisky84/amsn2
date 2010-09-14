# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

import sys


class ContactListModel(QAbstractListModel):

    def __init__(self, parent = None):
        QAbstractTableModel.__init__(self, parent)
        self.contactList = []
        self.groupDict = {}



    def rowCount(self, parent):
        if parent.isValid():
            #print "\t\t\t\t\t rowCount = 0"
            return 0
        else:
            #print "\t\t\t\t\t rowCount = " + str(len(self.contactList))
            return len(self.contactList)
            

    #def columnCount(self, parent):
        #if parent.isValid():
            #return 0
        #else:
            #return 3


    def data(self, index, role):
        #print "\t\t\t\tContactListModel.data: (" + str(index.row()) + "," + str(index.column()) + "), Role:  " + str(role) 
        if role == Qt.DisplayRole:
            if index.column() != 0:
                return QVariant()
            else:
                #print u"\t\t\t\t\tdata(): ("+str(index.row())+","+str(index.column())+") -> " + self.contactList[index.row()].name.to_HTML_string()
                return QString(self.contactList[index.row()].name.to_HTML_string())
        elif role == Qt.DecorationRole:
            if index.column != 0:
                return QVariant()
            else:
                return QPixmap(self.contactList[index.row()].dp)

    # amsn2 interface

    def contactlist_updated(self, clView):
        print "NotImplementedError\t\t\tContactListModel.contactlist_updated()"
        

    def contact_updated(self, contact):
        """ Adds a contact. If it is already present (this is checked by UID)
        the contact is updated

        @type contact: ContactView
        @param contact:the contact information."""
        print "\t\t\t\tContactListModel.contact_updated()"
        #print "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(UID)"
        #print "\tDevo elaborare: " + str(contact.name.get_tag("nickname")) +  "\tUID:" + contact.uid
        #if contactList is empty add directly the contact and return:
        if len(self.contactList) == 0:
            self.emit( SIGNAL("rowsAboutToBeInserted(const QModelIndex&, int, int)"), QModelIndex(), 1, 1 )
            self.contactList.append(contact)
            #print "\tHo aggiunto (VUOTA): " + str(contact.name.get_tag("nickname")) + "\tUID:" + contact.uid
            self.emit( SIGNAL("rowsInserted(const QModelIndex&, int, int)"), QModelIndex(), 1, 1 )
            return
            
        # if it's not empty, searches the position of the contact:
        contactIndex = 0
        for i in range(len(self.contactList)):
            #print "\t\tnella lista ho i: " + str(i) + "nome: " + str(self.contactList[i].name.get_tag("nickname")) +  "\tUID:" + self.contactList[i].uid,
            if self.contactList[i].uid < contact.uid:
                #print " --> incremento"
                contactIndex = i+1
            #else:
            #    print " --> passo"
        #print "\tcontactIndex è " + str(contactIndex) + ", len: " + str(len(self.contactList)) + " (UID)"
        #if contactIndex < len(self.contactList):
        #    print "\tconfronto UID: ho " + str(contact.uid) + ", trovo " + str(self.contactList[contactIndex].uid)
        #else:
        #    print "\tconfronto UID: sto in coda alla lista"
        if contactIndex < len(self.contactList) and self.contactList[contactIndex].uid == contact.uid: #contact already present
            self.contactList[contactIndex] = contact
            #print "\tHo aggiornato : " + str(contact.name.get_tag("nickname")) +  "\tUID:" + contact.uid
            self.emit(SIGNAL("dataChanged(const QModelIndex&, const QModelIndex&)"), \
                        self.index(contactIndex, 0, QModelIndex()), \
                        self.index(contactIndex, 2, QModelIndex()) )
        else: #contact is not present
            self.emit( SIGNAL("rowsAboutToBeInserted(const QModelIndex&, int, int)"), QModelIndex(), contactIndex, contactIndex )
            self.contactList.insert(contactIndex, contact)
            #print "\tHo aggiunto: " + str(contact.name.get_tag("nickname")) + "\tUID:" + contact.uid
            self.emit( SIGNAL("rowsInserted(const QModelIndex&, int, int)"), QModelIndex(), len(self.contactList)-1, len(self.contactList)-1 )
        

    def group_updated(self, gView):
        print "\t\t\t\tContactListModel.group_updated()"
        self.groupDict[gView.uid] = (gView.name, gView.contact_ids)
        print "\t\t\t\t\tlen(self.groupDict) = " + str(len(self.groupDict))




class Contacts:
    """ This class represents the list of contacts to be displayed in the
    contact list widget. It is an ordered list. Temporarily ordered upon the
    UID, it will be ordered on the state first, on the name then."""

    def __init__(self):
        self.cList = []

    def update(self, contact):
        """ Adds a contact. If it is already present (this is checked by UID)
        the contact is updated
        
        @type contact: ContactView
        @param contact:the contact information."""

        # searches the position of the contact
        contactIndex = -1
        for i in range(len(self.cList)):
            if self.cList[i].uid <= contact.uid:
                contactIndex = i
                break
        # adds or updates the contact
        if contactIndex == -1: # the list is empty
            contactIndex = 0 #cause we return the index
            self.cList.append(contact)
        elif self.cList[contactIndex].uid == contact.uid:
            self.cList[contactIndex] = contact
        else: 
            self.cList.append(contactIndex, contact)
        return contactIndex

    def size(self):
        return len(self.cList)

    def contactAt(self, index):
        if index >= self.size():
            return None
        return self.cList[index]


class ContactDelegate (QItemDelegate):
    def __init__(self, parent):
        """To allineate correctly the painted stuff parent MUST
        be the View"""
        QItemDelegate.__init__(self, parent)
        self.parent = parent

    def paint(self, painter, option, index):
        print "\t\t\t\tContactDelegate.paint: index = (%d,%d); rect=(%d,%d,%d,%d)"  \
                % (index.row(), index.column(), \
                   option.rect.x(), option.rect.y(), option.rect.width(), option.rect.height())
        if not index.isValid():
            return

        #painter must be saved before painting
        painter.save()
        viewRect = self.parent.rect()
        #blocco copiato :)
        #painter.translate(0, 0)
        #options = QStyleOptionViewItemV4(option)
        #self.initStyleOption(options, index)
        painter.setRenderHint(QPainter.Antialiasing, True)
        QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)

        #painting has to be clipped in this delegate's rect
        painter.setClipRect(option.rect)
        painter.setClipping(True)

        #painting the display picture:
        option.decorationAlignment = Qt.AlignLeft
        option.decorationPosition = QStyleOptionViewItem.Left
        #self.drawDecoration(painter, option, option.rect, QPixmap(index.model().data(index, Qt.DecorationRole)))
        self.drawDecoration(painter, option, option.rect, QPixmap("/home/rayleigh/src/aMSN2/amsn2/themes/displaypic/default/male.png").scaled(50,50))
        #The label's rendering need the rect to be shrinked (why..?)
        #option.rect.setX(option.rect.x()+110)
        datum = index.model().data(index, Qt.DisplayRole)
        #print "\t\t\t\tContactDelegate.paint datum = %s" % (str(datum))
        datum = datum.replace("<i>","<br><i>")
        self.drawDisplay(painter, option, option.rect, datum)
        #label = QLabel(str(datum))
        #label.setBackgroundRole(QPalette.Base)
        #labelOrigin = QPoint(option.rect.topLeft())
        #labelOriginOffset = QPoint(viewRect.topLeft())
        #labelOrigin.setY( labelOrigin.y() + option.rect.height()/2) #this centers the label vertically...
        #label.render(painter, labelOrigin+labelOriginOffset)#, QRegion(), QWidget.RenderFlags(QWidget.IgnoreMask))

        #this should draw the focus, but it doesn't work...
        #self.drawFocus(painter, option, option.rect)
        painter.restore()
        

    def sizeHint(self, option, index):
        #options = QStyleOptionViewItemV4(option)
        #self.initStyleOption(options, index)
        #doc = QTextDocument()
        #doc.setHtml(options.text)
        #doc.setTextWidth(options.rect.width())

        #if group, leave as it, if contactitem, use dp height for calculating sizeHint.
        #model = index.model()
        #qv = QPixmap(model.data(model.index(index.row(), 0, index.parent()), Qt.DecorationRole))
        #if qv.isNull():
        size = QSize(500, 50)
        #else:
        #    size = QSize(doc.idealWidth(), qv.height() + 6)

        return size




class Test(KMainWindow):
    def __init__(self):
        KMainWindow.__init__(self)
        
        self.view = QListView(self)
        model = DummyModel(self.view)
        self.view.setModel(model)
        self.view.setItemDelegate(ContactDelegate(self.view))
        
        lay = QHBoxLayout()
        lay.addWidget(self.view)

        w = QWidget()
        w.setLayout(lay)
        self.setCentralWidget(w)
        self.setGeometry(100,100,370,230)
        
        

class DummyModel(QAbstractListModel):
    def __init__(self, parent = None):
        QAbstractListModel.__init__(self, parent)

    def rowCount(self, parent):
        if parent.isValid():
            return 0
        else:
            return 4

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        if index.column() != 0:
            return QVariant()
        elif index.row() == 0:
            return QString("Ciao! <i>coglione</i>")
        elif index.row() == 1:
            return QString("Blah <i>blah</i>")
        else:
            return QString("altro")

        

if __name__ == "__main__":
    about_data = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about_data)
    kapp = KApplication()
    win = Test()
    win.show()
    kapp.exec_()


        

