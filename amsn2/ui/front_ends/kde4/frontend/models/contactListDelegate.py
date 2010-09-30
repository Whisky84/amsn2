# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog

from contactListModel   import KFERole

from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager

from PyQt4.QtGui    import  *

from PyQt4.QtCore   import  *

                            
class ContactStyledDelegate (QStyledItemDelegate):
    # Consider implementing a caching mechanism, if it's worth
    # dPS = defaultPictureSize
    dPS = 55.0
    # dPM = defaultPicture(Inner)Margin
    dPM = 5
    textOptions = QTextOption()
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)
        self.xyOff = QPointF(self.dPM, self.dPM)
        self.bottomRightDeltaPoint = QPointF(self.dPS, self.dPS) - self.xyOff
        self.textOptions.setWrapMode(QTextOption.NoWrap)
        
    def paint(self, painter, option, index):
        #print "\t\t\t\tContactStyledDelegate.paint()" 
        if not index.parent().isValid():
            #KFELog().d("I'm painting a group Item", "ContactStyledDelegate.paint()")
            QStyledItemDelegate.paint(self, painter, option, index)
        else:
            model = index.model()
            painter.save()
            topLeftPoint = QPointF(option.rect.topLeft())
            
            # -> Configure the painter
            painter.setClipRect(option.rect)
            painter.setClipping(True)
            # -> Draw the skeleton of a ItemView widget: highlighting, selection...
            QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)
    
            # -> Start drawing the decoration:
            # create the picture
            picture = QPixmap(model.data(index, KFERole.DecorationRole))
            # calculate the target position
            source = QRectF( QPointF(0.0,0.0), QSizeF(picture.size()) )
            target = QRectF( topLeftPoint + self.xyOff,
                             topLeftPoint + self.bottomRightDeltaPoint)
            # draw
            painter.drawPixmap(target, picture, source)
    
            # -> start drawing the emblem
            picturePath  = KFEThemeManager().pathOf("emblem_%s" % 
                            str(model.data(index, KFERole.StatusRole).toString()))
            picture = QPixmap(picturePath)
            source = QRectF( QPointF(0.0,0.0), QSizeF(picture.size()) )
            painter.drawPixmap(target, picture, source)
        
            # -> Start drawing the txtWidget:
            # create the txtWidget 
            txtWidget = QTextDocument()
            txt = model.data(index, KFERole.DisplayRole).toString()
            txt = txt.replace("<i>", "<br>,<i>")
            txt = txt.replace("<img src", '<img width="17" height="17" src')
            txtWidget.setHtml(index.model().data(index, KFERole.DisplayRole).toString().replace("<i>","<br><i>"))
            # calculate the vertical offset, to center the txtWidget vertically
            vOff = abs(option.rect.height() - txtWidget.size().height())/2
            # move the pointer to the txtWidget zone:
            painter.translate(topLeftPoint + QPointF(self.dPS, vOff))
            # draw
            txtWidget.drawContents(painter, QRectF(QRect( QPoint(0,0), option.rect.size())))
            # -> It's done!
            painter.restore()
        

    def sizeHint(self, option, index):
        if not index.parent().isValid():
            #KFELog().d("I'm sizing a group Item", "ContactStyledDelegate.sizeHint()")
            return QStyledItemDelegate.sizeHint(self, option, index)
        else:
            txtWidget = QTextDocument()
            txtWidget.setHtml(index.model().data(index, KFERole.DisplayRole).toString().replace("<i>","<br><i>"))
            txtSize = txtWidget.size().toSize()
            txtWidth  = txtSize.width()
            txtHeight = txtSize.height()
            return QSize( txtWidth,
                          max(txtHeight, self.dPS)  )
        


        

class ContactDelegate (QItemDelegate):
    def __init__(self, parent):
        """To allineate correctly the painted stuff parent MUST
        be the View"""
        QItemDelegate.__init__(self, parent)
        self.parent = parent

    def paint(self, painter, option, index):

        if not index.isValid():
            return

        #painter must be saved before painting
        painter.save()
        viewPos = self.parent.pos()
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
        self.drawDecoration(painter, option, decorationRect, index.model().data(index, Qt.DecorationRole).scaled(50,50))

        datum = index.model().data(index, Qt.DisplayRole).toString()

        label = QLabel(datum)
        label.setBackgroundRole(QPalette.Base)
        labelOrigin = QPoint(option.rect.topLeft())
        labelOriginOffset = QPoint(viewPos)
        labelOrigin.setY( labelOrigin.y() + option.rect.height()/3) #this centers the label vertically...

        labelPixmap = QPixmap.grabWidget(label)
        labelPixmapRect = QRect(option.rect.x()+65, \
                                  option.rect.y()+(option.rect.height()-labelPixmap.size().height())/2, \
                                  option.rect.width(), \
                                  option.rect.height())
        self.drawDecoration(painter, option, labelPixmapRect, labelPixmap)

        QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)
        painter.restore()
        

    def sizeHint(self, option, index):
        size = QSize(200, 60)
        return size
