# -*- coding: utf-8 -*-

from amsn2.ui.front_ends.kde4.adaptationLayer import KFELog

from contactListModel   import KFERole

from amsn2.ui.front_ends.kde4.adaptationLayer import KFEThemeManager

from PyQt4.QtGui    import  *

from PyQt4.QtCore   import  *

                            
class ContactStyledDelegate (QStyledItemDelegate):
    # Consider implementing a caching mechanism, if it's worth
    # dPS = defaultPictureSize
    dPS = 50.0
    # dPMmin = defaultPicture(Outer)Margin
    dPMmin = 3.0
    textOptions = QTextOption()
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)
        self.textOptions.setWrapMode(QTextOption.NoWrap)
        self.picSize = QSizeF(self.dPS, self.dPS)
        
    def paint(self, painter, option, index):
        model = index.model()
        painter.save()
        # -> Configure the painter
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)  # especially useful for scaled smileys.
        painter.setClipRect(option.rect)
        painter.setClipping(True)
        # -> Draw the skeleton of a ItemView widget: highlighting, selection...
        QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)
        txtWidget = QTextDocument()
        txt = model.data(index, KFERole.DisplayRole).toString()
        
        if not index.parent().isValid():
            # -> Start drawing the txtWidget:
            txt = "<b>"+txt+"</b>"
            painter.translate( QPointF(option.rect.topLeft()) )
            # create the txtWidget
            txtWidget.setHtml(txt)
            # draw the txtWidget
            txtWidget.drawContents(painter)
            
        else:
            topLeftPoint = QPointF(option.rect.topLeft())
            # -> Start drawing the decoration:
            # calc
            yPicMargin = abs((option.rect.height() - self.dPS)) / 2
            xPicMargin = self.dPMmin
            xyPicMargin = QPointF(xPicMargin, yPicMargin)
            # create the picture
            picture = QPixmap(model.data(index, KFERole.DecorationRole))
            # calculate the target position
            source = QRectF( QPointF(0.0,0.0), QSizeF(picture.size()) )
            target = QRectF( topLeftPoint + xyPicMargin, self.picSize )
            # draw the picture
            painter.drawPixmap(target, picture, source)
    
            # -> start drawing the emblem
            picturePath  = KFEThemeManager().pathOf("emblem_%s" % 
                            str(model.data(index, KFERole.StatusRole).toString()))
            picture = QPixmap(picturePath)
            source = QRectF( QPointF(0.0,0.0), QSizeF(picture.size()) )
            painter.drawPixmap(target, picture, source)
        
            # -> Start setting up the txtWidget:
            txt = self.__formatContactDisplayRole(txt)
            # set the text into txtWidget
            txtWidget.setHtml(txt)
            # calculate the vertical offset, to center the txtWidget vertically
            yTextOffset = abs(option.rect.height() - txtWidget.size().height()) / 2
            xTextOffset = 2 * xPicMargin + self.dPS
            xyTextOffset = QPointF(xTextOffset, yTextOffset)
            # move the pointer to the txtWidget zone:
            painter.translate(topLeftPoint + xyTextOffset)
            # draw the txtWidget
            txtWidget.drawContents(painter)

        # -> It's done!
        painter.restore()
        

    def sizeHint(self, option, index):
        txt = index.model().data(index, KFERole.DisplayRole).toString()
        txtWidget = QTextDocument()
        if not index.parent().isValid():
            txt = "<b>"+txt+"</b>"
            txtWidget.setHtml(txt)
            txtSize = txtWidget.size().toSize()
            return txtSize
        else:
            txt = self.__formatContactDisplayRole(txt)
            txtWidget.setHtml(txt)
            txtSize = txtWidget.size().toSize()
            txtWidth  = txtSize.width()
            txtHeight = txtSize.height()
            return QSize( txtWidth,
                          max(txtHeight, self.dPS+ 2*self.dPMmin)  )
                          
    def __formatContactDisplayRole(self, txt):
        smileySize = 16
        if not txt.contains('<i></i>'):
            txt.replace('<i>','<br><i>')
        txt.replace('<img src', '<img width="%d" height="%d" src' % (smileySize, smileySize))
        return txt
