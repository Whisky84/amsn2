# -*- coding: utf-8 -*-

from amsn2.ui import base

class aMSNChatWindow(base.aMSNChatWindow):
    """ This interface will represent a chat window of the UI
        It can have many aMSNChatWidgets"""
    def __init__(self, amsn_core):
        print "NotImplementedError:\t\taMSNChatWindow.__init__()"

    def add_chat_widget(self, chat_widget):
        """ add an aMSNChatWidget to the window """
        print "NotImplementedError:\t\taMSNChatWindow.add_chat_widget()"

    """TODO: move, remove, detach, attach (shouldn't we use add ?), close,
        flash..."""


class aMSNChatWidget(base.aMSNChatWidget):
    """ This interface will present a chat widget of the UI """
    def __init__(self, amsn_conversation, parent, contacts_uid):
        """ create the chat widget for the 'parent' window, but don't attach to
        it."""
        print "NotImplementedError:\t\taMSNChatWidget.__init__()"

    def on_message_received(self, messageview):
        """ Called for incoming and outgoing messages
            message: a MessageView of the message"""
        print "NotImplementedError:\t\taMSNChatWidget.on_message_received()"

    def nudge(self):
        print "NotImplementedError:\t\taMSNChatWidget.nudge()"

