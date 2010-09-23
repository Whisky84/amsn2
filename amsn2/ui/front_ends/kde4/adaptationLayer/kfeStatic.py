# -*- coding: utf-8 -*-

from amsn2.views.menuview      import  MenuItemView
from PyKDE4.kdeui   import      KMainWindow,    \
                                KMenuBar
from PyQt4.QtCore   import      QObject,        \
                                SIGNAL

def kMenuBarFromMenuView(menuView, mainWindow):
    kMenuBar = KMenuBar()
    #TODO: Refactor this to support nested cascaded menus, and the other MenuView features
    for i in menuView.items:
        if i.type == MenuItemView.CASCADE_MENU:
            kMenu = kMenuBar.addMenu(i.label)
            for j in i.items:
                    kAction = kMenu.addAction(j.label)
                    QObject.connect(kAction, SIGNAL("triggered()"), j.command)
    kMenuBar.addMenu(mainWindow.helpMenu())
    return kMenuBar





def analyze(menuView, pref = ""):
    if menuView.items:
        for i in menuView.items:
            print pref + "label: %s, type: %s, icon: %s, accel: %s, radio: %s, disabled: %s" \
                    % (i.label, i.type, i.icon, i.accelerator, i.radio_value, i.disabled)
            print pref + " command: %s" % i.command
            analyze(i, pref+"\t")
            print ""