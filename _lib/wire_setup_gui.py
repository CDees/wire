# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wire_setup_gui.ui'
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

class Ui_wire_setup_display(object):
    def setupUi(self, wire_setup_display):
        wire_setup_display.setObjectName(_fromUtf8("wire_setup_display"))
        wire_setup_display.resize(301, 431)
        self.wire_setup_hostname = QtGui.QLineEdit(wire_setup_display)
        self.wire_setup_hostname.setGeometry(QtCore.QRect(50, 190, 131, 27))
        self.wire_setup_hostname.setText(_fromUtf8(""))
        self.wire_setup_hostname.setAlignment(QtCore.Qt.AlignCenter)
        self.wire_setup_hostname.setObjectName(_fromUtf8("wire_setup_hostname"))
        self.wire_setup_port = QtGui.QLineEdit(wire_setup_display)
        self.wire_setup_port.setGeometry(QtCore.QRect(190, 190, 61, 27))
        self.wire_setup_port.setText(_fromUtf8(""))
        self.wire_setup_port.setAlignment(QtCore.Qt.AlignCenter)
        self.wire_setup_port.setObjectName(_fromUtf8("wire_setup_port"))
        self.connection_label = QtGui.QLabel(wire_setup_display)
        self.connection_label.setGeometry(QtCore.QRect(30, 170, 121, 17))
        self.connection_label.setObjectName(_fromUtf8("connection_label"))
        self.line = QtGui.QFrame(wire_setup_display)
        self.line.setGeometry(QtCore.QRect(-3, 220, 311, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(wire_setup_display)
        self.line_2.setGeometry(QtCore.QRect(0, 150, 311, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(wire_setup_display)
        QtCore.QMetaObject.connectSlotsByName(wire_setup_display)

    def retranslateUi(self, wire_setup_display):
        wire_setup_display.setWindowTitle(_translate("wire_setup_display", "Wire: Setup", None))
        self.wire_setup_hostname.setPlaceholderText(_translate("wire_setup_display", "hostname", None))
        self.wire_setup_port.setPlaceholderText(_translate("wire_setup_display", "port", None))
        self.connection_label.setText(_translate("wire_setup_display", "Setup Connection", None))

