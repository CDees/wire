# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wire_connect_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wire_connect_display(object):
    def setupUi(self, wire_connect_display):
        wire_connect_display.setObjectName(_fromUtf8("wire_connect_display"))
        wire_connect_display.resize(301, 431)
        wire_connect_display.setFocusPolicy(QtCore.Qt.ClickFocus)
        wire_connect_display.setWindowOpacity(1.0)
        self.connection_label = QtGui.QLabel(wire_connect_display)
        self.connection_label.setGeometry(QtCore.QRect(20, 170, 121, 17))
        self.connection_label.setObjectName(_fromUtf8("connection_label"))
        self.line = QtGui.QFrame(wire_connect_display)
        self.line.setGeometry(QtCore.QRect(-13, 220, 311, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(wire_connect_display)
        self.line_2.setGeometry(QtCore.QRect(-10, 150, 311, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.wire_connect_hostname = QtGui.QLineEdit(wire_connect_display)
        self.wire_connect_hostname.setGeometry(QtCore.QRect(40, 190, 131, 27))
        self.wire_connect_hostname.setText(_fromUtf8(""))
        self.wire_connect_hostname.setAlignment(QtCore.Qt.AlignCenter)
        self.wire_connect_hostname.setObjectName(_fromUtf8("wire_connect_hostname"))
        self.wire_connect_port = QtGui.QLineEdit(wire_connect_display)
        self.wire_connect_port.setGeometry(QtCore.QRect(180, 190, 61, 27))
        self.wire_connect_port.setText(_fromUtf8(""))
        self.wire_connect_port.setAlignment(QtCore.Qt.AlignCenter)
        self.wire_connect_port.setObjectName(_fromUtf8("wire_connect_port"))

        self.retranslateUi(wire_connect_display)
        QtCore.QMetaObject.connectSlotsByName(wire_connect_display)

    def retranslateUi(self, wire_connect_display):
        wire_connect_display.setWindowTitle(_translate("wire_connect_display", "Wire: Connect", None))
        self.connection_label.setText(_translate("wire_connect_display", "Peer Connection", None))
        self.wire_connect_hostname.setPlaceholderText(_translate("wire_connect_display", "hostname", None))
        self.wire_connect_port.setPlaceholderText(_translate("wire_connect_display", "port", None))

