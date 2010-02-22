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
    
    
    
    
class TreeModel(QAbstractItemModel):
    
    def __init__(self, data, parent = None):
        QAbstractItemModel.__init__(self, parent)
        rootData = []
        rootData.append("Title")
        rootData.append("Summary")
        self.rootItem  = TreeItem(rootData)
        data = QString(data)
        #self.setupModelData(data.split(QString("\n")), self.rootItem)
        A = TreeItem(["A","a"],self.rootItem)
        B = TreeItem("B",self.rootItem)
        C = TreeItem("C",self.rootItem)
        self.rootItem.appendChild(A)
        self.rootItem.appendChild(B)
        self.rootItem.appendChild(C)
        print "A=", A
        print "B=", B
        print "C=", C
        D = TreeItem("D",A)
        A.appendChild(D)
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

        
    def setupModelData(self, lines, parent):
        parents = []
        indentations = []
        parents.append(parent)
        indentations.append(0)

        number = 0

        while number < lines.count():
            position = 0;
            while position < lines[number].length(): 
                if lines[number].mid(position, 1) != " ":
                    break
                position+=1
            

            lineData = lines[number].mid(position).trimmed();

            if not lineData.isEmpty():
                #// Read the column data from the rest of the line.
                columnStrings = lineData.split("\t", QString.SkipEmptyParts);
                columnData = []
                for column in range(0,column < columnStrings.count()):
                    columnData.append(columnStrings[column])

                if position > indentations.last():
                    #// The last child of the current parent is now the new parent
                    #// unless the current parent has no children.

                    if parents.last().childCount() > 0:
                        parents.append(parents.last().child(parents.last().childCount()-1))
                        indentations.append(position)
                
                else:
                    while position < indentations.last() and parents.count() > 0:
                        parents.pop_back()
                        indentations.pop_back()

                        #// Append a new item to the current parent's list of children.
                parents.last().appendChild(TreeItem(columnData, parents.last()))

            number+=1
            
if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    file_ = QFile(":/default.txt")
    file_.open(QIODevice.ReadOnly)
    model = TreeModel(file_.readAll())
    view = QTreeView()
    view.setModel(model)
    view.show()
    qapp.exec_()
            