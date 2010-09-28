# -*- coding: utf-8 -*-

from adaptationLayer  import                            \
    KFESkinManager          as     SkinManager,         \
    KFESkin                 as     Skin,                \
    KFESplashScreen         as aMSNSplashScreen         \

from frontend import                                    \
    KFEChatWidget           as aMSNChatWidget,          \
    KFEChatWindow           as aMSNChatWindow,          \
    KFEContactListWidget    as aMSNContactListWidget,   \
    KFEContactListWindow    as aMSNContactListWindow,   \
    KFELoginWindow          as aMSNLoginWindow,         \
    KFEMainLoop             as aMSNMainLoop,            \
    KFEMainWindow           as aMSNMainWindow
    #kfeutil:
from frontend import                                    \
    KFEContactInputWindow   as aMSNContactInputWindow,  \
    KFEContactInputWindow   as aMSNContactDeleteWindow #Remove me!
    
from amsn2.ui.front_ends.kde4.adaptationLayer    import          \
    KFEAbstractErrorWindow          as  aMSNErrorWindow,        \
    KFEAbstractNotificationWindow   as  aMSNNotificationWindow, \
    KFEAbstractDialogWindow         as  aMSNDialogWindow,       \
    KFEAbstractGroupInputWindow     as  aMSNGroupInputWindow,   \
    KFEAbstractGroupDeleteWindow    as  aMSNGroupDeleteWindow,  \
                                                                \
    KFEDisplayPicChooser            as  aMSNDPChooserWindow,  \
    KFEFileChooser                  as  aMSNFileChooserWindow



"""KFEAbstractContactDeleteWindow  as  aMSNContactDeleteWindow,"""
