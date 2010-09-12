# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


class TreeItem(object):
    def __init__(self, data, parent = None):
        self.itemData = []
        for i in data:
            self.itemData.append(i)
        print "itemData è:", self.itemData
        self.parentItem = parent
        self.childItems = []
        
    def appendChild(self, child):
        self.childItems.append(child)
        
    
    def child(self, row):
        return self.childItems[row]
 
 
    def childCount(self):
        return len(self.childItems)
    
    def columnCount(self):
        return len(self.itemData)
    
    
    def data(self, column):
        if column < self.columnCount():
            return self.itemData[column]
        return QVariant()
        
    
    def row(self):
        if (self.parentItem):
            return self.parentItem.childItems.index(self)
    
    
    def parent(self):
        return self.parentItem
        
        
        
        
    
class ContactListModel(QAbstractItemModel):
    
    def __init__(self, parent = None):
        QAbstractItemModel.__init__(self, parent)
        rootData = []
        rootData.append("Title")
        rootData.append("Summary")
        self.rootItem  = TreeItem(rootData)
        self.n = 0
        
    
    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
            
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
            
        childItem = parentItem.child(row)
        
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()
            
    
    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        
        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self.rootItem:
            return QModelIndex()
            
        return self.createIndex(parentItem.row(), 0, parentItem)
        
    
    def rowCount(self, parent):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
        
        return parentItem.childCount()
        
        
    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()
            
    
    def data(self, index, role):
        self.n+=1
        print self.n,":", role
        if not index.isValid():
            return QVariant()
            
        if role != Qt.DisplayRole:
            return QVariant()
            
        item = index.internalPointer()
        
        return item.data(index.column())
        
        
    def flags(self, index):
        if not index.isValid():
            return 0;

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


    def headerData(self, section, orientation,role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)
        return QVariant()

        
    # amsn2 interface
    
    def contactlist_updated(self, clView):
        pass
        
        
        
            
if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    file_ = QFile(":/default.txt")
    file_.open(QIODevice.ReadOnly)
    model = TreeModel(file_.readAll())
    view = QTreeView()
    view.setModel(model)
    view.show()
    qapp.exec_()
            