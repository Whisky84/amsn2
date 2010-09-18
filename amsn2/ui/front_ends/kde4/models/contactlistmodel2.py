# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

import sys


class ContactListModel(QAbstractListModel):

    def __init__(self, parent = None):
        QAbstractTableModel.__init__(self, parent)
        self._parent = parent
        self.contactList = []
        self.groupDict = {}


    def rowCount(self, parent):
        if parent.isValid():
            #print "\t\t\t\t\t rowCount = 0"
            return 0
        else:
            #print "\t\t\t\t\t rowCount = " + str(len(self.contactList))
            return len(self.contactList)
            

    def columnCount(self, parent):
        if parent.isValid():
            return 0
        else:
            return 3


    def data(self, index, role):
        #print "\t\t\t\tContactListModel.data: (" + str(index.row()) + "," + str(index.column()) + "), Role:  " + str(role)
        if (not index.isValid()) or (index.column() != 0) :
            return QVariant()
        else:

            if role == Qt.DisplayRole:
                #print u"\t\t\t\t\tdata(): ("+str(index.row())+","+str(index.column())+") -> " + self.contactList[index.row()].name.to_HTML_string()
                return QVariant(QString(self.contactList[index.row()].name.to_HTML_string()).replace("<i>","<br><i>"))

            elif role == Qt.DecorationRole:
                _,dpPath = self.contactList[index.row()].dp.imgs[0]
                if dpPath == "dp_nopic":
                    _,dpPath = self._parent._core._theme_manager.get_value("dp_nopic")
                return QPixmap(dpPath)

            else:
                return QVariant()

                
    # amsn2 interface

    def contactlist_updated(self, clView):
        print "NotImplementedError\t\tContactListModel.contactlist_updated()"
        

    def contact_updated(self, contact):
        """ Adds a contact. If it is already present (this is checked by UID)
        the contact is updated

        @type contact: ContactView
        @param contact:the contact information."""
        #print "\t\t\t\tContactListModel.contact_updated()"
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
        #print "\t\t\t\tContactListModel.group_updated()"
        self.groupDict[gView.uid] = (gView.name, gView.contact_ids)
        #print "\t\t\t\t\tlen(self.groupDict) = " + str(len(self.groupDict))

    def getIndexByUid(self, uid):
        for i in range(len(self.contactList)):
            if self.contactList[i].uid == uid:
                return i
        return None




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
        #print "\t\t\t\tContactDelegate.paint: index = (%d,%d); rect=(%d,%d,%d,%d)"  \
                #% (index.row(), index.column(), \
                #   option.rect.x(), option.rect.y(), option.rect.width(), option.rect.height())
        if not index.isValid():
            return

        #painter must be saved before painting
        painter.save()
        viewPos = self.parent.pos()
        #print "\t\t\t\t\tparent: pos=(%d,%d)" \
                #% (viewPos.x(), viewPos.y()),
        #print "; geometry=(%d,%d)" % (self.parent.geometry().x(), self.parent.geometry().y()),
        #print "(x,y) = (%d,%d)" % (self.parent.x(), self.parent.y())
        #print "\t\t\t\t\tpainter: viewPort = (%d,%d)" % (painter.viewport().x(), painter.viewport().y()),
        #print "; window=(%d,%d)" % (painter.window().x(), painter.window().y())
        #blocco copiato :)
        #painter.translate(0, 0)
        #options = QStyleOptionViewItemV4(option)
        #self.initStyleOption(options, index)
        painter.setRenderHint(QPainter.Antialiasing, True)


        #painting has to be clipped in this delegate's rect
        painter.setClipRect(option.rect)
        painter.setClipping(True)

        #painting the display picture:
        option.decorationAlignment = Qt.AlignLeft
        option.decorationPosition = QStyleOptionViewItem.Left
        option.displayAlignment = Qt.AlignLeft

        decorationRect = QRect( option.rect.x()+5, \
                                option.rect.y() + 5, \
                                option.rect.width(), \
                                option.rect.height() ) 
        #self.drawDecoration(painter, option, option.rect, QPixmap(index.model().data(index, Qt.DecorationRole)))
        self.drawDecoration(painter, option, decorationRect, index.model().data(index, Qt.DecorationRole).scaled(50,50))
        #The label's rendering need the rect to be shrinked (why..?)
        #option.rect.setX(option.rect.x()+65)
        datum = index.model().data(index, Qt.DisplayRole).toString()
        #print "\t\t\t\tContactDelegate.paint datum = %s" % (str(datum))
        #self.drawDisplay(painter, option, option.rect, datum)
        label = QLabel(datum)
        label.setBackgroundRole(QPalette.Base)
        labelOrigin = QPoint(option.rect.topLeft())
        labelOriginOffset = QPoint(viewPos)
        labelOrigin.setY( labelOrigin.y() + option.rect.height()/3) #this centers the label vertically...
        #label.render(painter, labelOrigin+labelOriginOffset)#, QRegion(), QWidget.RenderFlags(QWidget.IgnoreMask))
        labelPixmap = QPixmap.grabWidget(label)
        labelPixmapRect = QRect(option.rect.x()+65, \
                                  option.rect.y()+(option.rect.height()-labelPixmap.size().height())/2, \
                                  option.rect.width(), \
                                  option.rect.height())
        self.drawDecoration(painter, option, labelPixmapRect, labelPixmap)
        
        QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)
        
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
        size = QSize(200, 60)
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
        
        
        lay = QVBoxLayout()
        lay.addWidget(QLabel("Ciao"))
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
        if (not index.isValid()) or (index.column() != 0):
            return QVariant()
        else:

            if role == Qt.DisplayRole:
                #print u"\t\t\t\t\tdata(): ("+str(index.row())+","+str(index.column())+") -> " + self.contactList[index.row()].name.to_HTML_string()
                return QVariant(QString("Sono un contatto<br><i>di indici (%d,%d)</i>"%(index.row(),index.column())))

            elif role == Qt.DecorationRole:
                dpPath = "/home/fastfading/.amsn2/kde4fe_at_hotmail.com/displaypics/whisky.gabriele_at_gmail.com/4c61450adf0df29977729a033c036a3c9b3b5948.img"
                return QPixmap(dpPath)

            else:
                return QVariant()


    
if __name__ == "__main__":
    about_data = KAboutData("a","b",ki18n("c"), "d")
    KCmdLineArgs.init(sys.argv, about_data)
    kapp = KApplication()
    win = Test()
    win.show()
    kapp.exec_()


        

